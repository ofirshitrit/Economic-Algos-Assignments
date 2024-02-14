import random

from main import *

running_time_rule1 = []
running_time_rule2 = []
running_time_both_rules = []


# To improve the running time we use rules of "pruning"

# Rule 1: delete identical states
def pruning_rule1(states):
    new_states = []
    length = len(states)

    for i in range(length):
        curr_state = states[i]

        # Check if curr_state is already in new_states
        if curr_state not in new_states:
            new_states.append(curr_state)

    states.clear()
    states.extend(new_states)


def egalitarian_allocation_rule1(valuations: list[list[float]]):
    start_time = time.time()
    initial_state = State(0, 0, 0)
    states = get_states(valuations, initial_state)
    pruning_rule1(states)
    final_state = max(states,
                      key=lambda state: min(state.valuation_of_player0, state.valuation_of_player1))
    path = find_path(initial_state, final_state)
    print_path(path)
    results = create_results(path)
    print_results(results, valuations, final_state)

    end_time = time.time()
    running_time = end_time - start_time
    running_time_rule1.append(running_time)
    return final_state


# Rule 2: delete every state where the optimistic bound is no better than the pessimistic bound
"""
Pessimistic bound: 
  the good result will not be worse - ex: divide the remaining objects randomlly 
Optimistic bound:
  the good result will not be better - ex: give the remaining objects to everyone  
"""
"""
State(state.number_of_objects + 1,
state.valuation_of_player0 + valuations[0][state.number_of_objects],
state.valuation_of_player1)
"""


def get_pessimistic_bound(state, remaining_objects, valuations):
    for object in range(remaining_objects):
        random_choice = random.randint(0, 1)
        if random_choice == 0:
            state.valuation_of_player0 += valuations[0][object]
        else:
            state.valuation_of_player0 += valuations[1][object]
        state.number_of_objects = state.number_of_objects + 1
    pessimistic_bound = min(state.valuation_of_player0, state.valuation_of_player1)
    return pessimistic_bound


def get_optimistic_bound(state, remaining_objects, valuations):
    for object in range(remaining_objects):
        state.valuation_of_player0 += valuations[0][object]
        state.valuation_of_player1 += valuations[1][object]
        state.number_of_objects = state.number_of_objects + 1
    optimistic_bound = min(state.valuation_of_player0, state.valuation_of_player1)
    return optimistic_bound


def pruning_rule2(states, total_objects, valuations):
    max_pessimistic_bound = 0
    for state in states:
        remaining_objects = total_objects - state.number_of_objects

        pessimistic_bound = get_pessimistic_bound(state, remaining_objects, valuations)
        if pessimistic_bound > max_pessimistic_bound:
            max_pessimistic_bound = pessimistic_bound

        optimistic_bound = get_optimistic_bound(state, remaining_objects, valuations)

        if optimistic_bound < pessimistic_bound:
            states.remove(state)


def egalitarian_allocation_rule2(valuations: list[list[float]]):
    start_time = time.time()
    initial_state = State(0, 0, 0)
    states = get_states(valuations, initial_state)
    pruning_rule2(states, len(valuations[0]), valuations)
    final_state = max(states,
                      key=lambda state: min(state.valuation_of_player0, state.valuation_of_player1))
    path = find_path(initial_state, final_state)
    print_path(path)
    results = create_results(path)
    print_results(results, valuations, final_state)
    end_time = time.time()
    running_time = end_time - start_time
    running_time_rule2.append(running_time)

    return final_state


def egalitarian_allocation_both_rules(valuations: list[list[float]]):
    start_time = time.time()
    initial_state = State(0, 0, 0)
    states = get_states(valuations, initial_state)
    pruning_rule1(states)
    pruning_rule2(states, len(valuations[0]), valuations)
    final_state = max(states,
                      key=lambda state: min(state.valuation_of_player0, state.valuation_of_player1))
    path = find_path(initial_state, final_state)
    print_path(path)
    results = create_results(path)
    print_results(results, valuations, final_state)
    end_time = time.time()
    running_time = end_time - start_time
    running_time_both_rules.append(running_time)

    return final_state


if __name__ == '__main__':
    # valuations = [[4, 5, 6, 7, 8], [8, 7, 6, 5, 4]]
    # valuations = [[4, 5, 6], [6, 5, 4]]
    # valuations = [[11, 55], [33, 44]]
    valuations = [[11, 55, 66], [33, 44, 22]]
    # valuations = [[11, 66], [44, 22]]
    # valuations = [[11, 22, 33, 44], [22, 11, 44, 33]]
    # results = {0: [1], 1: [0]}
    # print_outputs(results, valuations)

    # rule1_res = egalitarian_allocation_rule1(valuations)
    # print(f"\nrule1_res: {rule1_res}")

    rule2_res = egalitarian_allocation_rule2(valuations)
    print(f"\nrule2_res Allocation: {rule2_res}")
