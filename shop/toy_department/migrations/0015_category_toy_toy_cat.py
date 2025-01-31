# Generated by Django 4.2.16 on 2024-12-07 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toy_department', '0014_basket_toy_descr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='toy',
            name='toy_cat',
            field=models.ManyToManyField(to='toy_department.category'),
        ),
    ]
