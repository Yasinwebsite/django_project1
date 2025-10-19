from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        password = make_password(password1)
        
        get_user_model().objects.create(
            username = username,
            password = password,
        )
        
        
    return render(request,"registration/signup.html")




def signup(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    form = UserCreationForm()
    context = {"form":form}
    return render(request,"registration/signup.html",context)
