from django.shortcuts import render


def clinic_list(request):
    return render(request, "clinics_list.html", context={"clinics": []})
