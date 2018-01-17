
# Create your views here.
import re


# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets,filters
from rest_framework.response import Response

from DouBan.models import Movies, Actors, Styles, Countrys, Comments, User

from DouBan.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from serializers import MoviesSerializers, ActorsSerializers, StylesSerializers, CountrysSerializers, \
    CommentsSerializers, UserSerializers


class MoviesViewSet(viewsets.ModelViewSet):

    queryset=Movies.objects.all()
    serializer_class = MoviesSerializers

    filter_backends = (DjangoFilterBackend,filters.SearchFilter)
    search_fields=['director','hits','title','style__style','movie_actors__actors']#设置搜索栏范围，如果有外键，要注明外键的哪个字段，双下划线
    filter_fields = ('movie_actors', 'style','director','hits',)
    permission_classes = (IsAdminOrReadOnly,)



    def retrieve(self, request,*args, **kwargs):
        instance = self.get_object()
        instance.hits += 1
        print(instance.hits)
        instance.save()
        serializer = self.get_serializer(instance)

        return Response(serializer.data)


class ActorsViewSet(viewsets.ModelViewSet):
    queryset=Actors.objects.all()
    serializer_class = ActorsSerializers



class StylesViewSet(viewsets.ModelViewSet):
    queryset=Styles.objects.all()
    serializer_class =StylesSerializers

class CountrysViewSet(viewsets.ModelViewSet):
    queryset=Countrys.objects.all()
    serializer_class = CountrysSerializers

class CommentsViewSet(viewsets.ModelViewSet):
    queryset=Comments.objects.all()
    serializer_class =CommentsSerializers
    filter_backends = (DjangoFilterBackend,)
    permission_classes = (IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(comment_user=self.request.user)

    def list(self, request, *args, **kwargs):
        a = int(re.sub("\D", "", request.path))#获取路径中电影资源id
        queryset = self.filter_queryset(self.get_queryset().filter(comment_movie=a))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # def retrieve(self, request, *args, **kwargs):
    #     a = int(re.sub("\D", "", request.path))
    #     instance = self.get_object().filter(comment_movie=a)
    #
    #     print(instance.comment_movie)
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)


class UsersViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class = UserSerializers


