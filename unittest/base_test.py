from __future__ import annotations
from abc import ABC, abstractmethod


class BaseTest(ABC):
    @abstractmethod
    def test(self, data, *args, **kwargs):
        pass
