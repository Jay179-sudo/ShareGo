from django.shortcuts import render, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import Post
# Create your views here.
def home(request):
    return render(request, 'main.html')

from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from .forms import ArticleForm

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            candidate = form.save(commit=False)
            candidate.author = request.user
            candidate.save()

            return HttpResponseRedirect('/post')
    else:
        form = ArticleForm()
    return render(request, 'post/upload.html', {'form': form})

@login_required
def content(request):
    authors = get_user_model().objects.all().order_by('username')
    return render(request, 'post/content.html', {'authors': authors})

@login_required
def detailcontent(request, username):

    # author = User.objects.all().filter(username=username)
    # post = Post.objects.all().filter(author=author)
    author = User.objects.get(username=username)
    post = Post.objects.all().filter(author=author)
    return render(request, 'post/detail.html', {'author': post})