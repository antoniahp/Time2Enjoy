from django.urls import path

from hotel.infraestructure.views.import_final_client_view import ImportFinalClientView

urlpatterns = [
    path("new_final_client/", ImportFinalClientView.as_view(), name="new-final-client"),
]