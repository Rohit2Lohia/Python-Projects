from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Model rep by class
class Article(models.Model):
    """docstring for Article."""
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thum = models.ImageField(default='default.jpg', blank=True)
    # add its autor later
    author = models.ForeignKey(User,default=None,on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]+'.....'

# class Headline(models.Model):
# 	title = models.CharField(max_length=200)
# 	image = models.URLField(null=True, blank=True)
# 	url = models.TextField()
#
# 	def __str__(self):
# 		return self.title
