from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from .models import Animal
from .serializers import AnimalSerializer

class AnimalList(ListCreateAPIView):
  queryset = Animal.objects.all()
  serializer_class = AnimalSerializer
  
class AnimalDetail(RetrieveUpdateAPIView):
  queryset = Animal.objects.all()
  serializer_class = AnimalSerializer