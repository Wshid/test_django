from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})
# Create your views here.

# render : 넘겨진 요청과 blog/post_list.html 템플릿 받아 리턴된 내용이 브라우저에 보여짐
