from django.contrib import admin
from .models import Contact
# blog/admin.py
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at', 'is_published')
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ('title', 'body', 'author')
    list_filter = ('is_published',)


admin.site.register(Contact)
