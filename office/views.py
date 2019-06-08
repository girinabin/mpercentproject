from django.shortcuts import render
from .forms import Postform
def add_request(request):
    if request.method == 'POST':
        form = Postform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Postform()
    return render(request,'office/base.html',{'form': form})
