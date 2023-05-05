from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    return redirect('register')
                else:
                    new_user = User.objects.create(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=email,
                        password=password1
                    )

                    new_user.save()

                    return redirect('login')
        else:
            return redirect('register')

    return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(username, password)

        user = auth.authenticate(
            username=username,
            password=password
        )
        print(user)
        if user:
            auth.login(request, user)
            return redirect('create')
        else:
            return redirect('login')

    return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('register')