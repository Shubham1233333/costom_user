from django.http import request
from django.shortcuts import render
from .forms import Userform
from django.http import HttpResponse
# Create your views here.
def Home(request):
    print("vfhfrgrhrdhtgretfgrhtb")
    if request.method == "POST":
        form=Userform(request.POST)
        form.save()
        return HttpResponse("registered sucessfully")
    else:
            
        userform=Userform()
        d1={'username':userform}
        return render(request,'index.html',context=d1)
        