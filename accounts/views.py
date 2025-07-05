from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('Num1')
        password = request.POST.get('Num2')
        user = authenticate(request,username = username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home_page')
        else:
            return render(request,'login.html',{'error':'InvalidUser'})
    return render(request,'login.html')
def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('Num1')
        password = request.POST.get('Num2')
        con_password = request.POST.get('Num3')
        if(password != con_password):
            return render(request,'register.html',{'error':'error'})
        user = User.objects.create_user(username = username,password=password)
        return redirect('login_page')
    return render(request,'register.html')
def home_page(request):
    return render(request,'home.html')
def logout_page(request):
    logout(request)
    return redirect('login_page')