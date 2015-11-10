from django.contrib import admin
from .models import Plans, Processes, Species

# Register your models here.

admin.site.register(Plans)
admin.site.register(Processes)
admin.site.register(Species)
