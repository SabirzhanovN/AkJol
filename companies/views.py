from django.shortcuts import render
from .models import News, Company


def news(request):
    q_set = News.objects.all()

    context = {
        'data': q_set
    }
    return render(request, 'news/news.html', context)
