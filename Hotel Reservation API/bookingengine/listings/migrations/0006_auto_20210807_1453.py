# Generated by Django 3.2 on 2021-08-07 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_auto_20210807_1439'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='listing',
            options={'ordering': ['price']},
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='price_per_night',
            new_name='price',
        ),
    ]
