# Generated by Django 2.2.7 on 2019-11-13 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('seudonimo', models.CharField(blank=True, max_length=20)),
                ('nombre', models.CharField(blank=True, max_length=20)),
                ('apellido', models.CharField(blank=True, max_length=20)),
                ('edad', models.CharField(blank=True, max_length=20)),
                ('sexo', models.CharField(blank=True, max_length=20)),
                ('hubicacion_inicial', models.CharField(blank=True, max_length=20)),
                ('pasa_tiempos_dia', models.CharField(blank=True, max_length=20)),
                ('pasa_tiempos_medio_dia', models.CharField(blank=True, max_length=20)),
                ('pasa_tiempos_noche', models.CharField(blank=True, max_length=20)),
                ('biography', models.TextField(blank=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='users/pictures')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
