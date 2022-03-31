from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def new(request):
    # POST 요청이 있을 때, 이걸 뛰워주라 
    # ajax의 경우, Post요청이 있을 때, 이걸 보여줘. 
    if request.method == 'POST':
        print(request.POST)
        # orm 이 쓰이는 붑.ㄴ 
        # title은 포스트 요청의 name을 작성해주고, 
        # content 네임의 정보를 contnet로 만들어줘라
        # create의 작업. 

        # db에 저장을 해줌
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            cate = request.POST['category'],
        )
        #글 목록페이지로 보여죽. redirect 다른 페이지로 보여주기 import redirect 해주기
        return redirect('list')

    return render(request, 'new.html')

def list(request):
    articles = Article.objects.all()
    return render(request, 'list.html', {'articles': articles})


def detail(request, article_id):
    article = Article.objects.get(id = article_id)
    return render(request, 'detail.html', {'article': article})

