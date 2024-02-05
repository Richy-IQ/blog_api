from django.contrib import admin


from .models import Posters, Comment, Category

admin.site.register(Posters)
admin.site.register(Comment)
admin.site.register(Category)

