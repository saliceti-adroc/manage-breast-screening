from datetime import date

from django.db import models

from manage_breast_screening.clinics.models import BaseModel


class Participant(BaseModel):
    first_name = models.TextField()
    last_name = models.TextField()
    gender = models.TextField()
    nhs_number = models.TextField()
    phone = models.TextField()
    email = models.EmailField()
    date_of_birth = models.DateField()
    ethnicity = models.TextField()
    address = models.TextField()
    risk_level = models.TextField()
    extra_needs = models.JSONField(null=False, default=list)

    @property
    def full_name(self):
        return " ".join([name for name in [self.first_name, self.last_name] if name])

    def age(self):
        today = date.today()
        if (today.month, today.day) >= (
            self.date_of_birth.month,
            self.date_of_birth.day,
        ):
            return today.year - self.date_of_birth.year
        else:
            return today.year - self.date_of_birth.year - 1
