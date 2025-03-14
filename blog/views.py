from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    try:
        posts = paginator.page(page_number)     
    except PageNotAnInteger:
        # If page_number is not an integer get the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range get last page of resul
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(
        Post, status=Post.Status.PUBLISH, publish__year=year, publish__month=month, publish__day =day, slug=post
        )
    return render(request, "blog/post/detail.html", {"post": post})
