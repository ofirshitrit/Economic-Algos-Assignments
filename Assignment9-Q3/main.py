import networkx as nx


def find_decomposition(budget, preferences):
    C = sum(budget)
    n = len(preferences)
    m = len(budget)

    # Create a directed graph
    G = nx.DiGraph()

    # Add nodes for citizens and subjects
    for i in range(n):
        G.add_node(f'c{i}', demand=-C / n)  # demand for each citizen is -C/n
    for j in range(m):
        G.add_node(f's{j}')  # source node for each subject
        G.add_node(f't{j}')  # sink node for each subject

    # Add edges from source to citizens
    for i in range(n):
        G.add_edge('s', f'c{i}', capacity=C / n)

    # Add edges from citizens to subjects
    for i in range(n):
        for j in range(m):
            if j in preferences[i]:
                G.add_edge(f'c{i}', f's{j}', capacity=C / n)

    # Add edges from subjects to target
    for j in range(m):
        G.add_edge(f's{j}', 't', capacity=budget[j])  # fix here

    # Find the maximum flow in the graph
    flow_value, flow_dict = nx.maximum_flow(G, 's', 't')  # Here was the issue

    # Check if the flow value equals the total budget
    if flow_value == C:
        decomposition = {}
        for i in range(n):
            decomposition[f'c{i}'] = {f's{j}': flow_dict.get(f'c{i}', {}).get(f's{j}', 0) for j in range(m)}
        return True, decomposition
    else:
        return False, None


# Example usage
# 1. yes
# budget = [400, 50, 50, 0]
# preferences = [{0, 1}, {0, 2}, {0, 3}, {1, 2}, {0}]

# 2. yes
# budget = [1500, 3000, 1500]
# preferences = [{0, 1}, {1, 2}]

# 3. yes
# budget = [500, 300, 100]
# preferences = [{0, 1}, {1, 2}, {0, 2}]

# 4. No
budget = [500, 0, 100, 0, 200]
preferences = [{0, 1}, {1, 2}, {1, 2}]


is_decomposable, decomposition = find_decomposition(budget, preferences)
decomposable = "Yes" if is_decomposable else "No"

print("Is the budget decomposable?", decomposable)
if is_decomposable:
    print("Decomposition:")
    for citizen, allocation in decomposition.items():
        print(f"Citizen {citizen}: {allocation}")
