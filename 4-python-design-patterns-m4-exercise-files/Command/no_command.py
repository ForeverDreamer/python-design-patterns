from abc_command import AbsCommand


class NoCommand(AbsCommand):
    def __init__(self, name='NoCommand', description='命令不存在'):
        super().__init__(name, description)

    def execute(self):
        print('No command named {}'.format(self.name))




