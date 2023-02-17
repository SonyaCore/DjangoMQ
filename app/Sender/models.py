from django.db import models

# Create your models here.
class Sender(models.Model):
    subject = models.CharField(max_length=50)
    email = models.EmailField(max_length=48)
    message = models.CharField(max_length=1000)

    def __dir__(self):
        return self.subject
