from django.urls import path

from . import views

app_name = "record_a_mammogram"

urlpatterns = [
    path(
        "appointments/<int:id>/check-in/",
        views.check_in,
        name="check_in",
    ),
    path(
        "appointments/<int:id>/start-screening/",
        views.StartScreening.as_view(),
        name="start_screening",
    ),
    path(
        "ask-for-medical-information/",
        views.AskForMedicalInformation.as_view(),
        name="ask_for_medical_information",
    ),
    path(
        "record-medical-information/",
        views.RecordMedicalInformation.as_view(),
        name="record_medical_information",
    ),
    path("awaiting-images/", views.awaiting_images, name="awaiting_images"),
    path(
        "appointment-cannot-go-ahead/",
        views.AppointmentCannotGoAhead.as_view(),
        name="appointment_cannot_go_ahead",
    ),
]
