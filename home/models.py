# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    codicedipendete = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Dipendeti(models.Model):

    #__Dipendeti_FIELDS__
    nome = models.CharField(max_length=255, null=True, blank=True)
    cognome = models.CharField(max_length=255, null=True, blank=True)
    data nasciata = models.DateTimeField(blank=True, null=True, default=timezone.now)
    codice = models.CharField(max_length=255, null=True, blank=True)

    #__Dipendeti_FIELDS__END

    class Meta:
        verbose_name        = _("Dipendeti")
        verbose_name_plural = _("Dipendeti")


class Cliente(models.Model):

    #__Cliente_FIELDS__
    ragione sociale = models.CharField(max_length=255, null=True, blank=True)
    partita iva = models.CharField(max_length=255, null=True, blank=True)

    #__Cliente_FIELDS__END

    class Meta:
        verbose_name        = _("Cliente")
        verbose_name_plural = _("Cliente")


class Progetto(models.Model):

    #__Progetto_FIELDS__
    descrizione = models.TextField(max_length=255, null=True, blank=True)
    data inizio = models.DateTimeField(blank=True, null=True, default=timezone.now)
    data fine prevista = models.DateTimeField(blank=True, null=True, default=timezone.now)
    data fine = models.DateTimeField(blank=True, null=True, default=timezone.now)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    responsabile = models.ForeignKey(Dipendeti, on_delete=models.CASCADE)

    #__Progetto_FIELDS__END

    class Meta:
        verbose_name        = _("Progetto")
        verbose_name_plural = _("Progetto")



#__MODELS__END
