from typing import List
from abc import ABC, abstractmethod


class BaseTransformer(ABC):
    def __init__(self, extracted_data: dict) -> None:
        self.extracted_data = extracted_data

    @abstractmethod
    def transform_data(self) -> List[dict]:
        pass
