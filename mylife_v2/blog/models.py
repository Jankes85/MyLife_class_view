from django.db import models

# Create your models here.
from django.forms import DateInput


class Blog(models.Model):
    title = models.CharField(max_length=200, blank=False)
    note = models.TextField()
    entry_date = models.DateField(auto_now=False, blank=False, )
    category = models.CharField(max_length=1, choices=(("p", "programming"), ("i", "interests"), ("l", "life")),
                                blank=False)
    author = models.CharField(max_length=30, blank=False)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blog"
