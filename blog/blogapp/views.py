from django.shortcuts import render, HttpResponse

# Create your views here.

# def home(index):
#     return HttpResponse("This is the Home Page")

def bloghome(request):
    return render (request, 'blog/bloghome.html')

def blogpost(request, slug):
    return render (request, 'blog/blogpost.html')
