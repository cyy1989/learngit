"""doubans URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin

from django.conf.urls import url
from django.urls import path,include
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from DouBan import views
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

#admin.autodiscover()
router=DefaultRouter()
router.register(r'movies',views.MoviesViewSet,'movies')
router.register(r'actors',views.ActorsViewSet,'actors')
router.register(r'countrys',views.CountrysViewSet,'countrys')
router.register(r'style',views.StylesViewSet,'style')
router.register(r'comments',views.CommentsViewSet,'comments')
# router.register(r'users',views.UsersViewSet,'users')
urlpatterns = [
    path(r'admin/',admin.site.urls),
    url(r'^', include(router.urls)),
    # url(r'^api-token-auth/', obtain_jwt_token),
    # url(r'^api-token-refresh/', refresh_jwt_token),
    # url(r'^api-token-verify/', verify_jwt_token),
]

