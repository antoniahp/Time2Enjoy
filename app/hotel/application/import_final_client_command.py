from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

from cqrs.commands.command import Command

@dataclass(frozen=True)
class ImportFinalClientCommand(Command):
    id: UUID
    name: str
    email: str
    created_at: datetime