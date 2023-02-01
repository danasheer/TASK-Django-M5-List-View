from .models import Booking, Flight
from rest_framework.generics import ListAPIView
from flights.models import Flight
from .serializers import ShowFlight, UpcomingBookingSerializer
from django.utils import timezone

class ArticleListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = ShowFlight

class UpcomingBookingView(ListAPIView):
    queryset = Booking.objects.filter(date__gt=timezone.now())
    serializer_class = UpcomingBookingSerializer