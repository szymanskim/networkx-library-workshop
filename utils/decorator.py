import logging
from functools import wraps
import sys
import threading
try:
    import thread
except ImportError:
    import _thread as thread

def profile(method):
    @wraps(method)
    def timed(*args, **kw):
        import time
        ts = time.perf_counter()
        logging.debug('[{}] Execution Start: {:06f} s'.format(method.__name__.upper(), ts))
        result = method(*args, **kw)
        te = time.perf_counter()
        logging.debug('[{}] Execution End:   {:06f} s'.format(method.__name__.upper(), te))
        time = (te - ts)
        logging.info('[{}] Execution Time:  {:06f} s'.format(method.__name__.upper(), time))
        return result
    return timed

def quit_function(fn_name, s):
    logging.info('[{}] Execution took too long (Timeout: {} s)'.format(fn_name.upper(), s))
    sys.stderr.flush()
    thread.interrupt_main()

def exit_after(s):
    def outer(fn):
        def inner(*args, **kwargs):
            inner.__name__ = fn.__name__
            timer = threading.Timer(s, quit_function, args=[fn.__name__, s])
            timer.start()
            try:
                result = fn(*args, **kwargs)
            finally:
                timer.cancel()
            return result
        return inner
    return outer