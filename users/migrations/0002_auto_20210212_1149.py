# Generated by Django 3.1.6 on 2021-02-12 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(help_text='Please enter your Region code (+91, +1, +92)', max_length=13),
        ),
    ]
