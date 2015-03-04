__author__ = 'praneeth'
from django.contrib import admin
from .models import ModelA

import reversion

class BaseReversionAdmin(reversion.VersionAdmin):
    pass
admin.site.register(ModelA, BaseReversionAdmin)