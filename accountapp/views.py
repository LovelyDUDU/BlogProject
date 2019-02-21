from django.shortcuts import render, redirect
from django.contrib.auth.models import User #User라는 클래스를 가져옴
from django.contrib import auth #계정에 대한 권한? 을 가져옴

# Create your views here.

def signup(request): 
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username = request.POST['username'], password=request.POST['password1'])
            #signup.html 에서 작성한 form태그에서 password에 해당하는 부분인 password1을 가져와서 사용
            auth.login(request, user)
            return redirect('home') #회원가입되면 홈화면으로 돌아감
    return render(request,'signup.html')
 
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(request, username=username, password=password) #DB에서 실제 회원가입된 명단이 맞는지 확인함.
        if user is not None: #이미 존재하는 회원이라면
            auth.login(request, user) #로그인
            return redirect('home') #홈으로 보냄
        else: #없다면-> 에러출력
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    else: #request방식이 다르거나 문제가 있으면 로그인 화면에 유지
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST': #logout이 제대로 눌렸으면
        auth.logout(request) #로그아웃
        return redirect('home')
    return render(request, 'login.html')
