from abc import ABC
from observer.abc_observer import AbsObserver


class AbsSubject(ABC):
    # _observers = set()

    def __init__(self):
        self._observers = set()
    
    def attach(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError('Observer not derived from AbsObserver')
        self._observers |= {observer}
        
    def detach(self, observer):
        self._observers -= {observer}
        
    def _notify(self, value=None):
        for observer in self._observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)


if __name__ == '__main__':
    print(AbsSubject())
