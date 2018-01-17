

from rest_framework import serializers

from DouBan.models import Movies, Actors, Comments, Countrys, Styles, User


class MoviesSerializers(serializers.ModelSerializer):
    # movie_comment=serializers.PrimaryKeyRelatedField(many=True,queryset=Comments.objects.all())
    class Meta:
        model=Movies
        fields=('title','image','director','movie_actors','pub_date','country','hits','style','comments')
        depth = 1



class ActorsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Actors
        fields=('actors',)

class UserSerializers(serializers.ModelSerializer):
    # mobile_num=serializers.IntegerField()
    # username=serializers.PrimaryKeyRelatedField(many=True,queryset=Comments.objects.all())

    class Meta:
        model=User

        fields = ('mobile',)

class CommentsSerializers(serializers.ModelSerializer):
    comment_movie = MoviesSerializers()
    comment_user = UserSerializers()
    class Meta:
        model=Comments

        fields=('comment_date','comment_content','comment_movie','comment_user',)#访问时默认显示外键id ，创建时传id
        #comment_user=serializers.ReadOnlyField(source='Comments')
        #fields = '__all__'# 访问时显示外键字段的所有信息，但是只读的，不可编辑，即新建时不能传值
        #depth = 1




class CountrysSerializers(serializers.ModelSerializer):
    class Meta:
        model = Countrys
        fields = ('country_name',)


class StylesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Styles
        fields = ('style',)

# class authuserSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = 'auth.user'
#         fields = ('username','password','email')

        # depth = 1