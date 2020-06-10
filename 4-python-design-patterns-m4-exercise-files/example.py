class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        self.i = 123
        return 'hello world'


m = MyClass()
print(MyClass.i)
print(m.i)
r = m.f()
print(m.i)

print(r)
