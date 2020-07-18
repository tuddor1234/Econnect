# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class EconnectConfig(AppConfig):
    name = 'econnect'

    def ready(self):
        import signals