

# Create your m
# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

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
    comment_user=models.ForeignKey('User',related_name='comment_users',null=True,on_delete=models.SET_NULL)

    class Meta:
        ordering=('-comment_date',)

class Movies(models.Model):
    title=models.CharField(u'标题',max_length=20)
    image=models.ImageField(u'封面',upload_to='static/images/')
    director=models.CharField(u'导演',max_length=20)
    movie_actors=models.ManyToManyField(Actors,related_name='movies_actors')
    pub_date=models.DateField(u'上映时间')
    country=models.ManyToManyField(Countrys,related_name='movies_country')
    hits=models.IntegerField(u'点击数',default=0)
    style=models.ManyToManyField(Styles,related_name='movies_style')
    comments=models.URLField(null=True)
    # movie_comment=models.ManyToManyField(Comments,related_name='movies_comment',blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('hits',)





# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager):

    def create_user(self, mobile, email, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            mobile=mobile,
            email=UserManager.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, mobile, email, password=None):

        user = self.create_user(mobile, email, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    '''用户表'''

    mobile = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    avatar = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_delete = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    access_token = models.CharField(max_length=100, blank=True)
    refresh_token = models.CharField(max_length=100, blank=True)
    expires_in = models.BigIntegerField(default=0)

    objects = UserManager()

    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = ('email',)

    class Meta:
        ordering = ('-created_at',)

    def __unicode__(self):
        return self.mobile

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.mobile

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_superuser