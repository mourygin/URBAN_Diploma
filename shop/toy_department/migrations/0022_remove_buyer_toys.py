# Generated by Django 4.2.16 on 2024-12-13 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toy_department', '0021_remove_buyer_blocked_buyer_address_buyer_phone_nr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='toys',
        ),
    ]