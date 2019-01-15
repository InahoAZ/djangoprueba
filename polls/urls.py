from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coso/', views.coso, name='coso'),
    path('coso/<int:pk>', views.post_detail, name='post_detail'),
    path('coso/new', views.post_new, name='post_new'),
    path('coso/<int:pk>/edit/', views.post_edit, name='post_edit'),

]
