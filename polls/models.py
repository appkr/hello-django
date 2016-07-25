from __future__ import unicode_literals

from django.db import models


class Question(models.Model):
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField('date published')

    def __unicode__(self):
        return self.text


class Alternative(models.Model):
    question = models.ForeignKey(Question)
    text = models.CharField(max_length=200)
    vote_count = models.IntegerField(default=0)

    def __unicode__(self):
        return self.text
