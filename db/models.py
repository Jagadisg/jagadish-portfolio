from django.db import models

# Create your models here.
class contact(models.Model):
    sr_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=100 , default='')
    subject = models.CharField(max_length=200)
    message = models.TextField(default='')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


