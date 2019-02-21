from django.shortcuts import render
from .models import Blog
from .models import Portfolio
from django.shortcuts import render, get_object_or_404, redirect
#redirect-> 함수들을 다 처리한뒤 ~URL로 이동하세요(넘기세요)
from django.utils import timezone #현재시간 사용을 위해
from django.core.paginator import Paginator #장고의 core.paginator에서 임포트해옴

def main(request):
    return render(request,'main.html')

def home(request):
    blogs=Blog.objects
    blog_list= Blog.objects.all() #블로그의 모든 것들을 가져와서 리스트에 담음
    paginator = Paginator(blog_list, 3) #객체 3개를 한페이지로 잘라냄
    #request 된 페이지가 뭔지를 알아내고, request페이지를 변수에 담아내고
    page = request.GET.get('page') #page라는 변수에 request중 GET으로 받아낸거중 키값이 page인 value값을 담아주겠다?
    #request 된 페이지를 얻어온 뒤 return 해줌
    posts=paginator.get_page(page) #해당 페이지번호에 해당하는 페이지가 넘어옴
    return render(request,'home.html', {'blogs':blogs, 'posts':posts})

def detail(request,blog_id):
    blog_detail=get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html', {'blog':blog_detail})
#pk= primary key의 약자. 클래스에 지정해주지않아도 장고는 항상 pk에 대한 속성을 not null 및 autoincrement로, 이름은 id로 해서 자동으로 만들어줌. 
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
    #return redirect('/blog/' + str(blog.id)) #str은 형변환. blog.id는 숫자라서 문자로 형변환
    #redirect 함수는 안에 다른 url을 넣을수있음. 
    #render은 세번째로 키값을 받음. 데이터를 담아서 처리할때사용?

def ad(request):
    return redirect('http://yeungnam.likelion.org/')

def rewrite(request,blog_id):
    blog_detail=get_object_or_404(Blog,pk=blog_id)
    return render(request,'rewrite.html',{'blog':blog_detail})

def recreate(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.save()
    return redirect('/blog/' +str(blog.id))

def delete(request,blog_id):
    blog=get_object_or_404(Blog,pk=blog_id)
    blog.delete()
    return redirect('/home/')