from rest_framework import serializers
from .models import Guest, HotelRoom, Booking, HotelRoomType, Listing

class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ("name", "age", "email")

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Listing
        fields = ("listing_type", "title", "stars", "country", "city", "price")

class HotelRoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = HotelRoomType
        fields = "__all__"


class HotelRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model  = HotelRoom
        fields = ("room_number", "is_available")


class BookingSerializer(serializers.ModelSerializer):
    guest = GuestSerializer()
    room = HotelRoomSerializer()

    class Meta:
        model  = Booking
        fields = ("guest", "room", "checkin_date", "checkout_date")