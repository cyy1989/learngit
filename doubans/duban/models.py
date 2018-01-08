from django.db import models

# Create your models here.

class Countrys(models.Model):
    country_name=models.CharField(u'国家',max_length=20)

    def __str__(self):
        return self.country_name

class Styles(models.Model):
    style=models.CharField(u'电影类型',max_length=15)

    def __str__(self):
        return self.style


class Movies(models.Model):
    title=models.CharField(u'标题',max_length=20)
    image=models.ImageField(u'封面',upload_to='static/images/')
    direct=models.CharField(u'导演',max_length=20)
    actors=models.CharField(u'演员',max_length=100)
    pub_date=models.DateTimeField(u'上映时间')
    country=models.ManyToManyField(Countrys,related_name='movies_country')
    hits=models.IntegerField(u'点击数')
    style=models.ManyToManyField(Styles,related_name='movies_style')

    def __str__(self):
        return self.title
    class Meta:
        ordering=('hits',)



class User(models.Model):
    user_name=models.CharField(u'用户昵称',max_length=20)
    user_mobile_number=models.CharField(u'用户手机号',max_length=11)
    user_email=models.EmailField(u'用户邮箱')
    user_password=models.CharField(u'用户密码',max_length=10)

    def __str__(self):
        return self.user_name


class Comments(models.Model):
    comment_date=models.DateTimeField(u'评论时间',auto_now_add=True,editable=True)
    comment_content=models.TextField(u'评论内容',max_length=200)
    comment_movie=models.ForeignKey(Movies,related_name='comments_movies',null=True,on_delete=models.SET_NULL)
    comment_user=models.ForeignKey(User,related_name='comment_users',null=True,on_delete=models.SET_NULL)

    class Meta:
        ordering=('comment_date',)





