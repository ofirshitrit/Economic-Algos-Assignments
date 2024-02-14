import random
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, stream=sys.stdout, format='%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

# Comment this line to see prints of the logger
logger.setLevel(logging.WARNING)

"""
The Weights Round Rubin Algorithm:
1. initialize: every player gets 0
2. while there are still objects:
    - for every player compute: his right / his current number of objects + y  
    - the player that his portion is the highest gets to choose his favorite object
"""


def get_choosing_player(num_players, players_chosen_objects, rights, y):
    """
    Get the player with the highest portion to choose his favorite object.

    >>> get_choosing_player(3, [1, 0, 2], [1, 2, 4], 0.5)
    1

    """

    max_portion = float('-inf')
    choosing_player = None

    # Computing the portion for each player
    for player in range(num_players):
        portion = rights[player] / (players_chosen_objects[player] + y)

        # Find the player with the highest portion
        if portion > max_portion:
            max_portion = portion
            choosing_player = player

    return choosing_player


def get_chosen_object(valuations, choosing_player):
    """
    Get the favorite object of the player with the highest portion.

    >>> get_chosen_object([[11, 22, 33], [44, 55, 66], [77, 88, 99]], 1)
    2

    """
    # The player with the highest portion choose from the remaining objects the object that he wants the most
    max_value = float('-inf')
    chosen_object = None
    for i, value in enumerate(valuations[choosing_player]):
        if value > max_value:
            max_value = value
            chosen_object = i
    return chosen_object


def weighted_round_rubin(rights, valuations, y):
    """
    Perform the Weights Round Rubin Algorithm.

    >>> weighted_round_rubin([1, 2, 4], [[11, 11, 22, 33, 44], [11, 22, 44, 55, 66], [11, 33, 22, 11, 66]], 0.5)
    Player 2 takes item 4 with value 66
    Player 1 takes item 3 with value 55
    Player 2 takes item 1 with value 33
    Player 0 takes item 2 with value 22
    Player 2 takes item 0 with value 11

    >>> weighted_round_rubin([1, 1, 1], [[10, 10, 10], [10, 10, 10], [10, 10, 10]], 1)
    Player 0 takes item 0 with value 10
    Player 1 takes item 1 with value 10
    Player 2 takes item 2 with value 10

    >>> weighted_round_rubin([1, 2, 3], [[10, 10, 10, 10, 10], [10, 10, 10, 10, 10], [10, 10, 10, 10, 10]], 0.5)
    Player 2 takes item 0 with value 10
    Player 1 takes item 1 with value 10
    Player 0 takes item 2 with value 10
    Player 2 takes item 3 with value 10
    Player 1 takes item 4 with value 10

    >>> weighted_round_rubin([1.5, 1.5, 4], [[11.1, 11.1, 22, 33.5], [11.5, 22, 44, 55], [11.6, 33, 22.6, 11]], 0.2)
    Player 2 takes item 1 with value 33
    Player 0 takes item 3 with value 33.5
    Player 1 takes item 2 with value 44
    Player 2 takes item 0 with value 11.6

    >>> weighted_round_rubin([1, 2, 3], [[10, 10, 10], [10, 10, 10], [10, 10, 10]], -0.5)
    Player 0 takes item 0 with value 10
    Player 0 takes item 1 with value 10
    Player 0 takes item 2 with value 10

    >>> weighted_round_rubin([1, 1, 1], [[10, 10, 10], [10, 10, 10], [10, 10, 10]], -0.5)
    Player 0 takes item 0 with value 10
    Player 0 takes item 1 with value 10
    Player 0 takes item 2 with value 10

    >>> weighted_round_rubin([1, 1, 1], [[10, 10, 10], [10, 10, 10], [10, 10, 10]], 2)
    Player 0 takes item 0 with value 10
    Player 1 takes item 1 with value 10
    Player 2 takes item 2 with value 10

    >>> weighted_round_rubin([1, 2, 3], [[10, 10, 10], [10, 10, 10], [10, 10, 10]], 2)
    Player 2 takes item 0 with value 10
    Player 1 takes item 1 with value 10
    Player 2 takes item 2 with value 10

    """
    num_players = len(rights)
    num_objects = len(valuations[0])
    remaining_objects = set(range(num_objects))

    logger.info(f"Remaining objects: {remaining_objects}")
    logger.info(f"Valuations: {valuations}")

    # List of how much objects each player took - at the beginning every player get 0
    players_chosen_objects = [0 for _ in range(num_players)]

    while remaining_objects:

        choosing_player = get_choosing_player(num_players, players_chosen_objects, rights, y)

        chosen_object = get_chosen_object(valuations, choosing_player)

        players_chosen_objects[choosing_player] += 1

        remaining_objects.remove(chosen_object)
        logger.info(f"Remaining objects: {remaining_objects}")

        print(
            f"Player {choosing_player} takes item {chosen_object} with value {valuations[choosing_player][chosen_object]}",
            flush=True)

        # Remove the chosen value at the chosen_object index from each player's valuation
        for player in range(num_players):
            valuations[player][chosen_object] = 0

        logger.info(f"Valuations: {valuations}")
        logger.info(f"Players chosen objects: {players_chosen_objects}")
    logger.info("\n")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
