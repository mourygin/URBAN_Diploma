# Generated by Django 4.2.16 on 2024-12-12 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toy_department', '0020_buyer_blocked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buyer',
            name='blocked',
        ),
        migrations.AddField(
            model_name='buyer',
            name='address',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='buyer',
            name='phone_nr',
            field=models.CharField(default='', max_length=16),
        ),
    ]
