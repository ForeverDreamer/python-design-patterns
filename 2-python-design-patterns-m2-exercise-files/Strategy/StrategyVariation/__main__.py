from strategy_variation import *


def fedex_strategy(order):
    return 3.0


ups_strategy = lambda order: 4.0

order = Order()

# Test Federal Express shipping
sc = ShippingCost(fedex_strategy)
assert sc.calculate(order) == 3.0

# Test UPS shipping
sc = ShippingCost(ups_strategy)
assert sc.calculate(order) == 4.0

# Test Postal Service shipping
sc = ShippingCost(lambda order: 5.0)
assert sc.calculate(order) == 5.0

print('Tests passed')
