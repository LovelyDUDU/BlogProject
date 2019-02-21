from django.contrib import admin
from django.urls import path, include
import Blogapp.views
from django.conf import settings
from django.conf.urls.static import static
 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Blogapp.views.main, name="main"),
    path('home/', Blogapp.views.home, name="home"),
    path('portfolio/',Blogapp.views.portfolio, name="portfolio"),
    path('blog/', include('Blogapp.urls')),
    path('account/',include('accountapp.urls')),
    # path('blog/<int:blog_id>', Blogapp.views.detail, name="detail"),

    # url을 blog/정수형 으로 설계할껀데 detail함수에는 blog_id 라고 하는 변수로써 인자를 전달해주ㄹ어라. <> 이거는 path converter
    # blog_id는 detail함수에게 넘기는 인자임. detail함수는 request 이외에 추가적인 정보가 필요함(몇번 객체를 다룰것인지에 대한 정보) => 인자가 request, blog_id 두개가 필요함

    # path('blog/create/', Blogapp.views.create, name="create"),
    # path('blog/write/',Blogapp.views.write, name="write"),
    # path('blog/ad',Blogapp.views.ad, name="ad"),
    
    # path('blog/rewrite/<int:blog_id>', Blogapp.views.rewrite, name="rewrite"),
    # path('blog/recreate/<int:blog_id>', Blogapp.views.recreate, name="recreate"),
    # path('blog/delete/<int:blog_id>', Blogapp.views.delete, name="delete"),
    #path -> (어떤 url이 들어오면 , 어디에있는 어떤 함수를 실행시켜라)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
