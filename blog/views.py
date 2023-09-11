from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post


class StartingPageView(ListView):
    template_name = 'blog/index.html'
    model = Post
    context_object_name = 'posts'  # by default: object_list

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.order_by('-date')[:3]
        return data


def posts(request):
    return render(request, 'blog/posts.html', {
        'posts': Post.objects.all(),
    })


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post-detail.html', {
        'post': post,
        'tags': post.tags.all()
    })
