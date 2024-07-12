from django.shortcuts import render

# Create your views here.

def index(request):
    print('consegui chegar na view')
    return render(request, 'index.html')