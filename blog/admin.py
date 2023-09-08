from django.contrib import admin

# Register your models here.
from .models import Post, Author, Tag


class PostAdmin(admin.ModelAdmin):
    # readonly_fields = ('slug',)
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('author', 'date', 'tags')
    list_display = ('author', 'date', 'title')


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
