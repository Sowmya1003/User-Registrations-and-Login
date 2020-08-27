"""register URL Configuration

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
from django.urls import path,include
from registration.views import registration, home_view, login_page,welcome_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', registration, name='register_page'), # path which u have added here is the url for ur view
    path('home/', home_view, name="home_page"), # by using name i don't need to change everywhere with i have using navigation <a> tag
    path('login/', login_page, name="login_page"),
    path('welcome/', welcome_page, name="welcome_page")

]
