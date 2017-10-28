# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User


def index(request):

    return render(request,'login_app/index.html')


def create(request):
    results = User.objects.validator(request.POST)
    if results['status'] == True:
        user = User.objects.creator(request.POST)
        messages.success(request, 'User created')
        return redirect('/')
    else:
        for error in results['errors']:
            messages.error(request, error)
    return redirect('/')


def userPage(request):
    if not 'id' in request.session:
        messages.error(request,'Please log in again!')
        return redirect('/')
    else:
        return render(request,'login_app/user.html')


def login(request):
    results = User.objects.loginVal(request.POST)
    if results['status'] == False:
        messages.error(request, 'check email and password')
        return redirect('/')
    request.session['id'] = results['user'].id
    # request.session['email'] = results['user'].email
    # print request.session['email']
    request.session['first_name'] = results['user'].first_name
    #Change this route to route to the other app
    return redirect('wish/')


def logout(request):
    # request.session.flush()
    request.session.clear()
    return redirect('/')
