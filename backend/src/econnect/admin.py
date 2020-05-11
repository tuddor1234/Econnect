# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import User
from .models import Training
from .models import Trainer
from .models import Profile

# Register your models here.

admin.site.register(User)
admin.site.register(Trainer)
admin.site.register(Training)
admin.site.register(Profile)
