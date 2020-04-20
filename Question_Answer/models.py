from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    title       = models.CharField(max_length=150, unique=True)
    slug        = models.SlugField(max_length=150, unique=True, editable=False)
    description = models.CharField(max_length=300)
    pub_date    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"


class Question(models.Model):
    category       = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='questions')
    owner          = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions')
    question_title = models.CharField(max_length=150, unique=True)
    question_text  = models.TextField(max_length=50000, blank=False, unique=True)
    slug           = models.SlugField(max_length=150, unique=True, editable=False)
    pub_date       = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.question_title

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    class Meta:
        get_latest_by = "-pk"
        ordering = ['-pub_date']


class Answer(models.Model):
    user          = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='replies')
    question      = models.ForeignKey(Question, on_delete=models.CASCADE)
    pub_date      = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
    	return self.question

    class Meta:
    	ordering = ['-pub_date']