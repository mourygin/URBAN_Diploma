# Generated by Django 4.2.16 on 2024-10-15 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toy_department', '0008_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Buyer',
        ),
        migrations.DeleteModel(
            name='Toy',
        ),
    ]
