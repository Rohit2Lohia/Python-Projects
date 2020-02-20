from django.db import models

# Create your models here.
#Model rep by class
class Article(models.Model):
    """docstring for Article."""
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add thumbnail later
    # add its autor later
    def __str__(self):
        return self.title
