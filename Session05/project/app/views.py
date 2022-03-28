from django.shortcuts import render

# Create your views here.

def hello(request):
    # hello에 연결되는 함수 hello 작성
    # request 인수, 템플릿 이름, 세번째 인수(선택적): context

    return render(request, 'hello.html')

