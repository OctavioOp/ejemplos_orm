from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('create',views.add),
    path('delete/<num>',views.delete),
    path('edit/<num>', views.edit),
    path('home/',views.index2),
    path('create2',views.add2),
]
