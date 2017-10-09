from rest_framework import  serializers, viewsets
from django.contrib.auth.models import User
from agenda.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=('url','username','email','is_staff')

class TipoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Tipo
        fields=('nome')
        
class AgendaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Agenda
        fields=('nome','tipo')

class CompromissoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Compromisso
        fields=('nome','data_e_hora_de_inicio','descricao','local','agenda')
        
class CompromissoUsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=CompromissoUsuario
        fields=('compromisso','usuario')
    
class AgendaUsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=AgendaUsuario
        fields=('agenda','usuario')

   
