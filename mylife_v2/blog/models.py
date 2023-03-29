from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    note = models.TextField()
    entry_date = models.DateField(auto_now=False)
    category = models.CharField(max_length=1, choices=(("p", "programming"), ("i", "interests"), ("l", "life")))
    author = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blog"

