from django.shortcuts import render
from.models import Place
from .models import Teams

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    objj=Teams.objects.all()
    return render(request, "index.html",{'result':obj,'member':objj})
