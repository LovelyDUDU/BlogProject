from django.contrib import admin
from django.urls import path
import Blogapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Blogapp.views.main, name="main"),
    path('home/', Blogapp.views.home, name="home"),
    path('blog/<int:blog_id>', Blogapp.views.detail, name="detail"),
    path('portfolio/',Blogapp.views.portfolio, name="portfolio"),
    path('blog/create/', Blogapp.views.create, name="create"),
    path('blog/write/',Blogapp.views.write,name="write"),
    path('blog/ad',Blogapp.views.ad, name="ad"),
    #path -> (어떤 url이 들어오면 , 어디에있는 어떤 함수를 실행시켜라)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
