from django.urls import path
from . import views

urlpatterns = [
    path('', views.PageIndex.as_view(), name="index"),
    path('add/', views.PageAdd.as_view(), name="add"),
    path('<slug>/', views.PageDetail.as_view(), name="detail"),
]
