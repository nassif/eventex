# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Subscription(models.Model):
	name = models.CharField(_('nome'),max_length=100)
	cpf = models.CharField(_('CPF'),max_length=11, unique=True)
	email = models.EmailField(_('E-mail'), unique=True)
	phone = models.CharField(_('Fone'),max_length=20, blank=True)
	created_at = models.DateTimeField(_('Criado em'),auto_now_add=True)

	class Meta:
		"""configurações que podem ser feitas no modelo """
		ordering = ['created_at']
		verbose_name=_(u'inscrição')
		verbose_name_plural=_(u'inscrições')

	def __unicode__(self):
		'	retorno padrão de texto '
		return self.name
