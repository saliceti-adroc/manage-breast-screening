from pytest_django.asserts import assertFormError
import pytest

from manage_breast_screening.clinics.tests.factories import AppointmentFactory
from ..forms import AppointmentCannotGoAheadForm, ScreeningAppointmentForm


class TestScreeningAppointmentForm:
    def test_decision_cannot_be_left_blank(self):
        form = ScreeningAppointmentForm({})
        assertFormError(form, "decision", ["This field is required."])

@pytest.mark.django_db
class TestAppointmentCannotGoAheadForm:
    def test_reinvite_reflects_form_data(self):
        appointment = AppointmentFactory()
        form_data = {
            "stopped_reasons": ["failed_identity_check"],
            "decision": "True",
        }
        form = AppointmentCannotGoAheadForm(form_data, instance=appointment)
        form.is_valid()
        form.save()
        appointment.refresh_from_db()
        assert appointment.reinvite is True

        form_data = {
            "stopped_reasons": ["failed_identity_check"],
            "decision": "False",
        }
        form = AppointmentCannotGoAheadForm(form_data, instance=appointment)
        form.is_valid()
        form.save()
        appointment.refresh_from_db()
        assert appointment.reinvite is False


