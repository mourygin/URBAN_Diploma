# Generated by Django 4.2.16 on 2024-12-16 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toy_department', '0023_remove_toy_age_limited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='buyer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='toy_department.buyer'),
        ),
        migrations.AlterField(
            model_name='basket',
            name='toy_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='toy_department.toy'),
        ),
    ]