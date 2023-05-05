from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from reviews import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('review/', views.create, name='review_create'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
