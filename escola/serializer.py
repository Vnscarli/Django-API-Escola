from rest_framework import serializers
from escola.models import Aluno, Curso, Registro

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Aluno
        fields = ['id', 'nome', 'matricula']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Curso
        fields = '__all__'

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Registro
        exclude = []

