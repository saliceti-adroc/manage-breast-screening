import pytest

from .factories import ParticipantFactory


class TestParticipant:
    @pytest.mark.parametrize(
        "category,group",
        [
            ("White", "English, Welsh, Scottish, Northern Irish or British"),
            ("Asian or Asian British", "Pakistani"),
            (None, None),
        ],
    )
    def test_ethnic_group_category(self, category, group):
        assert (
            ParticipantFactory.build(ethnic_group=group).ethnic_group_category()
            == category
        )
