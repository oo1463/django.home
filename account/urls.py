"""LogIn URL Configuration

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
from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('signin/', views.SignIn.as_view(), name='signin'),
    path('signout/', views.signOut, name='signout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('mypage/', views.MyPage.as_view(), name='mypage'),
    path('msg/', views.Msg.as_view(), name='msg'),
    path('sendmsg/', views.SendMsg.as_view(), name='sendmsg'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
]
