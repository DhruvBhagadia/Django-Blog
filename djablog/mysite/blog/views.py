# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from .forms import PostForm

from django.contrib import messages

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

'''def main_page(request):
    template = get_template('blog/post/main_page.html')
    variables = Context({ 'user': request.user })
    output = template.render(variables)
    return HttpResponse(output)

def edit_post(request,pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        try:
            if form.is_valid():
                form.save()
                messages.success(request, "Your Blog Post Was Successfully Updated")

        except Exception as e:
            messages.warning(request, 'Your Post Was Not Saved Due To An Error: {}'.format(e))

    else:
        form = PostForm(instance=post)
    return render(request,'blog/post/new_post.html',{'form':form,'post':post})'''


def home(request):
	return render(request,'blog/post/home.html')

def new_post(request):
    template = 'blog/post/new_post.html'
    form = PostForm(request.POST or None)

    try:
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Blog Post Was Successfully Saved')
        else:
            form = PostForm()

    except Exception as e:
        messages.warning(request, "Blog Post Failed To Save. Error: {}".format(e))

    context = {
        'form': form,
    }

    return render(request, template, context)

# Create your views here.
