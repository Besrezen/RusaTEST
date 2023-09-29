from django.shortcuts import render
from .forms import FormaForm
import requests


# Create your views here.

def forma(request):
    if request.method == 'POST':
        form = FormaForm(request.POST, request.FILES)
        form.save()
        return render(request,'index.html')
    else:
        form = FormaForm()
        context = {'form': form}
        return render(request, 'forma.html', context)
