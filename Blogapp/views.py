from django.shortcuts import render
from .models import Blog
from .models import Portfolio
from django.shortcuts import render, get_object_or_404, redirect #redirect-> 함수들을 다 처리한뒤 ~URL로 이동하세요(넘기세요)
from django.utils import timezone #현재시간 사용을 위해
# Create your views here.

def main(request):
    return render(request,'main.html')

def home(request):
    blogs=Blog.objects
    return render(request,'home.html',{'blogs':blogs})


def detail(request,blog_id):
    blog_detail=get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'blog':blog_detail})

def portfolio(request):
    portfolios=Portfolio.objects
    return render(request,'portfolio.html', {'portfolios':portfolios})

def write(request): #write.html을 띄워주는 함수
    return render(request,'write.html')

def create(request): #입력받은 내용을 DB에 넣어주는 함수
    blog = Blog() #Blog 라고 하는 클래스로부터 blog의 객체를 생성
    blog.title = request.GET['title']#객체안에 title,body,pubdate를 씀. request.GET은 write.html에서 입력한거 가져옴
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now() #현재시간
    blog.save() #쿼리셋 메소드ㅇ중하나, blog라는 객체에 내용을 넣고 그거를 DB에 저장 #blog.delete()->삭제
    return redirect('/home/')
    #return redirect('/blog/' + str(blog.id)) #str으 ㄴ형변환. blog.id는 숫자라서 문자로 형변환
    #redirect 함수는 안에 다른 url을 넣을수있음. 
    #render은 세번째로 키값을 받음. 데이터를 담아서 처리할때사용?

def ad(request):
    return redirect('http://yeungnam.likelion.org/')