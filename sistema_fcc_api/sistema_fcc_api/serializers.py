from rest_framework import serializers
from rest_framework.authtoken.models import Token
from sistema_fcc_api.models import *

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id','first_name','last_name', 'email')

class AdminSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Administradores
        fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Alumnos
        fields = "__all__"

class MaestroSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Maestros
        fields = '__all__'

#aqui colocaremos el serializer de materias

class MateriaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nrc = serializers.CharField(required=True)
    nombre_materia = serializers.CharField(required=True)
    seccion = serializers.CharField(required=True)
    hora_inicio = serializers.CharField(required=True)
    hora_fin = serializers.CharField(required=True)
    salon = serializers.CharField(required=True)
    programa_educativo = serializers.CharField(required=True)
    dias_json = serializers.JSONField(required=True)
