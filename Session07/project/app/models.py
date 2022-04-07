from django.db import models

# Create your models here.
class Post(models.Model):
    #Field 어떤 데이터를 저장할 것이냐. 
    # 검색해서 입력 
    # 문자를 입력받는 것 CharField input
    # 길이 제한이 있음, 
    # 문자를 입력받는 것 TextField textarea
    # 
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
        #객체를 저장해주는 함수, 
        # 어떤 내용을 저장해줄거냐. 
        # object 1, 2, 3 로 보여주지 않고, 
        # title로 해주는 것이 좋다. 

