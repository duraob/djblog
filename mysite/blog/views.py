from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    ## All Posts published prior to now, sorted by desc
    posts = Post.objects.filter(published__date__lte=timezone.now().order_by('published_date'))
    return render(request, 'blog/post_list.html', {'posts':posts})