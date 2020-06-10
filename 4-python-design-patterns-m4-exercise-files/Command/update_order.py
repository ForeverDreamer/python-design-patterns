from command_abc import AbsCommand
from order_command_abc import AbsOrderCommand


class UpdateOrder(AbsCommand, AbsOrderCommand):
    name = 'UpdateQuantity'
    description = '更新商品数量'

    # def __init__(self, new_quantity, name='UpdateQuantity', description='更新商品数量'):
    #     super(AbsCommand, self).__init__(name, description)
    #     self._new_quantity = new_quantity

    def __init__(self, args):
        try:
            self._new_quantity = args[1]
        except IndexError:
            print('请提供更新数量！')
            exit()

    def execute(self):
        # Simulate database update
        print('Updated Database')

        # Simulate logging the update
        print('Logging: Updated quantity to {}'.format(self._new_quantity))
