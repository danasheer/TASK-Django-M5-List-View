from rest_framework.generics import ListAPIView
from flights.models import Flight
from rest_framework import serializers

class ShowFlight(serializers.ModelSerializer):

    class Meta:
        model = Flight 
        fields = ['destination','time', 'price','miles']