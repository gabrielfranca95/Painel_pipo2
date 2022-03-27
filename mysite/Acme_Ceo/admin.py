from django.contrib import admin
from .models import Norte_Europa
from .models import Dental_Sorriso
from django.contrib.auth.models import Group



# Register your models here.
admin.site.register(Norte_Europa)

admin.site.register(Dental_Sorriso)

admin.site.unregister(Group)



