# Generated by Django 4.2.16 on 2024-10-15 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('toy_department', '0007_delete_buyer_delete_toy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Toy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=7, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('description', models.CharField(blank=True, max_length=1024, null=True)),
                ('age_limited', models.BooleanField(default=False)),
                ('in_stock', models.IntegerField()),
                ('picture_min', models.CharField(default='', max_length=100)),
                ('picture_max', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=11)),
                ('age', models.IntegerField()),
                ('toys', models.ManyToManyField(related_name='toys', to='toy_department.toy')),
            ],
        ),
    ]
