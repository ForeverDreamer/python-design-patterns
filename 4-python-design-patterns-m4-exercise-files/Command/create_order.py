from abc_command import AbsCommand
from abc_order_command import AbsOrderCommand


class CreateOrder(AbsCommand):
    # name = 'CreateOrder'
    # description = '创建订单'

    # def __init__(self, name='CreateOrder', description='创建订单'):
    #     super(AbsCommand, self).__init__(name, description)

    def __init__(self, name='CreateOrder', description='创建订单'):
        super().__init__(name, description)

    def execute(self):
        print('订单创建成功！')

    # @property
    # def name(self):
    #     return self._name
    #
    # @property
    # def description(self):
    #     return self._description


if __name__ == '__main__':
    print(CreateOrder.mro())
    order = CreateOrder()
    print(order.name)
    print(order.description)
    order.execute()
