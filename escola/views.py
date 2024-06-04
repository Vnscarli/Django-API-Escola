from rest_framework import viewsets
from escola.models import Aluno, Curso, Registro
from escola.serializer import AlunoSerializer, CursoSerializer, RegistroSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo a lista de alunos e alunas"""
    queryset=Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo os cursos"""
    queryset=Curso.objects.all()
    serializer_class=CursoSerializer

class RegistroViewSet(viewsets.ModelViewSet):
    """Exibindo Registros"""
    queryset=Registro.objects.all()
    serializer_class=RegistroSerializer

