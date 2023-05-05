from django.shortcuts import render


def register(request):
    if request.method == 'POST':
        print(request.POST['first_name'])

    return render(request, 'accounts/register.html')

def login(request):
    pass


def logout(request):
    pass