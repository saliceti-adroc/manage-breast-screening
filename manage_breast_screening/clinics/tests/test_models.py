from manage_breast_screening.clinics import models

from .factories import ClinicFactory


def test_clinic_is_scheduled():
    factory = ClinicFactory.build()
    assert factory.state == models.ClinicState.SCHEDULED[0]
