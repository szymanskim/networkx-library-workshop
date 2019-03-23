import networkx as nx
import timeout_decorator

from utils import profile, exit_after
from benchmark import TIMEOUT

@exit_after(TIMEOUT)
@profile
def average_degree(graph):
    return sum(d for _, d in nx.degree(graph))/graph.number_of_nodes()

@exit_after(TIMEOUT)
@profile
def betweenness(graph):
    return nx.betweenness_centrality(graph)

@exit_after(TIMEOUT)
@profile
def closeness(graph):
    return nx.closeness_centrality(graph)

@exit_after(TIMEOUT)
@profile
def clustering_coefficient(graph):
    return nx.clustering(graph)

@exit_after(TIMEOUT)
@profile
def pagerank(graph):
    return nx.pagerank(graph)

@exit_after(TIMEOUT)
@profile
def average_shortest_path_length(graph):
    path_lengths = [v for t in nx.all_pairs_shortest_path_length(graph) for k, v in t[1].items() if k is not t[0]]
    return sum(path_lengths) / len(path_lengths)

@exit_after(TIMEOUT)
@profile
def diameter(graph):
    return max([nx.diameter(g) for g in nx.connected_component_subgraphs(graph)])

@exit_after(TIMEOUT)
@profile
def number_of_connected_components(graph):
    return nx.number_connected_components(graph)

@exit_after(TIMEOUT)
@profile
def network_density(graph):
    return nx.density(graph)
