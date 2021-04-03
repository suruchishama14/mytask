"""mytask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app import views as core_views,views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
    path('', core_views.category, name='category'),

    path('home/', core_views.home, name='home'),

    path('detail/', core_views.detail, name='detail'),
    path('add_data/', core_views.add_data, name='add_data'),
    path('singup/', core_views.singup, name='singup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login1/',LoginView.as_view(template_name='login.html', redirect_authenticated_user=True),
            name='login1'),
    path('logout/',LogoutView.as_view(next_page = 'category'),name='logout'),
]
