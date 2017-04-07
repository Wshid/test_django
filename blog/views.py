from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})
        # { }의 내용은 템플릿을 사용하기위해 데이터 추가하는 것
# Create your views here.

def post_detail(request, pk):
    post=get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

# render : 넘겨진 요청과 blog/post_list.html 템플릿 받아 리턴된 내용이 브라우저에 보여짐
