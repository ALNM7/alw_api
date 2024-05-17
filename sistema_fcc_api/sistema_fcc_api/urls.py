"""point_experts_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sistema_fcc_api.views import bootstrap
from sistema_fcc_api.views import users
from sistema_fcc_api.views import alumnos
from sistema_fcc_api.views import maestros
from sistema_fcc_api.views import materias
from sistema_fcc_api.views import auth

urlpatterns = [
    #Version
        path('bootstrap/version', bootstrap.VersionView.as_view()),
    #Crear Admin
        path('admin/', users.AdminView.as_view()),
    #Admin tabla
        path('lista-admins/', users.AdminAll.as_view()),
    #Editar Admin
        path('admins-edit/', users.AdminsViewEdit.as_view()),
    #Crear Alumno
        path('alumnos/', alumnos.AlumnosView.as_view()),
    #Alumno tabla
        path('lista-alumnos/', alumnos.AlumnosAll.as_view()),
    #editar alumno
        path('alumnos-edit/', alumnos.AlumnosViewEdit.as_view()),
    #crear Maestro
        path('maestros/', maestros.MaestrosView.as_view()),
    #maestro tabla
        path('lista-maestros/', maestros.MaestrosAll.as_view()),
    #Editar maestro 
        path('maestros-edit/', maestros.MaestrosViewEdit.as_view()),
    #Login
        path('token/', auth.CustomAuthToken.as_view()),
    #Logout
        path('logout/', auth.Logout.as_view()),



    #aqui vamos a colocar todo lo de materias 
        #para la tabla
        path('materias1/', materias.MateriasAll.as_view()),
        #para el registro de materias
        path('materias/', materias.MateriasView.as_view()),
        #para editarlas
        path('materias-edit/', materias.MateriasViewEdit.as_view())
]
