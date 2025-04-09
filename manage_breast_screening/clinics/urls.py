from django.urls import path

from . import views

app_name = "clinics"

urlpatterns = [
    # TODO: we will have something like
    # /clinics/{today,upcoming,completed,all}
    # /clinics/{id}
    path("", views.clinic_list, name="index"),
    path("<str:filter>/", views.clinic_list, name="index_with_filter"),
]
