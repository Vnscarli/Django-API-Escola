from django.contrib import admin
from escola.models import Aluno, Curso, Registro

class Alunos(admin.ModelAdmin):
    list_display= ('id', 'nome', 'matricula')
    list_display_links = ('id', 'nome')
    search_fields=('nome',)
    list_per_page=20

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display=('id', 'codigo_curso')
    list_display_links=('id', 'codigo_curso')
    search_fields=('codigo_curso',)

admin.site.register(Curso, Cursos)

class Registros(admin.ModelAdmin):
    list_display= ('id', 'aluno', 'curso', 'periodo')
    list_display_links = ('id',)
    list_per_page=20

admin.site.register(Registro, Registros)