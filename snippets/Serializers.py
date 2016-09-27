from rest_framework import serializers
from snippets.models import Pregunta, Genero, Libro, Usuario,Cupon


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ('correo', 'puntos')


class LibroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Libro
        fields = ('titulo','autor', 'descripcion','foto','genero')

class PreguntaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pregunta
        fields = ('pregu','rc', 'r','r2','r3','libro')

class GeneroSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genero
        fields = ('titulo',)

class CuponSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cupon
        fields = ('nombre','puntos','Descripcion')


