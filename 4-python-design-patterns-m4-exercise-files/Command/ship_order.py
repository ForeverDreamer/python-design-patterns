from command_abc import AbsCommand
from order_command_abc import AbsOrderCommand


class ShipOrder(AbsCommand, AbsOrderCommand):
    name = 'ShipOrder'
    description = '订单发货'

    # def __init__(self, name='ShipOrder', description='订单发货'):
    #     super(AbsCommand, self).__init__(name, description)

    def __init__(self, *args):
        pass

    def execute(self):
        print('订单发货成功')
