from datetime import datetime
from uuid import UUID

from hotel.domain.final_client import FinalClient


class FinalClientCreator:
    def create(self, id:UUID, name:str, email:str, created_at:datetime):
        return FinalClient(
            id=id,
            name=name,
            email=email,
            created_at=created_at
        )
