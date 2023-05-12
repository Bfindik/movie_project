from django.contrib import admin
from .models import FilmEkle
from .models import SinemaEkle
from .models import SeansEkle
from .models import SalonEkle
# Register your models here.
admin.site.register(FilmEkle)
admin.site.register(SinemaEkle)
admin.site.register(SeansEkle)
admin.site.register(SalonEkle)