from abc_command import AbsCommand
from abc_order_command import AbsOrderCommand


class UpdateOrder(AbsCommand):
    # name = 'UpdateQuantity'
    # description = '更新商品数量'

    # def __init__(self, new_quantity, name='UpdateQuantity', description='更新商品数量'):
    #     super(AbsCommand, self).__init__(name, description)
    #     self._new_quantity = new_quantity

    # def __init__(self, args):
    #     try:
    #         self._new_quantity = args[1]
    #     except IndexError:
    #         print('请提供更新数量！')
    #         exit()

    def __init__(self, name='UpdateOrder', description='更新订单'):
        super().__init__(name, description)

    def execute(self):
        print('订单更新成功')
        # # Simulate database update
        # print('Updated Database')
        #
        # # Simulate logging the update
        # print('Logging: Updated quantity to {}'.format(self._new_quantity))
