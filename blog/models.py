from django.db import models
from django.utils import timezone
# Create your models here.


#models.Model Post가 장고모델임을 의미함
#Post가 데이터베이스에 저장되어야 한다고 말하는 것과 같음
class Post(models.Model):
    author=models.ForeignKey('auth.User')
    title=models.CharField(max_length=200)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date=timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

# CharField : 글자수가 제한된 텍스트 정의
# TextFiled : 글자수의 제한을 따로 두지 않는 텍스트
# DeateTimeField : 날짜와 시간 필드
# ForeignKey : 다른 모델에 대한 링크(외래키)