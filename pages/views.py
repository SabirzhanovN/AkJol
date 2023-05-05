from django.contrib.auth.models import User
from django.shortcuts import render
from django.core.paginator import Paginator

from pages.models import Public, Image
from reviews.models import Review


def index(request):
    publics = Public.objects.all()

    l = []
    for i in publics:

        q_dict = {
            'id': i.id,
            'user': str(i.user_id),
            'title': i.title,
            'description': i.description,
            'created_at': i.created_at,
            'user_id': i.user_id,
            'images': Image.objects.filter(public_id=i.id),
            'review_cnt': len(Review.objects.filter(public_id=i.id))
        }

        l.append(q_dict)

    paginator = Paginator(l, 8)
    page = request.GET.get('page')
    paged_public = paginator.get_page(page)
    data = {
        'publics': paged_public
    }

    return render(request, 'pages/index.html', data)


def detail(request, id):
    queryset = Public.objects.get(id=id)
    images = Image.objects.filter(public_id=queryset)
    reviews = Review.objects.filter(public_id=queryset)

    data = {
        'public': queryset,
        'images': images,
        'user_': str(queryset.user_id),
        'reviews': reviews
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


def map(request):
    return render(request, 'pages/map.html')