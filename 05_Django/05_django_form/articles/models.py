from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # 객체 표시 형식 수정
    def __str__(self):
        return f'[{self.pk}] {self.title}'

class Comment(models.Model):
    # related_name : 부모 테이블에서 역으로 참조할 때 기본적으로 모델이름_set 형식으로 불러온다. related_name 이라는 값을 설정해서 _set 명령어를 임의로 변경할 수 있다.
    # Comment -> 이중 1:N 관계 (Article, User)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Model Level에서 Metadata 설정
    class Meta:
        ordering = ['-pk',]

    def __str__(self):
        return self.content