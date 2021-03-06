from django.db import models

# Create your models here.
class Blog(models.Model): #Blog 라는 클래스 선언
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def sumtitle(self):
        return self.title[:5]

    def summary(self):
        return self.body[:10]


class Portfolio(models.Model):
    title=models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description=models.CharField(max_length=500)

    def __str__(self):
        return self.title