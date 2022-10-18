from django.contrib import admin
from .models import MataKuliah, CatatanMk, SoalMk, Blog

# Register your models here.
admin.site.register(MataKuliah)
admin.site.register(CatatanMk)
admin.site.register(SoalMk)
admin.site.register(Blog)