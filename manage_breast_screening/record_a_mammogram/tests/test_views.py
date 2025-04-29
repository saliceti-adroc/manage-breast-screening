from django.urls import reverse
from pytest_django.asserts import assertContains, assertRedirects


class TestStartScreening:
    def test_appointment_continued(self, client):
        response = client.post(
            reverse("record_a_mammogram:start_screening"), {"decision": "continue"}
        )
        assertRedirects(
            response, reverse("record_a_mammogram:ask_for_medical_information")
        )

    def test_appointment_stopped(self, client):
        response = client.post(
            reverse("record_a_mammogram:start_screening"), {"decision": "dropout"}
        )
        assertRedirects(
            response, reverse("record_a_mammogram:appointment_cannot_go_ahead")
        )

    def test_renders_invalid_form(self, client):
        response = client.post(reverse("record_a_mammogram:start_screening"), {})
        assertContains(response, "There is a problem")
