from django.shortcuts import render
from django.db.models import *
from django.db import transaction
from sistema_fcc_api.serializers import *
from sistema_fcc_api.models import *
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.utils.html import strip_tags
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from datetime import datetime
from django.conf import settings
from django.template.loader import render_to_string
import string
import random
import json
#aqui se muestra la tabla de todas las materias
class MateriasAll(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        materias = Materias.objects.order_by("id")
        materias = MateriaSerializer(materias, many=True).data
        for materia in materias:
            materia["dias_json"] = json.loads(materia["dias_json"])
                
        return Response(materias, 200)

#View es para registrar
class MateriasView(generics.CreateAPIView):
    #Obtener usuario por ID
    # permission_classes = (permissions.IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        materia = get_object_or_404(Materias, id = request.GET.get("id"))
        materia = MateriaSerializer(materia, many=False).data
        materia["dias_json"] = json.loads(materia["dias_json"])
        return Response(materia, 200)
    
    #Registrar nuevo usuario
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        mate = MateriaSerializer(data=request.data)
        if mate.is_valid(): 
            #crea una materia nueva
            materia = Materias.objects.create(  nrc=request.data["nrc"],
                                                nombre_materia=request.data["nombre_materia"],
                                                seccion=request.data["seccion"],
                                                hora_inicio=request.data["hora_inicio"],
                                                hora_fin=request.data["hora_fin"],
                                                salon=request.data["salon"],
                                                programa_educativo=request.data["programa_educativo"],
                                                dias_json = json.dumps(request.data["dias_json"]))
            materia.save()
            return Response({"materia_created_id": materia.id}, 201)
        
        return Response(mate.errors ,status=status.HTTP_400_BAD_REQUEST)
    
class MateriasViewEdit(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        # iduser=request.data["id"]
        materia = get_object_or_404(Materias, id=request.data["id"])
        materia.nrc = request.data["nrc"]
        materia.nombre_materia = request.data["nombre_materia"]
        materia.seccion = request.data["seccion"]
        materia.hora_inicio = request.data["hora_inicio"]
        materia.hora_fin = request.data["hora_fin"]
        materia.salon = request.data["salon"]
        materia.programa_educativo = request.data["programa_educativo"]
        #jsondumps es para guardar arreglos en las bases de datos, lo transforma de valor 
        materia.dias_json = json.dumps(request.data["dias_json"])
        materia.save()
        #aqui vamos a serializar 
        user = MateriaSerializer(materia, many=False).data

        return Response(user,200)
    
    def delete(self, request, *args, **kwargs): #estructura de peticion
        profile = get_object_or_404(Materias, id=request.GET.get("id")) #el parametro materias es del modelo en -models.py-
        try:
            profile.delete()
            return Response({"details": "Todo bien Materia borrada"}, 200)
        except Exception as e:
            return Response({"details": "ERROR"}, 400)