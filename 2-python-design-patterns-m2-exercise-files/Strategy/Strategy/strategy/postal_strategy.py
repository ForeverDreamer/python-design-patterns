from strategy.abc_strategy import AbsStrategy


class PostalStrategy(AbsStrategy):

    def calculate(self, order):
        return 5.00
