from django.contrib import admin

# Register your models here.
from duban.models import Movies, Comments, User, Styles, Countrys

admin.site.register(Movies)
admin.site.register(User)
admin.site.register(Comments)
admin.site.register(Styles)
admin.site.register(Countrys)