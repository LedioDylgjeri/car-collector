# Generated by Django 4.1.3 on 2022-11-09 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_maintenance_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maintenance',
            options={'ordering': ['-date']},
        ),
    ]
