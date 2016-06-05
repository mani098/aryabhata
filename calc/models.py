from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class CalcLog(models.Model):
    user = models.ForeignKey(User)
    equation = models.TextField(null=True, blank=True, default=None)
    added_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s - %s" %(self.user, self.equation)


