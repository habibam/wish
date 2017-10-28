# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login_app.models import User
from .models import Product
from django.contrib import messages

def index(request):
    if not 'id' in request.session:
        messages.error(request, 'Please log in again!')
        return redirect('/')
    context={
        'cur_user': User.objects.get(id=request.session['id']),
        'other_users': User.objects.filter(id=request.session['id']),
        'products': Product.objects.exclude(items__id=request.session['id']),
        'user_wishlist': Product.objects.filter(items__id=request.session['id']),
}
    return render(request,'wish_app/index.html', context)

def add(request):
    return render(request,'wish_app/add.html',{'cur_user': User.objects.get(id=request.session['id'])})

def create(request):
    user = User.objects.get(id=request.session['id'])

    if len(request.POST['product']) < 1:
        messages.error(request, "Product field can't be blank.")
        return redirect('/wish/add')

    elif not any(char.isalpha() for char in request.POST['product']):
        messages.error(request, "Product field must contain at a word and be at least 3 characters long.")
        return redirect('/wish/add')

    else:
        product = Product.objects.create(name=request.POST['product'])
        user.products.add(product)
    return redirect('/wish')

def show(request,id):
    return render(request,'wish_app/product.html', {'productInfo': Product.objects.get(id=id)})

def addProduct(request,id):
    product = Product.objects.get(id=id)
    user = User.objects.get(id=request.session['id'])
    user.products.add(product)
    return redirect('/wish')


def remove(request,id):
    product = Product.objects.get(id=id)
    user = User.objects.get(id=request.session['id'])
    user.products.remove(product)
    return redirect('/wish')

def userPage(request):
    return render(request,'wish_app/user.html', {'allProducts': Product.objects.all()})

def delete(request,id):
    Product.objects.get(id=id).delete()
    return redirect('/wish')

def api(request):
    return render(request,'wish_app/apiPrac.html')



