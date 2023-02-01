from .models import Booking, Flight
from rest_framework.generics import ListAPIView
from flights.models import Flight
from .serializers import ShowFlight

class ArticleListView(ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = ShowFlight

