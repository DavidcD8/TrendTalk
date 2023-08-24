from django.contrib import admin
from django.urls import path
from django_summernote import urls as django_summernote_urls
from django.urls import path, include
from trendtalk.views import post_list, post_detail, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include(django_summernote_urls)),
    path('accounts/', include('allauth.urls')),
    path('accounts/profile/', profile, name='account_profile'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('', post_list, name='post_list'),
]
