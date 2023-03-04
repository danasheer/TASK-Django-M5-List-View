from .models import Booking, Flight
from rest_framework.generics import ListAPIView
from flights.models import Flight
from .serializers import ShowFlightSerializer, UpcomingBookingSerializer
from django.utils import timezone


class ArticleListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = ShowFlightSerializer


class UpcomingBookingView(ListAPIView):
    queryset = Booking.objects.filter(date__gt=timezone.now())
    serializer_class = UpcomingBookingSerializer
