from django.contrib import admin

from .models import *

class ImageInLineAdmin(admin.TabularInline):
    model = Image
    fields = ('image', )
    max_num = 4

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [ImageInLineAdmin, ]

admin.site.register(Category)


