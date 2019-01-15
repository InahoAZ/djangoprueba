from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coso/', views.coso, name='coso'),
    path('coso/<int:pk>', views.post_detail, name='post_detail'),

]
