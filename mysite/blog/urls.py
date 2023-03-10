from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    ## Create a path to link to post by its pk, use the post_detail view, name it post_detail
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    ## Create a path to create a new post
    path('post/new/', views.post_new, name='post_new'),
    ## Create a path to update an existing post
    path('post/<int:pk>/edit', views.post_edit, name='post_edit')
]