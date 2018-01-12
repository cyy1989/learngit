

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Countrys(models.Model):
    country_name=models.CharField(u'国家',max_length=20,unique=True)

    def __str__(self):
        return self.country_name

class Styles(models.Model):
    style=models.CharField(u'电影类型',max_length=15,unique=True,)

    def __str__(self):
        return self.style


class Actors(models.Model):
    actors=models.CharField(u'演员',max_length=50,unique=True)

    def __str__(self):
        return self.actors


class Comments(models.Model):
    comment_date=models.DateTimeField(u'评论时间',auto_now_add=True,editable=True)
    comment_content=models.TextField(u'评论内容',max_length=400)
    comment_movie=models.ForeignKey('Movies',related_name='comments_movies',null=True,on_delete=models.SET_NULL)
    comment_user=models.ForeignKey(User,related_name='comment_users',null=True,on_delete=models.SET_NULL)

    class Meta:
        ordering=('comment_date',)

class Movies(models.Model):
    title=models.CharField(u'标题',max_length=20)
    image=models.ImageField(u'封面',upload_to='static/images/')
    director=models.CharField(u'导演',max_length=20)
    actors=models.ManyToManyField(Actors,related_name='movies_actors')
    pub_date=models.DateField(u'上映时间')
    country=models.ManyToManyField(Countrys,related_name='movies_country')
    hits=models.IntegerField(u'点击数',default=0)
    style=models.ManyToManyField(Styles,related_name='movies_style')
    movie_comment=models.ManyToManyField(Comments,related_name='movies_comment')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('hits',)









