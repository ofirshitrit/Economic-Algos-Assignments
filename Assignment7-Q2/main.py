import networkx as nx


def vcg_cheapest_path(graph, source, target):
    shortest_path = nx.shortest_path(graph, source=source, target=target, weight='weight')

    total_cost = sum(graph[u][v]['weight'] for u, v in zip(shortest_path[:-1], shortest_path[1:]))

    edge_payments = {}

    for u, v in zip(shortest_path[:-1], shortest_path[1:]):
        weight = graph[u][v]['weight']
        graph.remove_edge(u, v)

        new_shortest_path = nx.shortest_path(graph, source=source, target=target, weight='weight')
        new_total_cost = sum(graph[u][v]['weight'] for u, v in zip(new_shortest_path[:-1], new_shortest_path[1:]))

        payment = new_total_cost - total_cost
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

