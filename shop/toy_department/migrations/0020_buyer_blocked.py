# Generated by Django 4.2.16 on 2024-12-12 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toy_department', '0019_toy_actual_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='blocked',
            field=models.BooleanField(default=False),
        ),
    ]
