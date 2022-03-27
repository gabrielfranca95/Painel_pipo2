from django.db import models

class Pampulha_Intermedica(models.Model):
	nome = models.CharField(u'Nome', max_length= 100 )
	cpf = models.CharField(u'CPF', blank=True, max_length = 14)
	data = models.DateField(u'Data de Admissão' )
	endereco = models.CharField(u'Endereço', blank=True, max_length = 200)

	class Meta:
		verbose_name ='Usuario do plano'
		verbose_name_plural ='Pampulha Intermédica'

	def __str__(self):
		return self.nome   



class Dental_Sorriso(models.Model):
	nome = models.CharField(u'Nome', max_length=100 )
	cpf = models.CharField(u'CPF', blank=True, max_length = 14)
	peso = models.CharField(u'Peso (kg)', blank=True, max_length = 10 )
	altura = models.CharField(u'Altura (cm)', blank=True, max_length = 200)

	class Meta:
		verbose_name ='Usuario do plano'
		verbose_name_plural ='Dental Sorriso'

	def __str__(self):
		return self.nome





class Mente_Sa_Corpo_Sao(models.Model):
	cpf = models.CharField(u'CPF', blank=True, max_length = 14)
	horas_meditadas = models.CharField(u'Horas Meditadas Nos Últimos 7 dias', blank=True, max_length = 200)

	class Meta:
		verbose_name ='Usuario do plano'
		verbose_name_plural ='Mente sã, Corpo São'

	def __str__(self):
		return self.cpf

    