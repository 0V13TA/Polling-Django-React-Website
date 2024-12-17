from rest_framework.viewsets import ModelViewSet
from .serializers import PersonSerializer
from ..models import Person


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
