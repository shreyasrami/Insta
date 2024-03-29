from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    full_name = models.CharField(default=None,max_length=25,null=True)
    dp = models.ImageField(upload_to='post_images',null=True,blank=True,default='post_images/dp_meirma') 
    follows = models.ManyToManyField('self',related_name='followed_by',symmetrical=False,blank=True)
    bio = models.CharField(default=None,max_length=50,null=True,blank=True)
    
    def __str__(self): 
        return str(self.user)

class Post(models.Model):
    author = models.ForeignKey('Profile',on_delete=models.CASCADE)
    img = models.ImageField(upload_to='post_images')
    caption = models.CharField(default=None,max_length=100)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.author)+'_'+str(self.pk)

    class Meta:
        ordering = ['-post_date']
    
class Comment(models.Model):
    post = models.ForeignKey('Post',on_delete=models.CASCADE)
    commentby = models.ForeignKey('Profile',on_delete=models.CASCADE)
    comments = models.CharField(max_length=100)
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.post)+'_'+str(self.commentby)
    
    class Meta:
        ordering = ['-comment_date']
    
class Like(models.Model):
    post = models.ForeignKey('Post',on_delete=models.CASCADE)
    likedby = models.ForeignKey('Profile',on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.post)+'_'+str(self.likedby)

