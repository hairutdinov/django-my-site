from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post
from .forms import CommentForm


class StartingPageView(ListView):
    template_name = 'blog/index.html'
    model = Post
    ordering = ['-date']
    context_object_name = 'posts'  # by default: object_list

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query[:3]
        return data


class PostsView(ListView):
    template_name = 'blog/posts.html'
    model = Post
    context_object_name = 'posts'


class PostDetailPage(DetailView):
    template_name = 'blog/post-detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_post = self.object
        request = self.request
        context['tags'] = loaded_post.tags.all()
        context['comment_form'] = CommentForm()
        return context
