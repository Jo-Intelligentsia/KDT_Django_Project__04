from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import PostForm, CommentForm


# Create your views here.
def index(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts,
    }
    return render(request, 'posts/index.html',context)

def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comments = post.comment_set.all()
    comments_form = CommentForm()
    context = {
        'post' : post,
        'comments' : comments,
        'comments_form' : comments_form,
    }
    return render(request, 'posts/detail.html',context)

@login_required
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # 게시글 작성자 정보 추가
            post.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)

def comment_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()
    return redirect('posts:detail',post.pk)

def comment_delete(request,post_pk,comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('posts:detail', post_pk)


def post_option(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        option = request.POST.get('option')
        if option == 'select1_content':
            if request.user not in post.select1_content.all():
                post.select1_content.add(request.user)
        elif option == 'select2_content':
            if request.user not in post.select2_content.all():
                post.select2_content.add(request.user)
    return redirect('posts:detail', post_pk=post_pk)