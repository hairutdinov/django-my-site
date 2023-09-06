from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse

# Create your views here.


def starting_page(request):
    return render(request, 'blog/index.html')


def posts(request):
    pass


def post_detail(request):
    pass
