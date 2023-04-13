from abs_builder import AbsBuilder


class MyComputerBuilder(AbsBuilder):

    def get_case(self):
        self._computer._case = 'Coolermaster N300'
     
    def build_mainboard(self):
        self._computer._mainboard = 'MSI 970'
        self._computer._cpu = 'Intel Core i7-4770'
        self._computer._memory = 'Corsair Vengeance 16GB'

    def install_mainboard(self):
        print('install mycomputer mainboard done!')

    def install_hard_drive(self):
        self._computer._hard_drive = 'Seagate 2TB'

    def install_video_card(self):
        self._computer._video_card = 'GeForce GTX 1070'

