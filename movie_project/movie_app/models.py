from time import timezone
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
# Create your models here.
class Genre(models.Model):
    type = models.CharField(max_length=100)
    def __str__(self):
        return self.type
class FilmEkle(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField(max_length=1000)
    vision_date = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    actors = models.TextField(max_length=500)
    formats = models.TextField(max_length=500)#tekrar bak
    date = models.DateTimeField(blank=True)
    image = models.URLField( max_length=500)
    trailer = models.URLField( max_length=300)
    genres = models.ManyToManyField(Genre, related_name='filmler')
    imdb_score = models.FloatField()
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title']
class SinemaEkle(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    gold_class = models.BooleanField(default=True)
    filmler = models.ManyToManyField(FilmEkle, related_name='sinemalar')
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title']
class SalonEkle(models.Model):
    capacity= models.IntegerField()
    salon_id = models.CharField(max_length=100)
    sinema = models.ForeignKey(SinemaEkle, on_delete=models.CASCADE, related_name='salonlar')
    def __str__(self):
        return self.salon_id
    class Meta:
        ordering = ['salon_id']
class SeansEkle(models.Model):
    tarih = models.DateField()
    saat = models.TimeField()
    altyazi = models.BooleanField(default=False)
    dublaj = models.BooleanField(default=False)
    salon = models.ForeignKey(SalonEkle, on_delete=models.CASCADE, related_name='seanslar')
    film = models.ForeignKey(FilmEkle, on_delete=models.CASCADE, related_name='seanslar')
    class Meta:
        ordering = ['tarih']
    def clean(self):
        if self.tarih < timezone.now().date():
            raise ValidationError("Geçmiş bir tarih ekleyemezsiniz.")
        if self.tarih == timezone.now().date():
          if self.saat < timezone.now().time():
            raise ValidationError("Geçmiş bir saat ekleyemezsiniz.")
class Bilet(models.Model):
    TAM = 'tam'
    OGRENCI = 'ogrenci'
    
    BILET_TIPLERI = [
        (TAM, 'Tam Bilet'),
        (OGRENCI, 'Öğrenci Bilet'),
    ]
    bilet_tipi = models.CharField(max_length=10, choices=BILET_TIPLERI, default=TAM)
    fiyat = models.DecimalField(max_digits=8, decimal_places=2)
    seans = models.ForeignKey(FilmEkle, on_delete=models.CASCADE, related_name='biletler')
    adet = models.IntegerField()
    
