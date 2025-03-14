from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Post
from django.views.generic import ListView
from django.views.decorators.http import require_POST
from .forms import CommentForm

# Create your views here.
class PostListView(ListView):
    """
    Alternatives post list view
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'blog/post/list.html'


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
    comments = post.comments.all()
    form = CommentForm()

    return render(request, "blog/post/detail.html", {"post": post, "comments":comments, "form": form})


def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
    if form.is_valid():
        # Form fields passed validation
        cd = form.cleaned_data
        # ... send email
    else:
        form = EmailPostForm()
    return render(request,'blog/post/share.html', { 'post': post,'form': form })
    

@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISH)
    comment = None
    # A comment was posted
    form = CommentForm(data=request.POST)
    if form.is_valid():
        # Create a Comment object without saving it to the data
        comment = form.save(commit=False)
        # Assign the post to the comment
        comment.post = post
        # Save the comment to the database
        comment.save()
    return render(request, 'blog/post/comment.html',{'post': post, 'form': form, 'comment': comment})
