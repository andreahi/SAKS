# -*- coding: cp1252 -*-
from django.db import models

from import_export import resources


# Create your models here.

class Tfunc:
    def upperstart(self, name):
        return "Andreas"
	
class Fravar(models.Model):
    elev = models.ForeignKey("Elev")
    fravardato = models.DateField('dato')
    timer = models.PositiveSmallIntegerField(default=0)
 #   kurs = models.OneToOneField("KursInstance", blank=True, null = True)
    kurs = models.ForeignKey('Kurs', blank=True, null=True)
    fravartyper = (
        ('gyldig','gyldig'), ('ugyldig','ugyldig')
)
    #fravartype = models.CharField(max_length=7, choices=fravartyper)
    
    class Meta:
        unique_together = ("fravardato", "elev")

class Kurs(models.Model):
    kursnavn = models.CharField(max_length=20)
    kursforkortelse = models.CharField(max_length=20)
    beskrivelse = models.CharField(max_length=200)
    def __unicode__(self):
        return self.kursforkortelse

class Larer(models.Model):
    navn = models.CharField(max_length=20)
    telefonnummer = models.CharField(max_length=8)
    def __unicode__(self):
        return self.navn
 

class KursInstance(models.Model):
    larere =  models.ManyToManyField(Larer)
    kurs = models.ForeignKey(Kurs)
    startdato = models.DateField()
    sluttdato = models.DateField()
    elever = models.ManyToManyField("Elev", blank=True)
    def __unicode__(self):
        return self.kurs.kursforkortelse
    

class Elev(models.Model):
    rettighet = models.CharField(max_length=30)
    fornavn = models.CharField(max_length=30, editable = True)
    etternavn = models.CharField(max_length=30, blank=True, null=True)
    def getnavn(self): return self.__navn
    def setnavn(self, value): self.__navn = value
    def delnavn(self): del self.__navn
    navn = property(getnavn, setnavn, delnavn)
    
    personnr = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)
    DUFnr = models.DecimalField(max_digits=11, decimal_places=0, blank=True, null=True)

    #kjonn_valg = (('mann','mann'), ('kvinne','kvinne'))
    bostedsadresse = models.CharField(max_length = 30)
    postnummer =models.PositiveIntegerField()
    sted = models.CharField(max_length = 30)
    
    RPNo =models.PositiveIntegerField(blank=True, null=True)
    s50 =models.PositiveIntegerField(blank=True, null=True)
    NBeh =models.PositiveIntegerField(blank=True, null=True)
    
    #kjonn = models.CharField(max_length=6, choices=kjonn_valg)
    #birthdate= models.DateField('birthdate')
    #language1 = models.CharField(max_length=30)
    #statsborgerskap = models.CharField(max_length=30)
    #comment = models.CharField(max_length=200, default=' ')
    #kurs =  models.ManyToManyField(KursInstance, blank=True)
    #aktivitet = models.CharField(max_length=40, choices=aktiviteter, blank=True)
    #startdato= models.DateField(blank=True, null=True)
    #sluttdato= models.DateField(blank=True, null=True)
    #antall_timer = models.PositiveSmallIntegerField(blank=True, default=0,verbose_name = r'Timer fullfort')
    vedtak = models.ManyToManyField("Norsk_vedtak", blank=True, null = True)
    skolegang = models.CharField(max_length = 200, blank=True)
    soketyper = (('oppholdstilatelse','oppholdstilatelse'), ('statsborgerskap','statsborgerskap'))
    soker = models.CharField('Soker', max_length=20, blank=True, choices = soketyper)
    deltagerkategorier = (('Rett/plikt','Rett/plikt'), ('Rett ','Rett'), ('Plikt ','Plikt'), ('Betaling ','Betaling'))
    deltagerkategori=models.CharField(max_length=20,blank=True, choices = deltagerkategorier)

    deltagerkategoriertid = (('Kveldsdeltagere','Kveldsdeltagere'), ('Dagdeltagere ','Dagdeltagere'))

    deltagerkategoritid=models.CharField(r'Deltagerkategori (tid)',max_length=20,blank=True, choices = deltagerkategoriertid)
    morsmal  = models.CharField(max_length=20, blank = True)
    def __unicode__(self):
        return self.fornavn + " " + self.etternavn
    def get_aktivitet(self, obj):
        return "\n".join([p.aktivitet for p in obj.vedtak.all()])
class Norsk_vedtak(models.Model):
    deltager = models.ForeignKey("Elev")
    aktiviteter = (
        ('Norsk og samf.kunnskap 300t', 'Norsk og samf.kunnskap 300t'),
        ('Norsk og samf.kunnskap 600t', 'Norsk og samf.kunnskap 600t'))
    vedtaker = (
        ('Innvilget norsk og samfunnskunnskap','Innvilget norsk og samfunnskunnskap'),
         ('Innvilget norsk','Innvilget norsk')
        )
    aktivitet = models.CharField(max_length=40,
                                    choices=aktiviteter)
    vedtakStatus = models.CharField(max_length=40,
                                    choices=vedtaker,
                                    verbose_name = r'Vedtak / status')
    vedtakStatusdato = models.DateField(verbose_name = r'Vedtak- / statusdato', blank=True, null=True)

    startdato= models.DateField()
    sluttdato= models.DateField()
    antall_timer = models.PositiveSmallIntegerField(blank=True,default=0)
    def __unicode__(self):
        return self.aktivitet + " " + self.vedtakStatusdato
    def get_aktivitet(self, obj):
        return "\n".join([p.aktivitet for p in obj.vedtak.all()])

from django.contrib import admin



    
from import_export.admin import ImportExportModelAdmin

class ElevResource(resources.ModelResource):
    list_display = ('get_aktivitet', 'vedtak')
    class Meta:
        model = Elev
            

class ElevAdmin(ImportExportModelAdmin):
    resource_class = ElevResource
    

