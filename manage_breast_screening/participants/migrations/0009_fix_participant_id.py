import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("participants", "0008_alter_participantaddress_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="participantaddress",
            name="participant",
        ),
        migrations.AddField(
            model_name="participantaddress",
            name="participant",
            field=models.OneToOneField(
                on_delete=models.deletion.CASCADE,
                related_name="address",
                to="participants.participant",
            ),
        ),
    ]
