"""Boardy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from MessageBoard import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_homepage, name="home"),
    path('boards', views.view_boards, name="boards"),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('creator/<str:username>', views.get_creator, name="getuser"),
    path('board/<int:board_id>', views.get_board, name="getboard"),
    path('message/<int:message_id>', views.get_message, name="getmessage"),
]
