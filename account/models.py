from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
