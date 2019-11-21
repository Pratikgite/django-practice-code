# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django .shortcuts import render 
from .models import Company, Employee

def index(request):
    all_employee = Employee.objects.all()
    return render(request, 'employee/index.html', {'all_employee':all_employee})

def emp_detail(request, id):
    try:
        data = Employee.objects.get(id=id)
    except:
        raise Http404("Something wents wrong")
    return render(request, 'employee/index.html', {'data':data})
    # return HttpResponse("Welcome in ID-"+id)