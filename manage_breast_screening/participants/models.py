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
