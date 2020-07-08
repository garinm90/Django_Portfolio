from django.shortcuts import render
from pprint import pprint
from blog.models import Post


def index(request):
    recent_post = Post.objects.order_by('-created_on')[:3]
    return render(request, 'pages/index.html', context={"recent_post": recent_post})
