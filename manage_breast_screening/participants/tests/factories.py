from datetime import date

from factory.django import DjangoModelFactory

from .. import models


class ParticipantFactory(DjangoModelFactory):
    class Meta:
        model = models.Participant

    first_name = "Janet"
    last_name = "Williams"
    gender = "Female"
    nhs_number = "07700900829"
    phone = "07700900829"
    email = "janet.williams@example.com"
    date_of_birth = date(1959, 7, 22)
    ethnicity = ""
    address = ""
    risk_level = "Routine"
    extra_needs = []
