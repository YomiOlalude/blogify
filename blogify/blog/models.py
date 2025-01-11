from account.models import User
from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=100, blank=False)
    content = models.TextField(blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True
    )
    tags = models.ManyToManyField("Tag", blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
