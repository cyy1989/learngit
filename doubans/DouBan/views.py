from django.contrib import auth
from django.contrib.auth.models import User

from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import detail_route, api_view
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

# from django_filters.rest_framework import DjangoFilterBackend

from DouBan.models import Movies,Actors, Styles, Countrys, Comments

from DouBan.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from DouBan.serializers import MoviesSerializers, ActorsSerializers, StylesSerializers, CountrysSerializers, \
    CommentsSerializers, UserSerializers


class MoviesViewSet(viewsets.ModelViewSet):

    queryset=Movies.objects.all()
    serializer_class = MoviesSerializers
    # parser_classes = (JSONParser,)
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('actors', 'style','director')
    # permission_classes = (IsAdminOrReadOnly,)


    # def add_hits(self,request,args, **kwargs):
    #     obj = self.get_object()
    #     obj.hits += 1
    #     serializer = self.get_serializer(obj, data=request.data)
    #     print(serializer.data)
    #     return Response(serializer.data)
    #@api_view(http_method_names=['GET'])
    def retrieve(self, request,*args, **kwargs):
        instance = self.get_object()
        instance.hits += 2
        print(instance.hits)
        instance.save()
        serializer = self.get_serializer(instance)

        return Response(serializer.data)
    #@api_view(http_method_names=['GET'])
    # def retDouBan.views.MoviesViewSet#retrieverieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.hits += 1
    #     print(instance.hits)
    #     instance.sava()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)

# class MoviesUpdate(GenericAPIView):
#     @api_view
#     def add_hits(self,request):
#         obj=self.get_object()
#         obj.hits += 1
#         serializer = self.get_serializer(obj, data=request.data)
#
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         # obj.hits += 1
#         obj.save()
#         return obj
#         return Response(MoviesSerializers(serializer.instance).data)


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
    filter_fields = ('comment_movie',)
    # permission_classes = (IsOwnerOrReadOnly,)
# class UsersViewSet(viewsets.ModelViewSet):
#     queryset=User.objects.all()
#     serializer_class = UserSerializers

# class authuserViewSet(viewsets.ModelViewSet):
#     queryset=auth_user.objects.all()
#     serializer_class =authuserSerializers
#'
