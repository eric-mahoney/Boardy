from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    ''' model for the different users '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(default="default.jpg", upload_to="profile_pictures")
    date_created = models.DateTimeField(auto_now=True, null=False)
    
    def __str__(self):
        return '{}'.format(self.user.username)

class Board(models.Model):
    ''' model for the message board '''
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    board_name = models.CharField(max_length=50, null=False, default="untitled board name")
    date_created = models.DateTimeField(auto_now=True, null=False)
    message_count = models.IntegerField(default=0)
    
    def __str__(self):
        return '{} - {}'.format(self.board_name, self.creator)

class Message(models.Model):
    ''' model for the messages within the message board '''
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.CharField(max_length=250, default='content', null=False)
    date_created = models.DateTimeField(auto_now=True, null=False)

    def __str__(self):
        return '{}: {}'.format(self.creator, self.content)