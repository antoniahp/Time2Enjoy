from abc import ABC, abstractmethod
from hotel.domain.final_client import FinalClient


class FinalClientRepository(ABC):
    @abstractmethod
    def save_final_client(self, final_client:FinalClient) -> None:
        pass
