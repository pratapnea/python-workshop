from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect
# Create your views here.

from .models import Post

def post_list(request):
	posts = Post.objects.all()
	return render(request, 'list.html', {'posts':posts})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.created = timezone.now()
			post.save()
			return redirect('post_list')
	else:
		form = PostForm()
		return render(request,'new_post.html', {'form':form})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk = pk)
	return render(request, 'post_details.html', {'post': post})