from datetime import datetime
from unittest.mock import MagicMock

import pytest

from manage_breast_screening.clinics.presenters import ClinicPresenter

from ..models import Clinic


@pytest.fixture
def mock_clinic():
    mock = MagicMock(spec=Clinic)

    mock.starts_at = datetime(2025, 1, 1, 9)
    mock.session_type.return_value = "All day"
    mock.clinic_slots.count.return_value = 10
    mock.setting.name = "Test setting"
    mock.time_range.return_value = {
        "start_time": datetime(2025, 1, 1, 9),
        "end_time": datetime(2025, 1, 1, 15),
    }
    mock.get_type_display.return_value = "Screening"
    mock.get_risk_type_display.return_value = "Routine"

    return mock


def test_clinic_presenter(mock_clinic):
    presenter = ClinicPresenter(mock_clinic)

    assert presenter.starts_at == "1 January 2025"
    assert presenter.session_type == "All day"
    assert presenter.number_of_slots == 10
    assert presenter.location_name == "Test setting"
    assert presenter.time_range == "9am to 3pm"
    assert presenter.type == "Screening"
    assert presenter.risk_type == "Routine"
