from django.contrib import admin
from .models import Blog #같은 폴더 안의 models에 Blog를 가져오셈
# Register your models here.
admin.site.register(Blog) #admin사이트에 등록해라


from .models import Portfolio
admin.site.register(Portfolio)