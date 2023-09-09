from django.contrib import admin
from .models import Post, Tag, Author, Comments


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Comments)
