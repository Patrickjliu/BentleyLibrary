from django.shortcuts import render

def index(request):
    # Your view logic goes here
    return render(request, 'core/index.html')