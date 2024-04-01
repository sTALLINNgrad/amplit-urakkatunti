from django.shortcuts import render
from django.http import HttpResponse

def start_page(request):
   context = {
        'message': 'Hello, World!'
    }
   return render(request, 'urakka_tunti/page.html', context) 

