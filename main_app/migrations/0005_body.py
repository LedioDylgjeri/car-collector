# Generated by Django 4.1.3 on 2022-11-09 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_maintenance_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Body',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
    ]
