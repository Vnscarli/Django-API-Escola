from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from escola.models import Aluno, Curso, Registro
from escola.serializer import AlunoSerializer, CursoSerializer, RegistroSerializer, ListarAlunosCursoSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo a lista de alunos e alunas"""
    queryset=Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo os cursos"""
    queryset=Curso.objects.all()
    serializer_class=CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class RegistroViewSet(viewsets.ModelViewSet):
    """Exibindo Registros"""
    queryset=Registro.objects.all()
    serializer_class=RegistroSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
class ListaAlunoCurso(generics.ListAPIView):
    """Listando os registros de um curso"""
    def get_queryset(self):
        queryset= Registro.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class=ListarAlunosCursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    