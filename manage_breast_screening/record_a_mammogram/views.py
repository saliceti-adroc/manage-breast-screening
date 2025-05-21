import logging

from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.views.generic import FormView

from manage_breast_screening.clinics.models import Appointment

from ..clinics.models import Appointment
from .forms import (
    AppointmentCannotGoAheadForm,
    AskForMedicalInformationForm,
    RecordMedicalInformationForm,
    ScreeningAppointmentForm,
)
from .presenters import AppointmentPresenter, present_secondary_nav

Status = Appointment.Status

logger = logging.getLogger(__name__)


def status_color(status):
    """
    Color to render the status tag
    """
    match status:
        case Status.CHECKED_IN:
            return ""  # no colour will get solid dark blue
        case Status.SCREENED:
            return "green"
        case (Status.DID_NOT_ATTEND, Status.CANCELLED):
            return "red"
        case (Status.ATTENDED_NOT_SCREENED, Status.PARTIALLY_SCREENED):
            return "orange"
        case _:
            return "blue"  # default blue


class BaseAppointmentForm(FormView):
    @property
    def appointment_id(self):
        return self.kwargs["id"]

    def get_appointment(self):
        return get_object_or_404(
            Appointment.objects.prefetch_related(
                "clinic_slot",
                "screening_episode__participant",
                "screening_episode__participant__address",
            ),
            pk=self.appointment_id,
        )


class StartScreening(BaseAppointmentForm):
    template_name = "record_a_mammogram/start_screening.jinja"
    form_class = ScreeningAppointmentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        appointment = self.get_appointment()
        presenter = AppointmentPresenter(appointment)

        context.update(
            {
                "appointment": presenter,
                "caption": presenter.clinic_slot.clinic_type + " appointment",
                "title": presenter.participant.full_name,
                "decision_legend": "Can the appointment go ahead?",
                "decision_hint": "Before you proceed, check the participant’s identity and confirm that their last mammogram was more than 6 months ago.",
            }
        )

        if appointment.status in [
            appointment.Status.SCREENED,
            appointment.Status.PARTIALLY_SCREENED,
        ]:
            context["secondary_nav_items"] = present_secondary_nav(appointment.pk)

        return context

    def form_valid(self, form):
        form.save()

        if form.cleaned_data["decision"] == "continue":
            return redirect(
                "record_a_mammogram:ask_for_medical_information",
                id=self.get_appointment().pk,
            )
        else:
            return redirect(
                "record_a_mammogram:appointment_cannot_go_ahead",
                id=self.get_appointment().pk,
            )


class AskForMedicalInformation(BaseAppointmentForm):
    template_name = "record_a_mammogram/ask_for_medical_information.jinja"
    form_class = AskForMedicalInformationForm

    def form_valid(self, form):
        form.save()

        appointment = self.get_appointment()

        if form.cleaned_data["decision"] == "continue":
            return redirect(
                "record_a_mammogram:record_medical_information", id=appointment.pk
            )
        else:
            return redirect("record_a_mammogram:awaiting_images", id=appointment.pk)


class RecordMedicalInformation(BaseAppointmentForm):
    template_name = "record_a_mammogram/record_medical_information.jinja"
    form_class = RecordMedicalInformationForm

    def form_valid(self, form):
        form.save()

        appointment = self.get_appointment()

        if form.cleaned_data["decision"] == "continue":
            return redirect("record_a_mammogram:awaiting_images", id=appointment.pk)
        else:
            return redirect(
                "record_a_mammogram:appointment_cannot_go_ahead", id=appointment.pk
            )


def appointment_cannot_go_ahead(request, id):
    appointment = get_object_or_404(Appointment, pk=id)
    participant = appointment.screening_episode.participant
    if request.method == "POST":
        form = AppointmentCannotGoAheadForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect("clinics:index")
    else:
        form = AppointmentCannotGoAheadForm(instance=appointment)

    return render(
        request,
        "record_a_mammogram/appointment_cannot_go_ahead.jinja",
        {"form": form, "participant": participant},
    )


def awaiting_images(request, id):
    return render(request, "record_a_mammogram/awaiting_images.jinja", {})


@require_http_methods(["POST"])
def check_in(request, id):
    appointment = get_object_or_404(Appointment, pk=id)
    appointment.status = Appointment.Status.CHECKED_IN
    appointment.save()

    return redirect("record_a_mammogram:start_screening", id=id)
