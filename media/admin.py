from django.contrib import admin
from .models import Album, Author, Picture, AlbumAdminForm


class PictureInline(admin.TabularInline):
    model = Picture
    fields = ('title', 'slug', 'author', 'picture')
    prepopulated_fields = {'slug':('title',)}

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    prepopulated_fields = {'slug':('title',)}
    inlines = [PictureInline]
    form = AlbumAdminForm

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'website', 'instagram')
    prepopulated_fields = {'slug':('name',)}

class PictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'album', 'author')
    prepopulated_fields = {'slug':('title',)}


# Register your models here.
admin.site.register(Album, AlbumAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Picture, PictureAdmin)
