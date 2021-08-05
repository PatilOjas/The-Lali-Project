#from GoalDiggers.login.models import NewUser
from django.db import models

class Assignments(models.Model):
    #username = models.ForeignKey(NewUser,related_name="username",on_delete=models.CASCADE)
    #username = models.ForeignKey('login.NewUser',related_name="username",on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='books/pdfs/')
    marks = models.IntegerField(default=0)


    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)
