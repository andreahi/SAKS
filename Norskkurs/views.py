# Create your views here.
# -*- coding: cp1252 -*-

from django.shortcuts import render_to_response
from django.shortcuts import render
from django import forms
from django.db import models

from Norskkurs.models import Elev
from Norskkurs.models import Fravar
from Norskkurs.models import Kurs
from Norskkurs.models import Larer
from Norskkurs.models import KursInstance
from Norskkurs.models import Norsk_vedtak

from django.forms import ModelForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.forms.models import model_to_dict
from django_tables2   import RequestConfig
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Count, Min, Sum, Avg
import django_tables2 as tables

from django.forms.extras.widgets import SelectDateWidget
from django.db.models import Q


from django_tables2.utils import A

class ElevForm(ModelForm):
    class Meta:
        model = Elev
        exclude = ['rettighet', 'RPNo','s50','NBeh']

class ElevTable(tables.Table):
    class Meta:
        model = Elev
        exclude = ['id','RPNo','s50','NBeh','postnummer']
    fornavn = tables.LinkColumn('detail', args=[A('pk')])
        
class KursForm(ModelForm):
    class Meta:
        model = Kurs
  
class Norsk_vedtakForm(ModelForm):
    class Meta:
        model = Norsk_vedtak
        exclude = ['antall_timer']
    sluttdato = forms.DateField(widget=forms.TextInput(attrs={'id': 'datepicker2','format' :'%d.%m.%Y'}))
    startdato = forms.DateField(widget=forms.TextInput(attrs={'id': 'datepicker','format' :'%d.%m.%Y'}))
    vedtakStatusdato = forms.DateField(widget=forms.TextInput(attrs={'id': 'datepicker3','format' :'%d.%m.%Y'}))

class KursInstanceForm(ModelForm):
    class Meta:
        model = KursInstance


class FravarForm(ModelForm):
    class Meta:
        model = Fravar

class LarerForm(ModelForm):
    class Meta:
        model = Larer

class KursInstanceTable(tables.Table):
    class Meta:
        model = KursInstance
     
 
class FravarTable(tables.Table):
    class Meta:
        model = Fravar
        exclude = ['elev','id']

class VedtakTable(tables.Table):
    class Meta:
        model = Norsk_vedtak
        exclude = ['deltager','id']


@login_required
def index(request):
    return render(request, 'Norskkurs/front/Publish/theme_02_design.html')


@login_required
def instillinger(request):
    return render(request, 'Norskkurs/front/Publish/instillinger.html')

@login_required
def fravar(request):
    return render(request,'Norskkurs/front/Publish/fravar.html')

#@login_required
#def visfravar(request):
#    table = FravarTable(Fravar.objects.all())
#    return render(request, "Norskkurs/front/Publish/visfravar.html", {'fravar': table})

@login_required
def visfravar(request):
    #table = FravarTable(Fravar.objects.all())
    table = None
    if request.method == 'POST':
        print request.POST
        if 'store' in request.POST:
            table = Fravar.objects.annotate(totalt_fravar=Sum('elev__fravar__timer')).values('elev__fornavn','totalt_fravar').distinct().filter(totalt_fravar__gt=30)
            return render(request, "Norskkurs/front/Publish/storstfravar.html", {'fravarliste': table})

    table = FravarTable(Fravar.objects.all())
    RequestConfig(request).configure(table)

    return render(request, "Norskkurs/front/Publish/visfravar.html", {'fravarliste': table})


def logout_view(request):
    logout(request)
    return render_to_response('Norskkurs/front/Publish/message.html',
    {'message_text':"Du er na logget ut"}, context_instance=RequestContext(request))

@login_required
def registrerfravar(request):
    if request.method == 'POST': # If the form has been submitted...
        form = FravarForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            #elev = Elev.objects.get(pk = form.cleaned_data['elev'].id)
            #elev.antall_timer += form.cleaned_data['timer']
            form.save()
            return render_to_response('Norskkurs/front/Publish/message.html',
    {'message_text':"Deltagelse lagt til"}, context_instance=RequestContext(request))

        #else:
            #self.add_error("nane", "error thingy")
            #raise forms.ValidationError("You did something wrong")
    else:
        form = FravarForm() # An unbound form

    return render(request, 'Norskkurs/front/Publish/registrerfravar.html', {
        'form': form,
    })
@login_required
def newelev(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ElevForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save()
            return render_to_response('Norskkurs/front/Publish/message.html',
    {'message_text':"Elev lagt til"}, context_instance=RequestContext(request))

        #else:
            #self.add_error("nane", "error thingy")
            #raise forms.ValidationError("You did something wrong")
    else:
        form = ElevForm() # An unbound form

    return render(request, 'Norskkurs/front/Publish/newelev.html', {
        'form': form})


@login_required
def adminkurs(request):
    if request.method == 'POST': # If the form has been submitted...
        form = KursForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save()
            return render_to_response('Norskkurs/front/Publish/message.html',
    {'message_text':"Kurs lagt til"}, context_instance=RequestContext(request))

        #else:
            #self.add_error("nane", "error thingy")
            #raise forms.ValidationError("You did something wrong")
    else:
        form = KursForm() # An unbound form

    return render(request, 'Norskkurs/front/Publish/adminkurs.html', {
        'form': form,
    })
@login_required
def adminlarer(request):
    if request.method == 'POST': # If the form has been submitted...
        form = LarerForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save()
            return render_to_response('Norskkurs/front/Publish/message.html',
    {'message_text':"Larer lagt til"}, context_instance=RequestContext(request))

        #else:
            #self.add_error("nane", "error thingy")
            #raise forms.ValidationError("You did something wrong")
    else:
        form = LarerForm() # An unbound form

    return render(request, 'Norskkurs/front/Publish/adminlarer.html', {
        'form': form,
    })
@login_required
def startkurs(request):
    if request.method == 'POST': # If the form has been submitted...
        form = KursInstanceForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save()
            return render_to_response('Norskkurs/front/Publish/message.html',
    {'message_text':"Kurs startet"}, context_instance=RequestContext(request))

        #else:
            #self.add_error("nane", "error thingy")
            #raise forms.ValidationError("You did something wrong")
    else:
        form = KursInstanceForm() # An unbound form

    return render(request, 'Norskkurs/front/Publish/adminlarer.html', {
        'form': form,
    })

class SearchForm(forms.Form):
    navn = forms.CharField(max_length=100, required=False,label='')


@login_required
def search(request):
    res = None
    if request.method == 'POST': # If the form has been submitted...
        form = SearchForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            name_s = form.cleaned_data['name']
            res = Elev.objects.all().filter(fornavn__icontains=name_s)
            
    else:
        form = SearchForm() # An unbound form

    return render(request, 'Norskkurs/front/Publish/search.html', {
        'form': form, 'res':res
    })
@login_required
def listall(request):
    res = None
    elev_list = ElevTable(Elev.objects.all())

    if request.method == 'POST': # If the form has been submitted...
        form = SearchForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            name_s = form.cleaned_data['navn']
            res = Elev.objects.all().filter( Q(fornavn__icontains=name_s) | Q(etternavn__icontains=name_s) | Q(bostedsadresse__icontains=name_s) |Q(sted__icontains=name_s))
            elev_list = ElevTable(res)    
    else:
        form = SearchForm() # An unbound form
        
        
    RequestConfig(request, paginate={"per_page": 6}).configure(elev_list)

    return render_to_response('Norskkurs/front/Publish/listall.html',
    {'elev_list':elev_list, 'form':form}, context_instance=RequestContext(request))

@login_required
def listallekurs(request):
    table = KursInstanceTable(KursInstance.objects.all())
    RequestConfig(request).configure(table)
    return render(request, "Norskkurs/front/Publish/listallekurs.html", {'fravar': table})

@login_required
def detail(request, elev_id):
    c = ElevForm(data=model_to_dict(Elev.objects.get(pk=elev_id)))
    fravar_list = FravarTable(Fravar.objects.all().filter(elev__id = elev_id))
    vedtak_list = VedtakTable(Norsk_vedtak.objects.all().filter(deltager__id = elev_id))

    res = None
    if request.method == 'POST': # If the form has been submitted...
        form = Norsk_vedtakForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            model_instance = form.save()
            model_instance.elev.add(Elev.objects.get(pk=elev_id))
            return render_to_response('Norskkurs/front/Publish/message.html',
    {'message_text':"Vedtak lagt til"}, context_instance=RequestContext(request))
            
    else:
        form = Norsk_vedtakForm() # An unbound form

    RequestConfig(request).configure(fravar_list)

    return render(request,'Norskkurs/front/Publish/detail.html',
                  {'elev':c,'fravar':fravar_list,'vedtak':vedtak_list, 'form': form})
#   return render(request, "Norskkurs/front/Publish/visfravar.html", {'fravar': table})

@login_required
def nyttvedtak(request):

    res = None
    if request.method == 'POST': # If the form has been submitted...
        form = Norsk_vedtakForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save()
            return render_to_response('Norskkurs/front/Publish/message.html',
    {'message_text':"Vedtak lagt til"}, context_instance=RequestContext(request))
            
    else:
        form = Norsk_vedtakForm() # An unbound form


    return render(request,'Norskkurs/front/Publish/nyttvedtak.html',
                  {'form': form})    
