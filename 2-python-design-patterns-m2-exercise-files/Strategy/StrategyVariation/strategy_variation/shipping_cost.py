class ShippingCost:

    def __init__(self, strategy):
        self._strategy = strategy

    def calculate(self, order):
        return self._strategy(order)
