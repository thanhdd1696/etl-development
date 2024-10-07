from __future__ import annotations
from abc import ABC, abstractmethod


class Extractor(ABC):
    @abstractmethod
    def extract(self, *args, **kwargs):
        pass

    @abstractmethod
    def get_name(self, *args, **kwargs):
        return ""
