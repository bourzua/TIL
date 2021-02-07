from django.urls import path
from . import views

urlpatterns = [
    path('', views.community_list_create),
    path('<int:pk>/', views.detail),
    path('<int:pk>/delete_update/', views.delete_update),
    path('<int:pk>/comments/', views.comments_create),
    path('<int:pk>/comments/get/', views.getComments),
    path('comments/<int:comment_id>/delete/', views.comment_delete),
    path('<str:username>/getusercommunities/', views.get_userCommunities),
    path('<str:username>/getusercomments/', views.get_userComments),
]
