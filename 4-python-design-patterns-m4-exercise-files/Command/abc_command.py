from abc import ABC, abstractmethod


class AbsCommand(ABC):

    def __init__(self, name, description):
        self._name = name
        self._description = description

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @abstractmethod
    def execute(self):
        raise NotImplementedError
