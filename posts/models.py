from django.db import models
from django.conf import settings


# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post_option = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='no_post_option')
    title = models.CharField(max_length=30)
    select1_content = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='option1_posts', blank=True)
    select2_content = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='option2_posts', blank=True)
    
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #  = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='win_comments')
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.TextField(null=False)