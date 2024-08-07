import json
from datetime import datetime
from uuid import uuid4

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from hotel.application.import_final_client_command import ImportFinalClientCommand
from hotel.application.import_final_client_command_handler import ImportFinalClientCommandHandler
from hotel.domain.final_client_creator import FinalClientCreator
from hotel.infraestructure.db_final_client_repository import DBFinalClientRepository


@method_decorator(csrf_exempt, name="dispatch")
class ImportFinalClientView(View):
    def __init__(self):
        super().__init__()
        self.__db_final_client_repository = DBFinalClientRepository()
        self.__db_final_client_creator = FinalClientCreator()
        self.__import_final_client_command_handler = ImportFinalClientCommandHandler(final_client_repository=self.__db_final_client_repository, final_client_creator=self.__db_final_client_creator)

    def post(self, request):
        data = json.loads(request.body)
        id = uuid4()
        created_at = datetime.now()

        command = ImportFinalClientCommand(
            id=id,
            name=data.get("name"),
            email=data.get("email"),
            created_at=created_at
        )

        self.__import_final_client_command_handler.handle(command)
        return JsonResponse({'id': str(id)}, status=201)