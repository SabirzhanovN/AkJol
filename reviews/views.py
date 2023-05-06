from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from pages.models import Public
from reviews.models import Review


def create(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        public_id = request.POST['public_id']

        review = request.POST['commit']

        user = User.objects.get(id=user_id)
        public = Public.objects.get(id=public_id)

        new_review = Review.objects.create(
            user=user,
            public=public,
            review=review
        )

        new_review.save()
        return redirect('detail', public_id)