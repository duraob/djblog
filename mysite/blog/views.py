from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm

# Create your views here.
def post_list(request):
    ## All Posts published prior to now, sorted by desc
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    ## From the request get the pk & search for that obj in posts table, return dtls render view
    ## if obj doesnt exist return the 404 page
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post' : post})

def post_new(request):
    ## Take details from the user's blog post form and create a new record in Posts table
    if request.method == 'POST':
        ## After we submit form, we want to see the data we just put in instead of a blank form
        form = PostForm(request.POST)
        ## Check to see if form is valid with correct data before submitting it to DB
        if form.isvalid():
            post = form.save(commit=False) ## dont save model immediately
            post.author = request.user
            post.published_date = timezone.now()
            post.save() ## preserve cahnges and create a new blog post
            return redirect('post_detail', pk=post.pk) ## return the user to the post they just created
    else:
        ## Creating a new blog post, so give a blank form
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})