from django.shortcuts import render
from django.utils import timezone
from .models import Post, CVSection
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CVForm
from django.shortcuts import redirect

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def cv_list(request):
    cvsections = CVSection.objects.all()
    return render(request, 'blog/cv_list.html', {'cvsections': cvsections})

def cv_detail(request, pk):
    cvsection = get_object_or_404(CVSection, pk=pk)
    return render(request, 'blog/cv_detail.html', {'cvsection': cvsection})

def cv_new(request):
    if request.method == 'POST':
        form = CVForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            # return redirect('cv')
    else:
        form = CVForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def cv_edit(request, pk):
    cv = get_object_or_404(CVSection, pk=pk)
    # if request.method = 'POST':
