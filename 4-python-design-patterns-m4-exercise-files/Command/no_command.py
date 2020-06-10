from command_abc import AbsCommand


class NoCommand(AbsCommand):
    def __init__(self, args):
        self._command = args[0]
        # self.execute()

    def execute(self):
        print('No command named {}'.format(self._command))




