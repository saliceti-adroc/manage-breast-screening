from django import forms


class ScreeningAppointmentForm(forms.Form):
    decision = forms.ChoiceField(
        choices=(
            ("continue", "Yes, go to medical information"),
            ("dropout", "No, screening cannot proceed"),
        ),
        required=True,
        widget=forms.RadioSelect(),
    )

    def save(self):
        pass


class AskForMedicalInformationForm(forms.Form):
    decision = forms.ChoiceField(
        choices=(
            ("continue", "Yes, mark incomplete sections as ‘none’ or ‘no’"),
            ("dropout", "No, screening cannot proceed"),
        ),
        required=True,
        widget=forms.RadioSelect(),
    )

    def save(self):
        pass


class RecordMedicalInformationForm(forms.Form):
    decision = forms.ChoiceField(
        choices=(
            ("continue", "Yes, go to medical information"),
            ("dropout", "No, screening cannot proceed"),
        ),
        required=True,
        widget=forms.RadioSelect(),
    )

    def save(self):
        pass


class AppointmentCannotGoAheadForm(forms.Form):
    pass
