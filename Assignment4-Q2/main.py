"""
Search in the state space:
State is a vector with length n+1 such that: 
- The first element is the number of objects that was divided so far
- The rest n elements are the valuations of the players so far

The idea:
1. Initialize empty State: (0; 0,0)
2. For every object:
    For every exist State we will create more States by add one more object to the players
3. From all the last States , we choose the State with the max min value 

"""
import sys
import time
from State import State
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, stream=sys.stdout, format='%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

# Comment this line to see prints of the logger
logger.setLevel(logging.WARNING)


running_time_without_rules = []


def find_path(root, target_state, current_path=None):
    if current_path is None:
        current_path = []

    if root is None:
        return None

    current_path = current_path + [root]

    if root.isEqual(target_state):
        return current_path

    left_path = find_path(root.left, target_state, current_path.copy())
    right_path = find_path(root.right, target_state, current_path.copy())

    return left_path or right_path


def print_path(path):
    if path:
        logger.info("\nPath to leaf:")
        for state in path:
            logger.info(state)


def create_results(path):
    results = {0: [], 1: []}
    for (state, next_state) in zip(path, path[1:]):
        if state.valuation_of_player0 != next_state.valuation_of_player0:
            # player 0 take the current object
            results[0].append(state.number_of_objects)
        elif state.valuation_of_player1 != next_state.valuation_of_player1:
            # player 1 take the current object
            results[1].append(state.number_of_objects)
    logger.info("\nResults: ", results)
    return results


def print_player_results(player, results, final_state):
    objects = ', '.join(map(str, results[player]))
    total_value = getattr(final_state, f'valuation_of_player{player}')
    print(f"player {player} gets items {objects} with values {total_value}")


def print_results(results, valuations, final_state):
    print_player_results(0, results, final_state)
    print_player_results(1, results, final_state)


def add_new_states(current_states, valuations):
    new_states = []
    for state in current_states:
        # For every new state - nether player 0 gets the object or player 1 gets the object
        new_state_for_player0 = State(state.number_of_objects + 1,
                                      state.valuation_of_player0 + valuations[0][state.number_of_objects],
                                      state.valuation_of_player1)

        new_state_for_player1 = State(state.number_of_objects + 1,
                                      state.valuation_of_player0,
                                      state.valuation_of_player1 + valuations[1][state.number_of_objects])

        state.left = new_state_for_player0
        state.right = new_state_for_player1
        new_states.extend([new_state_for_player0, new_state_for_player1])
    return new_states


def get_states(valuations: list[list[float]], initial_state):
    number_of_objects = len(valuations[0])

    logger.info(f"Initial State: {initial_state.__str__()}")

    current_states = [initial_state]

    for i in range(number_of_objects):
        logger.info(f"\nObject {i}: ")
        new_states = add_new_states(current_states, valuations)

        logger.info("The new states: ")
        for i, state in enumerate(new_states):
            logger.info(f"State {i}: {state.__str__()}, Sum is: {state.valuation_of_player0 + state.valuation_of_player1}")
        current_states = new_states

    return current_states


def egalitarian_allocation(valuations: list[list[float]]):
    start_time = time.time()
    initial_state = State(0, 0, 0)
    states = get_states(valuations, initial_state)
    final_state = max(states,
                      key=lambda state: min(state.valuation_of_player0, state.valuation_of_player1))

    path = find_path(initial_state, final_state)
    print_path(path)
    results = create_results(path)
    print_results(results, valuations, final_state)
    end_time = time.time()
    running_time = end_time - start_time
    running_time_without_rules.append(running_time)
    return final_state


def max_product_allocation(valuations: list[list[float]]):
    initial_state = State(0, 0, 0)  # Assuming initial product is 1 for both players
    states = get_states(valuations, initial_state)
    final_state = max(states,
                      key=lambda state: state.valuation_of_player0 * state.valuation_of_player1)
    path = find_path(initial_state, final_state)
    print_path(path)
    results = create_results(path)
    print_results(results, valuations, final_state)
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
    result_state = egalitarian_allocation(valuations)
    # print(f"\nEgalitarian Allocation: {result_state}")

    # result_state1 = max_product_allocation(valuations)
    # print(f"\nmax_product_allocation: {result_state1}")
