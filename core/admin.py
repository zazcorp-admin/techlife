from django.contrib import admin
from .models import BlogPost, Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class BlogPostModelAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(BlogPost, BlogPostModelAdmin)


admin.site.register(Category)