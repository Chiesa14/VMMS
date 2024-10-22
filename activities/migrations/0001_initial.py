# Generated by Django 5.1.2 on 2024-10-22 08:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('maintenance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('maintenance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='maintenance.maintenanceschedule')),
            ],
            options={
                'db_table': 'activities',
            },
        ),
    ]
