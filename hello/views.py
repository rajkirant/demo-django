from django.shortcuts import render

# Create your views here1.
def index(request):
    return render(request, 'hello.html')
