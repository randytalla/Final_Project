from django.shortcuts import render, HttpResponse

# Create your views here.

# def home(index):
#     return HttpResponse("This is the Home Page")

def bloghome(index):
    return HttpResponse('This is the blog home page page')

def blogpost(request, slug):
    return HttpResponse(f'This is blog post: {slug}')
