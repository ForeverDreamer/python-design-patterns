from autos.abs_auto import AbsAuto


class ChevySpark(AbsAuto):

    @staticmethod
    def start():
        print('Chevy Spark running efficiently.')

    @staticmethod
    def stop():
        print('Chevy Spark shutting down.')
