"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from myapp.views import CreateUserView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView # prebuilt views to obtain access+refresh tokens

urlpatterns = [
    path("admin/", admin.site.urls),
    # additions
    # urls we can go to that will call a function/perform an operation
    path("api/user/register/", CreateUserView.as_view(), name="register"), # allows to make new user, can name whatever we want
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"), # gets our token (already made, just have to link)
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"), # refreshes token
    path("api-auth/", include("rest_framework.urls")), # includes all urls from restframework urls
]
