from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Video(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        )
    
    TYPE= (
        ('premium', 'Premium'),
        ('Free', 'Free'),
        
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='vlog_posts')
    body = models.TextField()
    videofile= models.FileField(upload_to='deploy/videos/%Y/%m/%d/', null=True, verbose_name="")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    type_vlog = models.CharField(max_length=10,choices=TYPE,default='Free')
    views= models.IntegerField(default=0)
    tags = TaggableManager()
    
    class Meta:
        ordering = ('-publish',)
    
       
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('vlog:post_detail',args=[self.publish.year,self.publish.month,self.publish.day, self.slug])

    
    objects = models.Manager()
    published = PublishedManager()
    

class Comment(models.Model):
    post = models.ForeignKey(Video,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class Meta:
        ordering = ('created',)
    def __str__(self):
        return self.body

# Create your models here.

