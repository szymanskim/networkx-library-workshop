import argparse
import logging
from datetime import datetime

import networkx as nx

from io_helper import load_adjlist
from measures import *

TIMEOUT = 7200

AVAILABLE_FILES = ['astroph', 'chicago', 'livemocha', 'youtube', 'all']

LOG_FILENAME = '{}.log'.format(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))
logging.basicConfig(filename=LOG_FILENAME, format='%(asctime)s - %(message)s', level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())

def main(filename):
    MEASURE_FUNCTIONS = [
        average_degree, number_of_connected_components, network_density, clustering_coefficient, pagerank, average_shortest_path_length, diameter, closeness, betweenness
    ]
    if filename == 'all':
        filenames = AVAILABLE_FILES[:-1]
    else:
        filenames = [filename]

    for file in filenames:
        logging.info('Network: {}'.format(file))

        logging.info('Loading network')
        g = load_adjlist(file)

        print(nx.info(g))

        for func in MEASURE_FUNCTIONS:
            try:
                result = func(g)
                if isinstance(result, (int, float)):
                    logging.info('Calculated {}: {}'.format(func.__name__, result))
                else:
                    logging.info('Calculated {}'.format(func.__name__))
            except:
                pass

def parse_arguments():
    parser = argparse.ArgumentParser(description='Benchmark NetworkX Library.')
    parser.add_argument('-f', '--file', dest='filename', choices=AVAILABLE_FILES,
                        help="File to benchmark ('all', for all files)", required=True)
    args = parser.parse_args(sys.argv[1:])
    return args


if __name__ == "__main__":
    import sys
    args = parse_arguments()
    main(args.filename)
