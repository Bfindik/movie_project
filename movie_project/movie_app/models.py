from django.db import models
# Create your models here.
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
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['title']
class SinemaEkle(models.Model):
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
    salon = models.ForeignKey(SalonEkle, on_delete=models.CASCADE, related_name='seanslar')
    film = models.ForeignKey(FilmEkle, on_delete=models.CASCADE, related_name='seanslar')
    class Meta:
        ordering = ['saat']

    
