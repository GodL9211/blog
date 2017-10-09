from django.contrib import admin
from .models import Post, Category, Tag

class PostAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['title',  'author']
    list_filter = ['author']
    search_fields = ['author', 'tags']
admin.site.register(Post, PostAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_filter = ['name']
    list_per_page = 15
    list_display = ['name']
    search_fields = ['name']
admin.site.register(Category, CategoryAdmin)

class TagAdmin(admin.ModelAdmin):
    list_filter = ['name']
    list_per_page = 15
    list_display = ['name']
    search_fields = ['name']
admin.site.register(Tag, TagAdmin)