"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include,path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<int:id>/post_edit', views.post_edit, name='post_edit'),
    path('<int:id>/post_delete', views.post_delete, name='post_delete'),
    path('', views.post_list, name='post_list'),
    path('<int:id>/<slug>/', views.post_detail, name='post_detail'),
    path('post_create/', views.post_create, name='post_create'),

    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('register/', views.register, name='register'),
    path('edit_profile/',views.edit_profile, name='edit_profile'),
    path('oauth/', include('social_django.urls', namespace="social")),
    path('like/', views.like_post, name='like_post'),
] 

if settings.DEBUG:
    urlpatterns == static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)