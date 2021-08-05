from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.urls import reverse
from PIL import Image

class Tasks(models.Model):
    title=models.CharField(max_length=50,default="")
    desc=models.TextField()
    intern=models.ForeignKey(User,on_delete=CASCADE)
    comments=models.TextField(default=None, blank=True, null=True)
    isComplete=models.BooleanField(default=False)
    file=models.FileField(upload_to='uploads/',default=None, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')  

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    skills=models.TextField()
    resume=models.FileField(upload_to='uploads/resume/',default=None, blank=True, null=True)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img=Image.open(self.image.path)

        if img.height>300 or img.width<300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
# Create your models here.
