from datetime import datetime

import pytest
import time_machine
from pytest_django.asserts import assertQuerySetEqual

from manage_breast_screening.clinics import models

from .factories import ClinicFactory


def test_clinic_is_scheduled():
    factory = ClinicFactory.build()
    assert factory.state == models.Clinic.State.SCHEDULED


@pytest.mark.django_db
@time_machine.travel(datetime(2025, 1, 1, 10))
def test_status_filtering():
    current = ClinicFactory.create(starts_at=datetime(2025, 1, 1, 9))
    future = ClinicFactory.create(starts_at=datetime(2025, 1, 2, 9))
    past = ClinicFactory.create(starts_at=datetime(2024, 1, 1, 9))

    assertQuerySetEqual(
        models.Clinic.objects.all(), {current, future, past}, ordered=False
    )
    assertQuerySetEqual(models.Clinic.objects.today(), {current}, ordered=False)
    assertQuerySetEqual(models.Clinic.objects.upcoming(), {future}, ordered=False)
    assertQuerySetEqual(models.Clinic.objects.completed(), {past}, ordered=False)
