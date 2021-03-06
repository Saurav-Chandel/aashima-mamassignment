# Generated by Django 4.0.5 on 2022-06-03 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_user_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_image')),
                ('Country', models.CharField(blank=True, max_length=200, null=True)),
                ('City', models.CharField(blank=True, max_length=200, null=True)),
                ('State', models.CharField(blank=True, max_length=200, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('ZipCode', models.CharField(blank=True, max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
