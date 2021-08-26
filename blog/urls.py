from django.urls import path

from . import views


app_name = "blog"
urlpatterns = [
    path('', views.accueil_blog, name='accueil'),
    path('<int:cle_primaire>/', views.article, name='article'),
]
