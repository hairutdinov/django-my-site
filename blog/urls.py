from django.urls import path
from . import views


urlpatterns = [
    path('', views.StartingPageView.as_view(), name='starting-page'),
    path('posts', views.PostsView.as_view(), name='posts'),
    path('posts/<slug:slug>', views.post_detail, name='post-detail'),
]
