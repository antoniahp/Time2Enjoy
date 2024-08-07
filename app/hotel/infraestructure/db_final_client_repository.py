from hotel.domain.final_client import FinalClient
from hotel.domain.final_client_repository import FinalClientRepository


class DBFinalClientRepository(FinalClientRepository):

    def save_final_client(self, final_client:FinalClient) -> None:
        final_client.save()
        pass
