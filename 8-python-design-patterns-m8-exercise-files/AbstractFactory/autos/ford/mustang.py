from autos.abs_auto import AbsAuto


class FordMustang(AbsAuto):

    @staticmethod
    def start():
        print("Ford Mustang roaring and ready to go!")

    @staticmethod
    def stop():
        print('Ford Mustang shutting down.')
