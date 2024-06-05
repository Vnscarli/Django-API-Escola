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

class ListarAlunosCursoSerializer(serializers.ModelSerializer):
    aluno= serializers.ReadOnlyField(source='aluno.nome')
    matricula = serializers.ReadOnlyField(source='aluno.matricula')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model=Registro
        fields = ['aluno', 'matricula', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
