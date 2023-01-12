# Generated by Django 4.1.5 on 2023-01-12 04:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plate',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=50)),
            ],
        ),
    ]