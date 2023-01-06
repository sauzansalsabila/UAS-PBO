from django.contrib import admin
from .models import *
class tampil(admin.ModelAdmin):
    list_display = ['namakapten', 'tanggalberangkat', 'jenisikan', 'jumlah', 'img']
    search_fields = ['namakapten', 'tanggalberangkat', 'jenisikan']
    list_filter = ['alattangkap']
    list_per_page = 5

admin.site.register(lagu, tampil)
admin.site.register(alattangkap)
admin.site.register(peta)
# Register your models here.
