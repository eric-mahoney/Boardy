from django.contrib import admin
from .models import Profile, Board, Message

# Register your models here.
admin.site.register(Profile)
admin.site.register(Board)
admin.site.register(Message)