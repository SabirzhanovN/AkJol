from django.shortcuts import render


def create(request):
    return render(request, 'pages/create.html')
