from autos.abs_auto import AbsAuto


class CadillacCTS(AbsAuto):

    @staticmethod
    def start():
        print('Cadillac CTS purring luxuriously.')

    @staticmethod
    def stop():
        print('Cadillac CTS shutting down.')
