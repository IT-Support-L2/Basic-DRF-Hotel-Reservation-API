# Generated by Django 3.2 on 2021-08-07 12:38

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField(default=20)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='bookinginfo',
            options={'ordering': ['price']},
        ),
        migrations.AlterModelOptions(
            name='hotelroom',
            options={'ordering': ['is_available']},
        ),
        migrations.AlterModelOptions(
            name='hotelroomtype',
            options={'ordering': ['price_per_night']},
        ),
        migrations.AddField(
            model_name='hotelroom',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='hotelroomtype',
            name='price_per_night',
            field=models.DecimalField(decimal_places=2, default=999.99, max_digits=6),
        ),
        migrations.AddField(
            model_name='listing',
            name='stars',
            field=models.SmallIntegerField(default=3, validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='hotelroom',
            name='hotel_room_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='listings.hotelroomtype'),
        ),
        migrations.AlterField(
            model_name='hotelroomtype',
            name='hotel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='listings.listing'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin_date', models.DateField(default=datetime.datetime.now)),
                ('checkout_date', models.DateField(default=datetime.datetime.now)),
                ('is_checkout', models.BooleanField(default=False)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.guest')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.hotelroom')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.hotelroomtype')),
            ],
        ),
    ]
