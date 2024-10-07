from __future__ import annotations
from abc import ABC, abstractmethod


class Transformer(ABC):
    @abstractmethod
    def transform(self, data, *args, **kwargs):
        pass

    @abstractmethod
    def get_name(self, *args, **kwargs):
        return ""
