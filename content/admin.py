from django.contrib import admin

from content.models import Blog, BlogPost


class BlogAdmin(admin.ModelAdmin):
    list_display = ['owner', 'title']


admin.site.register(Blog, BlogAdmin)


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['blog', 'title', 'is_published']


admin.site.register(BlogPost, BlogPostAdmin)