from django.contrib import admin
from django.urls import path
from django_summernote import urls as django_summernote_urls
from django.urls import path, include
from trendtalk.views import post_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include(django_summernote_urls)),
    path('', post_list, name='post_list'),
]
