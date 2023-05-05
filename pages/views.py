from django.contrib.auth.models import User
from django.shortcuts import render

from pages.models import Public, Image


def index(request):
    publics = Public.objects.all()
    images = Image.objects.all()

    data = {
        'publics': publics,
        'images': images
    }

    return render(request, 'pages/index.html', data)


def detail(request, id):
    queryset = Public.objects.get(id=id)
    images = Image.objects.filter(public_id=queryset)

    data = {
        'public': queryset,
        'images': images
    }
    return render(request, 'pages/detail.html', data)


def create(request):
    if request.method == 'POST':
        images = []
        if request.FILES:
            for img in request.FILES:
                images.append(request.FILES[img])

        title = request.POST['title']
        description = request.POST['description']
        address = request.POST['address']

        user_id = request.POST['user_id']

        new_public = Public.objects.create(
            title=title,
            description=description,
            address=address,
            user_id=User.objects.get(id=user_id)
        )
        new_public.save()

        new_public_id = new_public.id
        for img in images:
            image_for = Image.objects.create(
                image=img,
                public_id=Public.objects.get(id=new_public_id)
            )

            image_for.save()

    return render(request, 'pages/create.html')
