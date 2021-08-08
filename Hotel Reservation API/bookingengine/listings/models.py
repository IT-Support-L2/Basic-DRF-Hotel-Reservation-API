from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from django.db.models.fields import EmailField
from django.dispatch import receiver
from django.db.models.signals import post_save


class Listing(models.Model):
    HOTEL = 'hotel'
    APARTMENT = 'apartment'
    LISTING_TYPE_CHOICES = (
        ('hotel', 'Hotel'),
        ('apartment', 'Apartment'),
    )

    listing_type = models.CharField(
        max_length=16,
        choices=LISTING_TYPE_CHOICES,
        default=APARTMENT
    )
    title = models.CharField(max_length=255,)
    country = models.CharField(max_length=255,)
    city = models.CharField(max_length=255,)
    stars = models.SmallIntegerField(default=3, validators=[MinValueValidator(3), MaxValueValidator(5)])
    price = models.DecimalField(default=999.99, max_digits=6, decimal_places=2)
    
    class Meta:
        ordering = ['price']

    def __str__(self):
        return self.title
    

class HotelRoomType(models.Model):
    hotel = models.ForeignKey(
        Listing,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    
    )
    title = models.CharField(max_length=255,)

    def __str__(self):
        return f'{self.hotel}'


class HotelRoom(models.Model):
    hotel_room_type = models.ForeignKey(
        HotelRoomType,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        
    )
    room_number = models.CharField(max_length=255,)
    is_available = models.BooleanField(default=True)
    class Meta:
        ordering = ['is_available']

    def __str__(self):
        return f'{str(self.hotel_room_type)} - {str(self.room_number)}'
class Guest(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(default=20)
    email = EmailField(max_length=100)

    def __str__(self):
        return self.name
class Booking(models.Model):
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    room  = models.ForeignKey(HotelRoom, on_delete=models.CASCADE)
    checkin_date = models.DateField(default=datetime.now)
    checkout_date = models.DateField(default=datetime.now)
    is_checkout = models.BooleanField(default=False)


    def __str__(self):
        return str(self.room)


@receiver(post_save,sender=Booking)
def  check_availability(sender, instance, created, **kwargs):
    room = instance.room
    if created:
        room.is_available = False
        room.save()
    if instance.checkout_date == True:
        room.is_available = True
        room.save()



