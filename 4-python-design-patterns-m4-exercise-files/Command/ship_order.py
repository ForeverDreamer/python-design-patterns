from abc_command import AbsCommand
from abc_order_command import AbsOrderCommand


class ShipOrder(AbsCommand):
    # name = 'ShipOrder'
    # description = '订单发货'

    # def __init__(self, name='ShipOrder', description='订单发货'):
    #     super(AbsCommand, self).__init__(name, description)

    def __init__(self, name='ShipOrder', description='订单发货'):
        super().__init__(name, description)

    def execute(self):
        print('订单发货成功')
