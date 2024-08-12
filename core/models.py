from django.db import models
from django.utils.text import slugify

from base import BaseModel
from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.


class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    category_pic = models.ImageField(upload_to='category', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.category_name


class BlogPost(BaseModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    title = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blog_posts', null=True, blank=True)
    content = models.TextField()
    cover_pic = models.ImageField(upload_to='blog_posts/cover_pics', blank=True, null=True)
    tags = TaggableManager()
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(BlogPost, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
