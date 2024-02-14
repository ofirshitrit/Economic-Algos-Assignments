import logging
import sys

from main import egalitarian_allocation, running_time_without_rules
from pruning_rules import *
import matplotlib.pyplot as plt

# Configure logging
logging.basicConfig(level=logging.INFO, stream=sys.stdout, format='%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)

# Comment this line to see prints of the logger
logger.setLevel(logging.WARNING)


def running_egalitarian_allocation():
    # number of objects = [2 8 14 20 25]
    egalitarian_allocation([[1, 2], [3, 4]])
    logger.info("running time: ", running_time_without_rules)

    egalitarian_allocation([[1, 2, 5, 4, 6, 1, 3, 5], [8, 4, 9, 2, 6, 1, 5, 2]])
    logger.info("running time: ", running_time_without_rules)

    random_valuations_player0 = [random.randint(1, 10) for _ in range(14)]
    random_valuations_player1 = [random.randint(1, 10) for _ in range(14)]
    egalitarian_allocation([random_valuations_player0, random_valuations_player1])
    logger.info("running time: ", running_time_without_rules)

    random_valuations_player0 = [random.randint(1, 10) for _ in range(20)]
    random_valuations_player1 = [random.randint(1, 10) for _ in range(20)]
    egalitarian_allocation([random_valuations_player0, random_valuations_player1])
    logger.info("running time: ", running_time_without_rules)

    random_valuations_player0 = [random.randint(1, 10) for _ in range(25)]
    random_valuations_player1 = [random.randint(1, 10) for _ in range(25)]
    egalitarian_allocation([random_valuations_player0, random_valuations_player1])
    logger.info("running time: ", running_time_without_rules)


def display_plots_without_rules():
    running_egalitarian_allocation()
    x_values = [2, 8, 14, 20, 25]
    y_values = running_time_without_rules
    plt.plot(x_values, y_values,marker='o', label='Sample Data')
    # Add labels and title
    plt.xlabel('Number Of Products')
    plt.ylabel('Running Time')
    plt.title('Egalitarian Allocation Without Rules')
    plt.legend()
    plt.show()


def running_egalitarian_allocation_rule1():
    # number of objects = [2 6 8 14 17]
    egalitarian_allocation_rule1([[1, 2], [3, 4]])
    logger.info("running time: ", running_time_rule1)

    egalitarian_allocation_rule1([[1, 2, 5, 4, 6, 1], [8, 4, 9, 2, 6, 1]])
    logger.info("running time: ", running_time_rule1)

    egalitarian_allocation_rule1([[1, 2, 5, 4, 6, 1, 3, 5], [8, 4, 9, 2, 6, 1, 5, 2]])
    logger.info("running time: ", running_time_rule1)

    random_valuations_player0 = [random.randint(1, 10) for _ in range(14)]
    random_valuations_player1 = [random.randint(1, 10) for _ in range(14)]
    egalitarian_allocation_rule1([random_valuations_player0, random_valuations_player1])
    logger.info("running time: ", running_time_rule1)

    random_valuations_player0 = [random.randint(1, 10) for _ in range(17)]
    random_valuations_player1 = [random.randint(1, 10) for _ in range(17)]
    egalitarian_allocation_rule1([random_valuations_player0, random_valuations_player1])
    logger.info("running time: ", running_time_rule1)


def display_plots_with_rule1():
    running_egalitarian_allocation_rule1()
    x_values = [2, 6, 8, 14, 17]
    y_values = running_time_rule1
    plt.plot(x_values, y_values,marker='o', label='Sample Data')
    # Add labels and title
    plt.xlabel('Number Of Products')
    plt.ylabel('Running Time')
    plt.title('Egalitarian Allocation With Rule 1')
    plt.legend()
    plt.show()


def running_egalitarian_allocation_rule2():
    # number of objects = [2 6 8 14 17]
    egalitarian_allocation_rule2([[1, 2], [3, 4]])
    logger.info("running time: ", running_time_rule2)

    egalitarian_allocation_rule2([[1, 2, 5, 4, 6, 1], [8, 4, 9, 2, 6, 1]])
    logger.info("running time: ", running_time_rule2)

    egalitarian_allocation_rule2([[1, 2, 5, 4, 6, 1, 3, 5], [8, 4, 9, 2, 6, 1, 5, 2]])
    logger.info("running time: ", running_time_rule2)

    random_valuations_player0 = [random.randint(1, 10) for _ in range(14)]
    random_valuations_player1 = [random.randint(1, 10) for _ in range(14)]
    egalitarian_allocation_rule2([random_valuations_player0, random_valuations_player1])
    logger.info("running time: ", running_time_rule2)

    random_valuations_player0 = [random.randint(1, 10) for _ in range(17)]
    random_valuations_player1 = [random.randint(1, 10) for _ in range(17)]
    egalitarian_allocation_rule2([random_valuations_player0, random_valuations_player1])
    logger.info("running time: ", running_time_rule2)


def display_plots_with_rule2():
    running_egalitarian_allocation_rule2()
    x_values = [2, 6, 8, 14, 17]
    y_values = running_time_rule2
    plt.plot(x_values, y_values,marker='o', label='Sample Data')
    # Add labels and title
    plt.xlabel('Number Of Products')
    plt.ylabel('Running Time')
    plt.title('Egalitarian Allocation With Rule 2')
    plt.legend()
    plt.show()


def running_egalitarian_allocation_rules():
    # number of objects = [2 6 8 14 17]
    egalitarian_allocation_both_rules([[1, 2], [3, 4]])
    logger.info("running time: ", running_time_both_rules)

    egalitarian_allocation_both_rules([[1, 2, 5, 4, 6, 1], [8, 4, 9, 2, 6, 1]])
    logger.info("running time: ", running_time_both_rules)

    egalitarian_allocation_both_rules([[1, 2, 5, 4, 6, 1, 3, 5], [8, 4, 9, 2, 6, 1, 5, 2]])
    logger.info("running time: ", running_time_both_rules)

    random_valuations_player0 = [random.randint(1, 10) for _ in range(14)]
    random_valuations_player1 = [random.randint(1, 10) for _ in range(14)]
    egalitarian_allocation_both_rules([random_valuations_player0, random_valuations_player1])
    logger.info("running time: ", running_time_both_rules)

    random_valuations_player0 = [random.randint(1, 10) for _ in range(17)]
    random_valuations_player1 = [random.randint(1, 10) for _ in range(17)]
    egalitarian_allocation_both_rules([random_valuations_player0, random_valuations_player1])
    logger.info("running time: ", running_time_both_rules)


def display_plots_both_rules():
    running_egalitarian_allocation_rules()
    x_values = [2, 6, 8, 14, 17]
    y_values = running_time_both_rules
    plt.plot(x_values, y_values,marker='o', label='Sample Data')
    # Add labels and title
    plt.xlabel('Number Of Products')
    plt.ylabel('Running Time')
    plt.title('Egalitarian Allocation With Both Rules')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    display_plots_without_rules()
    # display_plots_with_rule1()
    # display_plots_with_rule2()
    # display_plots_both_rules()
