from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    matricula = models.CharField(max_length=10)

    def __str__(self):
        return self.nome
    

class Curso(models.Model):
    codigo_curso=models.CharField(max_length=10)
    NIVEL=(
        ('B', 'Basico'),
        ('I', 'Intermediario'),
        ('A', 'Avancado')
    )
    
    nivel=models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    def __str__(self):
        return self.codigo_curso
    
class Registro(models.Model):
    PERIODO=(
        ('M', 'Manha'),
        ('T', 'Tarde'),
        ('N', 'Noite')
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo=models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')
    def __str__(self):
        return self.periodo