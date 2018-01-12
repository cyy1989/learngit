from django.contrib import admin



# Register your models here.
from DouBan.models import Movies, Comments, Actors, Styles, Countrys

admin.site.register(Movies)
admin.site.register(Actors)
admin.site.register(Comments)
admin.site.register(Styles)
admin.site.register(Countrys)