# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'blog/post/signup.html', {'form': form})

def post_list_view(request):
    list_objects = Post.published.all()
    paginator = Paginator(list_objects, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail_view(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})

def new_post(request):
    template = 'blog/post/new_post.html'
    form = PostForm(request.POST or None)

    try:
        if form.is_valid():
            post = form.save()
            post.slug = slugify(post.title)
            post.save()
            messages.success(request, 'Your Blog Post Was Successfully Saved')
        else:
            form = PostForm()

    except Exception as e:
        messages.warning(request, "Blog Post Failed To Save. Error: {}".format(e))

    context = {
        'form': form,
    }

    return render(request, template, context)

def home(request):
	return render(request,'blog/post/home.html')
# Create your views here.
