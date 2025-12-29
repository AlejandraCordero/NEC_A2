import random
import matplotlib.pyplot as plt
import networkx as nx

def is_valid_coloring(graph, chromosome):
    for u, v in graph.edges():
        if chromosome[u] == chromosome[v]:
            return False
    return True

# random chromosome
def create_chromosome(num_nodes, max_colors):
    return [random.randint(0, max_colors - 1) for _ in range(num_nodes)]
