from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return "<User: {}-{}>".format(self.username, self.first_name)


class UserResume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.TextField()
    date_of_adding = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<UserResume: {}".format(self.user.username)
