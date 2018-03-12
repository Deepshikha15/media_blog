# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class Update(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now(), blank=True)

    def __unicode__(self):
        return self.title
