from django.contrib import admin

from AppCoder.models import Hermanos, Nietos, Padres

# Register your models here.
admin.site.register(Padres)
admin.site.register(Hermanos)
admin.site.register(Nietos)