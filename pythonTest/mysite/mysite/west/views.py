# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from django.core.context_processors import csrf

from west.models import Character
from west.models import kind

from django import forms

def first_page(request):
    return HttpResponse("<p>西餐</p>")

'''
def staff(request):
    staff_list = Character.objects.all()
    staff_str  = map(str, staff_list)
    return HttpResponse("<p>" + ' '.join(staff_str) + "</p>")
'''

'''
def staff(request):
    staff_list  = Character.objects.all()
    staff_str  = map(str, staff_list)
    context   = {'label': ' '.join(staff_str)}
    return render(request, 'templay.html', context)
'''
def staff(request):
    staff_list = Character.objects.all()
    # return render(request, 'templay2.html', {'staffs': staff_list})
    return render(request, 'templay3_extend.html', {'staffs': staff_list})
    

def templay(request):
    context          = {}
    # context['label'] = 'Hello World!'
    context['label2'] = 'Hello World too!'
    return render(request, 'templay.html', context)

'''
#form get
def form(request):
    return render(request, 'form.html')

def investigate(request):
    rlt = request.GET['staff']
    return HttpResponse(rlt)
'''

'''
#form post
def form(request):
    return render(request, 'investigate.html')

def investigate(request):
    ctx ={}
    ctx.update(csrf(request))
    if request.POST:
        ctx['rlt'] = request.POST['staff']
    return render(request, "investigate.html", ctx)
'''

'''
# into mysql
def form(request):
    return render(request, 'investigate.html')

def investigate(request):
    if request.POST:
        submitted  = request.POST['staff']
        new_record = Character(name = submitted)
        new_record.save()
    ctx ={}
    ctx.update(csrf(request))
    all_records = Character.objects.all()
    ctx['staff'] = all_records
    return render(request, "investigate.html", ctx)
'''

#form object
class CharacterForm(forms.Form):
    name = forms.CharField(max_length = 200)

def investigate(request):
    if request.POST:
        form = CharacterForm(request.POST)
        if form.is_valid():
            submitted  = form.cleaned_data['name']
            new_record = Character(name = submitted)
            new_record.save()

    form = CharacterForm()
    ctx ={}
    ctx.update(csrf(request))
    all_records = Character.objects.all()
    ctx['staff'] = all_records
    ctx['form']  = form
    return render(request, "investigate.html", ctx)

def west_kind(request):
    ctx ={}
    all_kinds = kind.objects.all()
    ctx['kinds'] = all_kinds
    return render(request, "west_kind.html", ctx)
    
