from datetime import datetime

from django.shortcuts import render

from .models import Clinic, Provider, Setting

STATUS_COLORS = {
    Clinic.State.SCHEDULED: "blue",  # default blue
    Clinic.State.IN_PROGRESS: "blue",
    Clinic.State.CLOSED: "grey",
}


def clinic_list(request, filter="today"):
    match filter:
        case "today":
            clinics = Clinic.objects.today()
        case "upcoming":
            clinics = Clinic.objects.upcoming()
        case "completed":
            clinics = Clinic.objects.completed()
        case _:
            clinics = Clinic.objects.all()

    return render(
        request,
        "clinics/index.html",
        context={
            "filter": filter,
            "filteredClinics": clinics,
            "filteredClinicCounts": {
                "all": Clinic.objects.count(),
                "today": Clinic.objects.today().count(),
                "upcoming": Clinic.objects.upcoming().count(),
                "completed": Clinic.objects.completed().count(),
            },
            "STATUS_COLORS": STATUS_COLORS,
        },
    )
