class State:
    def __init__(self, number_of_objects, valuation_of_player0, valuation_of_player1, left=None, right=None):
        self.number_of_objects = number_of_objects
        self.valuation_of_player0 = valuation_of_player0
        self.valuation_of_player1 = valuation_of_player1
        self.left = left
        self.right = right

    def isEqual(self, other):
        return (self.number_of_objects == other.number_of_objects) and (
                self.valuation_of_player0 == other.valuation_of_player0) and (
                self.valuation_of_player1 == other.valuation_of_player1)

    def __str__(self):
        return f"({self.number_of_objects}; {self.valuation_of_player0}, {self.valuation_of_player1})"


