from abs_builder import AbsBuilder


class BudgetBoxBuilder(AbsBuilder):

    def get_case(self):
        self._computer._case = 'IN WIN BP655'
     
    def build_mainboard(self):
        self._computer._mainboard = 'ASRock AM1H-ITX'
        self._computer._cpu = 'AMD Athlon 5150'
        self._computer._memory = 'Kingston ValueRAM 4GB'

    def install_mainboard(self):
        print('install budget_box mainboard done!')

    def install_hard_drive(self):
        self._computer._hard_drive = 'WD Blue 1TB'

    def install_video_card(self):
        self._computer._video_card = 'On board'




