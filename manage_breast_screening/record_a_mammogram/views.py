import logging

from django.shortcuts import redirect, render
from django.views.generic import FormView

from .forms import (
    AppointmentCannotGoAheadForm,
    AskForMedicalInformationForm,
    RecordMedicalInformationForm,
    ScreeningAppointmentForm,
)

logger = logging.getLogger(__name__)


class StartScreening(FormView):
    template_name = "record_a_mammogram/start_screening.jinja"
    form_class = ScreeningAppointmentForm

    def form_valid(self, form):
        form.save()

        if form.cleaned_data["decision"] == "continue":
            return redirect("record_a_mammogram:ask_for_medical_information")
        else:
            return redirect("record_a_mammogram:appointment_cannot_go_ahead")


class AskForMedicalInformation(FormView):
    template_name = "record_a_mammogram/ask_for_medical_information.jinja"
    form_class = AskForMedicalInformationForm

    def form_valid(self, form):
        form.save()

        if form.cleaned_data["decision"] == "continue":
            return redirect("record_a_mammogram:record_medical_information")
        else:
            return redirect("record_a_mammogram:awaiting_images")


class RecordMedicalInformation(FormView):
    template_name = "record_a_mammogram/record_medical_information.jinja"
    form_class = RecordMedicalInformationForm

    def form_valid(self, form):
        form.save()

        if form.cleaned_data["decision"] == "continue":
            return redirect("record_a_mammogram:awaiting_images")
        else:
            return redirect("record_a_mammogram:appointment_cannot_go_ahead")


class AppointmentCannotGoAhead(FormView):
    template_name = "record_a_mammogram/appointment_cannot_go_ahead.jinja"
    form_class = AppointmentCannotGoAheadForm


def awaiting_images(request):
    return render(request, "record_a_mammogram/awaiting_images.jinja", {})
