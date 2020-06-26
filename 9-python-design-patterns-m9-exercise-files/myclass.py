from abs_class import AbsClass


class MyClass(AbsClass):

    @staticmethod
    def do_something(something):
        print('Doing %s.' % something)
