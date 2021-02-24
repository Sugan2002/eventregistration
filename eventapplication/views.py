from django.shortcuts import render
from .models import Participant
from django.core.exceptions import ValidationError
#Create your views here.
def home(request):
    context = {}
    return render(request, 'eventapplication/home.html', context)

def register(request):
    context = {}
    if request.method == 'POST':
        p1 = Participant()
        p1.username = request.POST.get('username','-')
        p1.email = request.POST.get('email','-')
        p1.email = request.POST.get('phone','-')
        p1.email = request.POST.get('insitution','-')

        if  len(Participant.objects.all())>10:
            return render(request,'eventapp/failed.html',context)
        else:
            p1.save()
            return render(request,'eventapp/success.html',context)
    if request.method == 'GET':
        context['username'] = ''
        context['email'] = ''
        context['phone'] = ''
        context['insitution'] = ''
    
    return render(request, 'eventapplication/register.html', context)

def listofparticipant(request):
    context = {}
    context['Participant'] = Participant.objects.all()

    return render(request, 'eventapplication/listofparticipant.html', context)

def success(request):
    context = {}
    return render(request, 'eventapplication/success.html', context)

def failed(request):
    context = {}
    return render(request, 'eventapplication/failed.html', context)

