# Generated by Django 4.0.5 on 2022-06-03 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_profiles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='id',
        ),
        migrations.AlterField(
            model_name='profiles',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
