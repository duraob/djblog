from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    ## Create a path to link to post by its pk, use the post_detail view, name it post_detail
    path('post/<int:pk>/', views.post_detail, name='post_deatil')
]
