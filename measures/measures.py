import networkx as nx

from utils import profile


@profile
def average_degree(graph):
    return sum(d for _, d in nx.degree(graph))/graph.number_of_nodes()

@profile
def betweenness(graph):
    return nx.betweenness_centrality(graph)

@profile
def closeness(graph):
    return nx.closeness_centrality(graph)

@profile
def clustering_coefficient(graph):
    return nx.clustering(graph)

@profile
def pagerank(graph):
    return nx.pagerank(graph)

@profile
def average_shortest_path_length(graph):
    path_lengths = [v for t in nx.all_pairs_shortest_path_length(graph) for k, v in t[1].items() if k is not t[0]]
    return sum(path_lengths) / len(path_lengths)

@profile
def diameter(graph):
    return max([nx.diameter(g) for g in nx.connected_component_subgraphs(graph)])

@profile
def number_of_connected_components(graph):
    return nx.number_connected_components(graph)

@profile
def network_density(graph):
    return nx.density(graph)
