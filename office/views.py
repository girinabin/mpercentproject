from django.shortcuts import render
from .models import post
from .forms import OperationRequest
# Create your views here.
def add_request(request):
    form = OperationRequest()
    if request.method == 'POST':
        form = OperationRequest(request.POST,request.FILES)#request.FILES must important
        if form.is_valid():
            form.save()
    return render(request,'office/operational.html',{'form': form})

def home(request):
    poost = post.objects
    return render(request,'office/home.html',{'post1':poost})