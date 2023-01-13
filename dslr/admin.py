from django.contrib import admin
from dslr.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
