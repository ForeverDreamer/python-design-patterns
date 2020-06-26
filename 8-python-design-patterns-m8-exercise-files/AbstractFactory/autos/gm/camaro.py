from autos.abs_auto import AbsAuto


class ChevyCamaro(AbsAuto):

    @staticmethod
    def start():
        print('Chevy Camaro V8 sounding awesome!')

    @staticmethod
    def stop():
        print('Chevy Camaro shutting down.')
