from django.contrib import admin
from django.urls import path, include
from trendtalk import views
from django.urls import path
from trendtalk.views import profile
from trendtalk import views
from trendtalk.views import PostListView, PostDetailView, profile


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', views.PostListView.as_view(), name='home'),
    path("accounts/", include("allauth.urls")),
    path('accounts/profile/', profile, name='account_profile'),
    path('like/<slug:slug>', views.PostLikeView.as_view(), name='post_like'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('', PostListView.as_view(), name='post_list'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),

]
