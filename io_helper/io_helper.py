import networkx as nx

from utils import profile


@profile
def load_adjlist(filename):
    return nx.read_adjlist('networks/{}'.format(filename), comments='%')
