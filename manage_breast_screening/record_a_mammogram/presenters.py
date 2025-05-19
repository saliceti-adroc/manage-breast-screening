import re

from django.urls import reverse

from ..clinics.models import Appointment
from ..utils.date_formatting import format_date, format_relative_date, format_time

Status = Appointment.Status


def sentence_case(value):
    """
    Capitalise the first letter of a sentence.

    >>> sentence_case('a quick brown fox jumps over the lazy dog')
    'A quick brown fox jumps over the lazy dog'

    Unlike the built in `capitalize` filter, this will preserve
    capital letters already in the string:

    >>> sentence_case('not in PACS')
    'Not in PACS'
    """
    if not value:
        return ""

    return value[0].upper() + value[1:]


def format_nhs_number(value):
    """
    Format an NHS number with spaces

    >>> format_nhs_number('9998887777')
    '999 888 7777'
    """
    if not value:
        return ""

    digits = re.sub(r"\s", "", value)

    return f"{digits[:3]} {digits[3:6]} {digits[6:]}"


def format_age(value: int) -> str:
    return f"{value} years old"


def status_colour(status):
    """
    Color to render the status tag
    """
    match status:
        case Status.CHECKED_IN:
            return ""  # no colour will get solid dark blue
        case Status.SCREENED:
            return "green"
        case Status.DID_NOT_ATTEND | Status.CANCELLED:
            return "red"
        case Status.ATTENDED_NOT_SCREENED | Status.PARTIALLY_SCREENED:
            return "orange"
        case _:
            return "blue"  # default blue


def present_secondary_nav(id):
    """
    Build a secondary nav for reviewing the information of screened/partially screened appointments.
    """
    return [
        {
            "id": "all",
            "text": "Appointment details",
            "href": reverse("record_a_mammogram:start_screening", kwargs={"id": id}),
            "current": True,
        },
        {"id": "medical_information", "text": "Medical information", "href": "#"},
        {"id": "images", "text": "Images", "href": "#"},
    ]


class AppointmentPresenter:
    def __init__(self, appointment):
        self._appointment = appointment
        self._last_known_screening = appointment.screening_episode.previous()

        self.allStatuses = Status
        self.id = appointment.id
        self.clinic_slot = ClinicSlotPresenter(appointment.clinic_slot)
        self.participant = ParticipantPresenter(
            appointment.screening_episode.participant
        )

    @property
    def status(self):
        colour = status_colour(self._appointment.status)

        return {
            "classes": f"nhsuk-tag--{colour} app-nowrap" if colour else "app-nowrap",
            "text": self._appointment.get_status_display(),
            "key": self._appointment.status,
            "is_confirmed": self._appointment.status == Status.CONFIRMED,
        }

    @property
    def last_known_screening(self):
        return (
            {
                "date": format_date(self._last_known_screening.created_at),
                "relative_date": format_relative_date(
                    self._last_known_screening.created_at
                ),
                # TODO: the current model doesn't allow for knowing the type and location of a historical screening
                # if it is not tied to one of our clinic slots.
                "location": None,
                "type": None,
            }
            if self._last_known_screening
            else {}
        )


class ClinicSlotPresenter:
    def __init__(self, clinic_slot):
        self._clinic_slot = clinic_slot
        self._clinic = clinic_slot.clinic

        self.clinic_id = self._clinic.id

    @property
    def clinic_type(self):
        return self._clinic.get_type_display().capitalize()

    @property
    def slot_time_and_clinic_date(self):
        clinic_slot = self._clinic_slot
        clinic = self._clinic

        return f"{format_time(clinic_slot.starts_at)} ({ clinic_slot.duration_in_minutes } minutes) - { format_date(clinic.starts_at) } ({ format_relative_date(clinic.starts_at) })"


class ParticipantPresenter:
    def __init__(self, participant):
        self._participant = participant

        self.extra_needs = participant.extra_needs
        self.ethnic_group = participant.ethnic_group
        self.full_name = participant.full_name
        self.nhs_number = format_nhs_number(participant.nhs_number)
        self.date_of_birth = format_date(participant.date_of_birth)
        self.age = format_age(participant.age())
        self.risk_level = sentence_case(participant.risk_level)

    @property
    def ethnic_group_category(self):
        category = self._participant.ethnic_group_category()
        if category:
            return category.replace("Any other", "any other")
        else:
            return None

    @property
    def address(self):
        address = self._participant.address
        if not address:
            return {}

        return {"lines": address.lines, "postcode": address.postcode}
