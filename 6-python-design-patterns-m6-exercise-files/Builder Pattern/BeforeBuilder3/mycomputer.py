from computer import Computer


class MyComputer:

    def __init__(self):
        self._computer = None

    def get_computer(self):
        return self._computer

    def build_computer(self):
        self._computer = Computer()
        self._computer.case = 'Coolermaster N300'
        self._computer.mainboard = 'MSI 970'
        self._computer.cpu = 'Intel Core i7-4770'
        self._computer.memory = 'Corsair Vengeance 16GB'
        self._computer.hard_drive = 'Seagate 2TB'
        self._computer.video_card = 'GeForce GTX 1070'


