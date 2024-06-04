
from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet, RegistroViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('curso', CursosViewSet, basename='Cursos')
router.register('registro', RegistroViewSet, basename='Registros')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
