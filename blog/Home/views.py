from django.shortcuts import render, HttpResponse

# Create your views here.

def home(index):
    return HttpResponse("This is the Home Page")

def contact(index):
    return HttpResponse('This is the contact page')

def about(index):
    return HttpResponse('This is the about page')
