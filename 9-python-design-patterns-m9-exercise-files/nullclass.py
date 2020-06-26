from abs_class import AbsClass


class NullClass(AbsClass):

    @staticmethod
    def do_something(something):
        print('Not doing %s.' % something)