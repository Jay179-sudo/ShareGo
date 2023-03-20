from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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