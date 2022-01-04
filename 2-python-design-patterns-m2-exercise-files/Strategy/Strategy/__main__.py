"""Classification: Behavioral"""

from strategy import *

order = Order()
# Test Federal Express shipping
sc = ShippingCost(FedExStrategy())
assert sc.calculate(order) == 3.0

# Test UPS shipping
sc = ShippingCost(UPSStrategy())
assert sc.calculate(order) == 4.0

# Test Postal Service shipping
sc = ShippingCost(PostalStrategy())
assert sc.calculate(order) == 5.0

print('Tests passed')
