import logging
from functools import wraps

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