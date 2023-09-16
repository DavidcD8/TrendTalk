from django.contrib import admin
from django.urls import path, include
from trendtalk import views
from django.urls import path
from trendtalk.views import profile
from trendtalk import views
from trendtalk.views import PostListView, PostDetailView, profile
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', views.PostListView.as_view(), name='home'),
    path("accounts/", include("allauth.urls")),
    path('accounts/profile/', profile, name='account_profile'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('', PostListView.as_view(), name='post_list'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('post/<slug:slug>/like/', views.post_like, name='post_like'),
    path('comment/<int:comment_id>/edit/',
         views.edit_comment, name='edit_comment'),
    path('comment/delete/<int:comment_id>/',
         views.delete_comment, name='delete_comment'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
