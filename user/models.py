from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
import time

class UserGroup(models.Model):

    name = models.CharField(max_length=80, unique=True)

    comment = models.CharField(max_length=160, blank=True, null=True)

    def __str_(self):
        return self.name


class User(AbstractUser):
    USER_ROLE_CHOICES = (
        ('SU', 'SuperUser'),
        ('GA', 'GroupAdmin'),
        ('CU', 'CommonUser'),
    )
    name = models.CharField(max_length=80)
    uuid = models.CharField(max_length=100)
    role = models.CharField(max_length=2, choices=USER_ROLE_CHOICES, default='CU')
    group = models.ManyToManyField(UserGroup)


    def __str__(self):
        return self.username


class AdminGroup(models.Model):
    """
    under the user control group
    用户可以管理的用户组，或组的管理员是该用户
    """

    user = models.ForeignKey(User)
    group = models.ForeignKey(UserGroup)

    def __str__(self):
        return '%s: %s' % (self.user.username, self.group.name)


# class Document(models.Model):
#     def upload_to(self, filename):
#         return 'upload/'+str(self.user.id)+time.strftime('/%Y/%m/%d/', time.localtime())+filename
#
#     docfile = models.FileField(upload_to=upload_to)
#     user = models.ForeignKey(User)
