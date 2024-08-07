from cqrs.commands.command_handler import CommandHandler
from hotel.application.import_final_client_command import ImportFinalClientCommand
from hotel.domain.final_client_creator import FinalClientCreator
from hotel.domain.final_client_repository import FinalClientRepository


class ImportFinalClientCommandHandler(CommandHandler):
    def __init__(self, final_client_repository: FinalClientRepository, final_client_creator: FinalClientCreator):
        self.final_client_repository = final_client_repository
        self.final_client_creator = final_client_creator

    def handle(self, command: ImportFinalClientCommand):
        final_client = self.final_client_creator.create(
            id=command.id,
            name=command.name,
            email=command.email,
            created_at=command.created_at
        )
        self.final_client_repository.save_final_client(final_client)




