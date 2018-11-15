from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'mainpage/post_list.html', {'posts': posts})
def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'mainpage/post_detail.html', {'post': post})
def about(request):
	return render(request, 'mainpage/about.html', {})
def past_projects(request):
	return render(request, 'mainpage/past_projects.html', {})
def smart_home(request):
	return render(request, 'mainpage/smart_home.html', {})
def contact(request):
	return render(request, 'mainpage/contact.html', {})