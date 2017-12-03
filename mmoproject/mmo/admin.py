from django.contrib import admin
import mmo.models
# Register your models here.
admin.site.register(mmo.models.PlayerAccount)
admin.site.register(mmo.models.Character)
admin.site.register(mmo.models.Guild)