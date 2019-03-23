import argparse
import logging

import networkx as nx

from io_helper import load_adjlist
from measures import *

AVAILABLE_FILES = ['astroph', 'chicago', 'livemocha', 'youtube']
MEASURE_FUNCTIONS = [
    average_degree, number_of_connected_components, network_density, clustering_coefficient, pagerank, average_shortest_path_length, diameter, closeness, betweenness
]

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.DEBUG)


def main(filename):
    logging.info('Network: {}'.format(filename))

    logging.info('Loading network')
    g = load_adjlist(filename)

    print(nx.info(g))

    for func in MEASURE_FUNCTIONS:
        logging.info('Calculate {}'.format(func.__name__))
        result = func(g)
        if isinstance(result, (int, float)):
            logging.info('Calculated {}: {}'.format(func.__name__, result))


def parse_arguments():
    parser = argparse.ArgumentParser(description='Benchmark NetworkX Library.')
    parser.add_argument('-f', '--file', dest='filename', choices=AVAILABLE_FILES,
                        help='File to benchmark', required=True)
    args = parser.parse_args(sys.argv[1:])
    return args


if __name__ == "__main__":
    import sys
    args = parse_arguments()
    main(args.filename)
