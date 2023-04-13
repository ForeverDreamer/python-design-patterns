"""电脑类"""


class Computer:

    def __init__(self, case=None, mainboard=None, cpu=None, memory=None, hard_drive=None, video_card=None):
        self._case = case
        self._mainboard = mainboard
        self._cpu = cpu
        self._memory = memory
        self._hard_drive = hard_drive
        self._video_card = video_card

    def display(self):
        print('Custom Computer:')
        print('\t{:>10}: {}'.format('Case', self._case))
        print('\t{:>10}: {}'.format('Mainboard', self._mainboard))
        print('\t{:>10}: {}'.format('CPU', self._cpu))
        print('\t{:>10}: {}'.format('Memory', self._memory))
        print('\t{:>10}: {}'.format('Hard drive', self._hard_drive))
        print('\t{:>10}: {}'.format('Video card', self._video_card))
