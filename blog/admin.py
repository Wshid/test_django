from django.contrib import admin
from .models import Post
# Register your models here.

admin.site.register(Post)
#Post 모델을 가져옴
#관리자페이지에서 확인하려면 이와같이 클래스를 등록해야함
