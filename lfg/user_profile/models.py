from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class LFGProfile(models.Model):
    # Profile info fields
    user = models.ForeignKey(User)
    postal_code = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    def __unicode(self):
        return self.__str__()


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        LFGProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)