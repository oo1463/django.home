from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
    path('<str:whatboard>/', views.board, name='board'),

    path('<str:whatboard>/posting/', views.writingpost, name='writingpost'),

    path('<str:whatboard>/<int:pk>/', views.postdetail, name='postdetail'),

    path('<str:whatboard>/<int:pk>/recommend', views.recommend, name='recommend'),
    path('<str:whatboard>/<int:pk>/unrecommend', views.unrecommend, name='unrecommend'),

    path('<str:whatboard>/<int:pk>/del', views.deletepost, name='deletepost'),

    path('<str:whatboard>/<int:pk>/comment/<int:commentnumber>', views.deletecomment, name='deletecomment'),
    path('<str:whatboard>/<int:pk>/edit/', views.edit, name='edit'),
]
