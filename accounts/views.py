from django.core.checks import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == 'POST':
       first_name = request.POST['first_name']
       last_name = request.POST['last_name']
       username = request.POST['username']
       email = request.POST['email']
       password1 = request.POST['Password1']
       password2 = request.POST['Password2']
       if password1 == password2:
            if User.objects.filter(username=username).exists():
               messages.info(request,'Username Taken')
               return redirect('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request,"email taken")
                return redirect('register')
            else:
                user = User.objects.create(username = username ,first_name = first_name, last_name = last_name, email = email, password = password1)
                user.save()
                print("User Created")
       else:
            print('password not matchinng')
            messages.error(request,"password mismatch")
            return redirect('register')
       
       return redirect('login')
    else: 
        return render(request, 'register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username= username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'INVALID CREDENTIALS')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')