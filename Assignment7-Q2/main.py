import networkx as nx
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, stream=sys.stdout, format='%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)


# Comment this line to see prints of the logger
# logger.setLevel(logging.WARNING)


def vcg_cheapest_path(graph, source, target):
    shortest_path = nx.shortest_path(graph, source=source, target=target, weight='weight')
    logger.info(f"shorted path: {shortest_path} ")

    total_cost = sum(graph[u][v]['weight'] for u, v in zip(shortest_path[:-1], shortest_path[1:]))
    logger.info(f"total_cost: {total_cost} ")


    edge_payments = {}

    for u, v in zip(shortest_path[:-1], shortest_path[1:]):
        weight = graph[u][v]['weight']
        graph.remove_edge(u, v)
        logger.info(f"u: {u}, v: {v}")

        new_shortest_path = nx.shortest_path(graph, source=source, target=target, weight='weight')
        logger.info(f"new_shortest_path: {new_shortest_path} ")

        curr_cost_without_uv = -sum(graph[u][v]['weight'] for u, v in zip(new_shortest_path[:-1], new_shortest_path[1:]))
        logger.info(f"curr_cost_without_uv: {curr_cost_without_uv} ")

        cost_of_cheapest_path_without_uv = total_cost - weight
        payment = curr_cost_without_uv + cost_of_cheapest_path_without_uv
        logger.info(f"payment: {payment} ")

        edge_payments[(u, v)] = payment
        graph.add_edge(u, v, weight=weight)

    return edge_payments


if __name__ == "__main__":
    G = nx.Graph()
    G.add_edge('A', 'B', weight=3)
    G.add_edge('A', 'C', weight=5)
    G.add_edge('A', 'D', weight=10)
    G.add_edge('B', 'C', weight=1)
    G.add_edge('B', 'D', weight=4)
    G.add_edge('C', 'D', weight=1)

    edge_payments = vcg_cheapest_path(G, 'A', 'D')

    for edge, payment in edge_payments.items():
        print()
        print(f"Edge {edge[0]} -> {edge[1]}: {payment}")
