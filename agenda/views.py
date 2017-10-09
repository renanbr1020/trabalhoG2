from django.shortcuts import render
from django.http import HttpResponse
from agenda.models import *
from rest_framework import routers, serializers, viewsets
from agenda.serializers import *
from django.contrib.auth.models import User

# Create your views here.

'''
def listaAgendas(request):
    
    retorno = "<h1> Todas as agendas </h1>"
    listaAgendas = Agenda.objects.all()
    for agenda in listaAgendas:
        retorno += '<br> Nome da agenda: {}<br> '.format(agenda.nome_Da_Agenda)
    return HttpResponse(retorno)
'''

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class TipoViewSet(viewsets.ModelViewSet):
    queryset=Tipo.objects.all()
    serializer_class=TipoSerializer

class AgendaViewSet(viewsets.ModelViewSet):
    queryset=Agenda.objects.all()
    serializer_class=AgendaSerializer

class CompromissoViewSet(viewsets.ModelViewSet):
    queryset=Compromisso.objects.all()
    serializer_class=CompromissoSerializer

class CompromissoUsuarioViewSet(viewsets.ModelViewSet):
    queryset=CompromissoUsuario.objects.all()
    serializer_class=CompromissoUsuarioSerializer

class AgendaUsuarioViewSet(viewsets.ModelViewSet):
    queryset=AgendaUsuario.objects.all()
    serializer_class=AgendaUsuarioSerializer


