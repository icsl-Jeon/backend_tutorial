from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from accountapp.models import HelloWorld
from django.urls import reverse


def hello_world(request):
    # return HttpResponse('Hello world!')
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        print(temp)
        new_hello_world.save()
        print('saved...?')
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': hello_world_list})
