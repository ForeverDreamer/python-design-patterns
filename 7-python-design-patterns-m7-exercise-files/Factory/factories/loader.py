from importlib import import_module
from inspect import getmembers, isabstract, isclass
from .abs_factory import AbsFactory


def load_factory(factory_name):
    try:
        factory_module = import_module('.' + factory_name, 'factories')
    except ImportError:
        factory_module = import_module('.null_factory', 'factories')
    
    classes = getmembers(factory_module, lambda m: isclass(m) and not isabstract(m) and issubclass(m, AbsFactory))
    return classes[0][1]()
    # for name, cls in classes:
    #     yield cls()
