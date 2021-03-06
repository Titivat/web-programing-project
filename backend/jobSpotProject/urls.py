"""jobSpotProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login/', user_login, name="user_login"),
    # path('success/', success, name="user_success"),
    # path('logout/', user_logout, name="user_logout"),

    path('api/v1/', include('users.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),


    path('api/', include('users.urls')),
    path('api/forum/', include('forums.urls')),
    path('api/position/', include('positions.urls')),
    path('api/post/', include('posts.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
