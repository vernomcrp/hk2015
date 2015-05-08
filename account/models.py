from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class GroupAccount(models.Model):
    group_no = models.IntegerField()
    note = models.TextField(max_length=200)
    def __unicode__(self):
        return u'{} {}'.format(self.group_no, self.note)

class Account(models.Model):
    user = models.ForeignKey(User)
    group = models.ForeignKey(GroupAccount)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return u'group: {}, user: {}, is_admin {}'.format(self.group.note, self.user.username, self.is_admin)


