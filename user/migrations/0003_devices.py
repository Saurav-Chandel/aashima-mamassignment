# Generated by Django 4.0.5 on 2022-06-02 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DeviceToken', models.CharField(blank=True, max_length=250, null=True)),
                ('DeviceType', models.CharField(choices=[('iOS', 'iOS'), ('Android', 'Android')], max_length=500)),
                ('DateAdded', models.DateTimeField(default=django.utils.timezone.now)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]