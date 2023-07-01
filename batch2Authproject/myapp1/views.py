from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login
from django.shortcuts import render
from .forms import NewUserForm

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'success.html')

    form = NewUserForm()
    return  render(request,'register.html',context={'register_form':form})

