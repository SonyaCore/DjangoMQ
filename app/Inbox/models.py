from django.db import models

# Create your models here.
class Inbox(models.Model):
    id = models.IntegerField(unique=True, primary_key=True)
    subject = models.CharField(max_length=50)
    email = models.EmailField(max_length=48)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.subject

class InboxUser(models.Model):
    user_id = models.IntegerField( blank=True)
    message_id = models.IntegerField(unique=True, blank=True)

    def __str__(self):
        return f"User id {str(self.user_id)} Message ID {str(self.quote_id)}"