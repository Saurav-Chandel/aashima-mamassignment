# Generated by Django 4.0.5 on 2022-06-02 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_devices'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=300)),
                ('token_type', models.CharField(choices=[('verification', 'Email Verification'), ('pwd_reset', 'Password Reset')], max_length=20)),
                ('created_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('expired_on', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
