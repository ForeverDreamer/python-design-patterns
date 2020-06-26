from autos.abs_auto import AbsAuto


class LincolnMKS(AbsAuto):

    @staticmethod
    def start():
        print('Lincoln MKS running smoothly.')

    @staticmethod
    def stop():
        print('Lincoln MKS shutting down.')
