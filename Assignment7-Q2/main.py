import networkx as nx
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, stream=sys.stdout, format='%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

# Comment this line to see prints of the logger
logger.setLevel(logging.WARNING)


def vcg_cheapest_path(graph, source, target):
    """
    This functon find the cheapest path from source to target and prints the cost of every edge in this path

    >>> G = nx.Graph()
    >>> G.add_edge('A', 'B', weight=3)
    >>> G.add_edge('A', 'C', weight=5)
    >>> G.add_edge('A', 'D', weight=10)
    >>> G.add_edge('B', 'C', weight=1)
    >>> G.add_edge('B', 'D', weight=4)
    >>> G.add_edge('C', 'D', weight=1)
    >>> vcg_cheapest_path(G, 'A', 'D')
    {('A', 'B'): -4, ('B', 'C'): -2, ('C', 'D'): -3}

    >>> G = nx.Graph()
    >>> G.add_edge('A', 'B', weight=3)
    >>> G.add_edge('A', 'C', weight=5)
    >>> G.add_edge('A', 'D', weight=10)
    >>> G.add_edge('B', 'C', weight=1)
    >>> G.add_edge('B', 'D', weight=4)
    >>> G.add_edge('C', 'D', weight=1)
    >>> vcg_cheapest_path(G, 'A', 'D')
    {('A', 'B'): -4, ('B', 'C'): -2, ('C', 'D'): -3}

    """
    shortest_path = nx.shortest_path(graph, source=source, target=target, weight='weight')
    logger.info(f"shorted path: {shortest_path} ")

    edges_cost = {}

    for u, v in zip(shortest_path[:-1], shortest_path[1:]):
        weight = graph[u][v]['weight']

        total_cost = sum(graph[u][v]['weight'] for u, v in zip(shortest_path[:-1], shortest_path[1:]))
        # compute the cost when the uv is exists
        cost_of_cheapest_path_with_uv = -(total_cost - weight)

        # remove the edge temporary
        graph.remove_edge(u, v)
        new_shortest_path = nx.shortest_path(graph, source=source, target=target, weight='weight')
        logger.info(f"new_shortest_path: {new_shortest_path} ")

        # compute the cost when the uv is not exists
        cost_of_cheapest_path_without_uv = -sum(graph[u][v]['weight'] for u, v in zip(new_shortest_path[:-1], new_shortest_path[1:]))
        logger.info(f"cost_of_cheapest_path_without_uv: {cost_of_cheapest_path_without_uv} ")

        cost = cost_of_cheapest_path_without_uv - cost_of_cheapest_path_with_uv
        logger.info(f"cost: {cost} ")

        edges_cost[(u, v)] = cost
        graph.add_edge(u, v, weight=weight)

    return edges_cost


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # G = nx.Graph()
    # G.add_edge('A', 'B', weight=3)
    # G.add_edge('A', 'C', weight=5)
    # G.add_edge('A', 'D', weight=10)
    # G.add_edge('B', 'C', weight=1)
    # G.add_edge('B', 'D', weight=4)
    # G.add_edge('C', 'D', weight=1)
    #
    # print(vcg_cheapest_path(G, 'A', 'D'))
