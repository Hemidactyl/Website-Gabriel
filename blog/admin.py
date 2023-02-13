from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category', 'language', 'status', 'created_on')
    list_filter = ('category', 'language', 'status')
    search_filter = ['title', 'content']
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Post, PostAdmin)
