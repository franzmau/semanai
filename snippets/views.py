from django.shortcuts import render

# Create your views here.


from snippets.models import Libro,Usuario,Pregunta,Genero,Cupon
from rest_framework import viewsets
from snippets.Serializers import UserSerializer, LibroSerializer, PreguntaSerializer, GeneroSerializer,CuponSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer


class LibroViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer


class PreguntaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer


class GeneroViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class CuponViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Cupon.objects.all()
    serializer_class = CuponSerializer