from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import User_Login

def user_login(request):
    user = User_Login.objects.all()
    
    if request.method == 'POST':
        
        if 'login' in request.POST:
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            if username and password:
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("home")
                else:
                    messages.error(request, "The Username or Password is incorrect!")
                    return render(request, "login/login.html")
                
        elif 'signup' in request.POST:
            username_su = request.POST.get('username_su')
            password_su = request.POST.get('password_su')
            password_2_su = request.POST.get('password_2_su')
            
            if username_su and password_su and password_2_su:
                not_unq_username = User_Login.objects.filter(username=username_su).exists()
                
                if not_unq_username:
                    messages.error(request, "The Username does exists ! Please enter enother Username.")
                    return render(request, "login/login.html")
                
                elif password_su != password_2_su:
                    messages.error(request, "The Password is not valid !")
                    return render(request, "login/login.html")
                
                elif not not_unq_username and password_su == password_2_su:
                    user = User_Login.objects.create_user(username=username_su, password=password_su) 
                    user.save()
                    login(request, user)
                    return redirect("home")
        
    return render(request, 'login/login.html')
