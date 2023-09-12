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


class PostDetailPage(View):
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get('stored_posts', [])
        return post_id in stored_posts

    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request, 'blog/post-detail.html', {
            'post': post,
            'tags': post.tags.all(),
            'comments': post.comments.all().order_by('-id'),
            'comment_form': CommentForm(),
            'is_saved_for_later': self.is_stored_post(request, post.id),
        })

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post-detail', args=[slug]))

        return render(request, 'blog/post-detail.html', {
            'post': post,
            'tags': post.tags.all(),
            'comments': post.comments.all().order_by('-id'),
            'comment_form': form,
            'is_saved_for_later': self.is_stored_post(request, post.id),
        })


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get('stored_posts', [])
        return render(request, 'blog/stored-posts.html', {
            'posts': Post.objects.filter(id__in=stored_posts).all(),
            'has_posts': len(stored_posts) > 0,
        })

    def post(self, request):
        stored_posts = request.session.get('stored_posts', [])
        post_id = int(request.POST['post_id'])

        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)

        request.session['stored_posts'] = stored_posts
        return HttpResponseRedirect('/')
