# Generated by Django 2.0 on 2018-04-02 10:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.query_utils


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0005_auto_20180402_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(limit_choices_to=django.db.models.query_utils.Q(user_type='patient'), null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL),
        ),
    ]
