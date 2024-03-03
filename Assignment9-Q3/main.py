import networkx as nx


def find_decomposition(budget, preferences):
    """
    Finds a decomposition of budget allocation based on citizens' preferences.

    Args:
        budget (float): A list of integers representing the budget for each subject.
        preferences (list): A list of sets representing citizens' preferences.

    Returns:
        tuple: A tuple containing a boolean indicating whether decomposition is possible and
        a dictionary representing the decomposition if possible, None otherwise.

    Examples:
        # Example 1: decomposable
        >>> budget = [400, 50, 50, 0]
        >>> preferences = [{0, 1}, {0, 2}, {0, 3}, {1, 2}, {0}]
        >>> is_decomposable, decomposition = find_decomposition(budget, preferences)
        >>> is_decomposable
        True
        >>> decomposition
        {'c0': {'s0': 100.0, 's1': 0, 's2': 0, 's3': 0}, 'c1': {'s0': 100.0, 's1': 0, 's2': 0, 's3': 0}, 'c2': {'s0': 100.0, 's1': 0, 's2': 0, 's3': 0}, 'c3': {'s0': 0, 's1': 50.0, 's2': 50.0, 's3': 0}, 'c4': {'s0': 100.0, 's1': 0, 's2': 0, 's3': 0}}

        # Example 2: decomposable
        >>> budget = [1500, 3000, 1500]
        >>> preferences = [{0, 1}, {1, 2}]
        >>> is_decomposable, decomposition = find_decomposition(budget, preferences)
        >>> is_decomposable
        True
        >>> decomposition
        {'c0': {'s0': 1500.0, 's1': 1500.0, 's2': 0}, 'c1': {'s0': 0, 's1': 1500.0, 's2': 1500.0}}

        # Example 3: decomposable
        >>> budget = [500, 300, 100]
        >>> preferences = [{0, 1}, {1, 2}, {0, 2}]
        >>> is_decomposable, decomposition = find_decomposition(budget, preferences)
        >>> is_decomposable
        True
        >>> decomposition
        {'c0': {'s0': 300.0, 's1': 0, 's2': 0}, 'c1': {'s0': 0, 's1': 300.0, 's2': 0}, 'c2': {'s0': 200.0, 's1': 0, 's2': 100.0}}

        # Example 4: Not decomposable
        >>> budget = [500, 0, 100, 0, 200]
        >>> preferences = [{0, 1}, {1, 2}, {1, 2}]
        >>> is_decomposable, decomposition = find_decomposition(budget, preferences)
        >>> is_decomposable
        False
        >>> decomposition
        {}

        # Example 5: Not decomposable
        >>> budget = [500, 0, 100, 0, 200]
        >>> preferences = [{0, 1}, {0, 4}, {1, 2}]
        >>> is_decomposable, decomposition = find_decomposition(budget, preferences)
        >>> is_decomposable
        False
        >>> decomposition
        {}
    """

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
        G.add_edge(f's{j}', 't', capacity=budget[j])

    # Find the maximum flow in the graph
    flow_value, flow_dict = nx.maximum_flow(G, 's', 't')

    # Check if the flow value equals the total budget
    if flow_value == C:
        decomposition = {}
        for i in range(n):
            decomposition[f'c{i}'] = {f's{j}': flow_dict.get(f'c{i}', {}).get(f's{j}', 0) for j in range(m)}
        return True, decomposition
    else:
        return False, {}


if __name__ == "__main__":
    import doctest

    doctest.testmod()
