from __future__ import annotations
from abc import ABC, abstractmethod


class Loader(ABC):
    @abstractmethod
    def load(self, data, *args, **kwargs):
        pass

    @abstractmethod
    def get_name(self, *args, **kwargs):
        return ""
