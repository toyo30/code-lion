from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    cate = models.CharField(max_length=10)

    #article 모델로 출력할 일이 있을 때, 출력 값을 타이틀로하겠다. 
    def __str__(self):
        return self.title

# 사람 테이블을 만듬 
# 가로 안에 넣는 값은 클래스다.
# 이 클래스의 특성을 상속한다. 
# models.Model의 클래스를 물려받는다. 

class Person(models.Model):
    name = models.CharField(max_length=10)
    address =models.TextField()


# Article.objects.create(title = "좋은날", content = "눈물이 차 올라서 고갤 들어")

# Article.objects.all()

#Article.objects.get(pk = 3)

# name 케릭터 필드 


# address 텍스트 필드