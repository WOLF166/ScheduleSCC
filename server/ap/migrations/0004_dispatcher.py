# Generated by Django 5.1.3 on 2025-05-24 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0003_alter_schedule_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dispatcher',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('login', models.TextField()),
                ('password', models.TextField()),
            ],
        ),
    ]
