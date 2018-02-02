# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User, Three
from django.shortcuts import render, redirect
from django.contrib import messages



# Create your views here.
def index(request):
    return render(request, 'login/index.html')

def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully registered!")
    return redirect('/success')

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully logged in!")
    return redirect('/success')

def success(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')


    three = Three.objects.all()
    w =[]
    print request.session['user_id']

    for threetwo in three:
        if request.session['user_id'] == threetwo.fkonetom.id:
            w.append(threetwo)
    three = Three.objects.all()
    m =[]
    for threetwo in three:
        if request.session['user_id'] != threetwo.fkonetom.id:
            m.append(threetwo)
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'threes': Three.objects.order_by("travel_from"),
        'q':w,
        'd':m
    }
    return render(request, 'login/success.html', context)
def join(request):

    trip = Three.objects.get(id=three.id)

    trip.join.objects.create(trip=trip, appointments=user) 

    return redirect(reverse('/success'))
def new(request):
    user = User.objects.get(id=request.session['user_id'])

    errors = Three.objects.validate_appointment(request.POST)
    # a = Auction.objects.get(id=id)
    # a.bidder = user
    # print request.session['user_id']
    if len(errors) == 0:
        return redirect("/new")


        user = User.objects.get(id=request.session['user_id'])
        trip = Three.objects.create(destination=request.POST['destination'],description=request.POST['description'], fkonetom=user, travel_from=request.POST['travel_from'], travel_to=request.POST['travel_to'], user=user)

    else: 
        for err in errors:
            messages.error(request, err)
        return redirect('/add_new')
    
    # user.auctions = auction
    # user.save()

    #don't put many-to-many
    # print "hello"
    return redirect('/success')


def add_new(request):
    return render(request, 'login/new.html')

def new(request):
    user = User.objects.get(id=request.session['user_id'])
    errors = Three.objects.validate_appointment(request.POST)
    
    if len(errors) == 0:


        user = User.objects.get(id=request.session['user_id'])
        three = Three.objects.create(destination=request.POST['destination'],description=request.POST['description'], travel_from=request.POST['travel_from'], travel_to=request.POST['travel_to'], fkonetom=user)
        return redirect('/success')

    else: 
        for err in errors:
            messages.error(request, err)
        return redirect('/add_new')


def edit(request, id):
    b = Three.objects.get(id=id)

    
    context = {
        'b':b
    }
    return render(request, 'login/appointment.html', context)

def update(request, id):
    b = Three.objects.get(id=id)

    b.destination=request.POST['destination']
    b.description=request.POST['description'] 
    b.travel_from=request.POST['travel_from'] 
    b.travel_to=request.POST['travel_to']
    b.save()

    return redirect('/success')