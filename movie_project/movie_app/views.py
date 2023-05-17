from django.shortcuts import render
from .models import FilmEkle
from .models import SinemaEkle
from .models import SeansEkle
from .models import Bilet
from django.shortcuts import get_object_or_404
from datetime import datetime, date
# Create your views here.
def index(request):
    film_list = FilmEkle.objects.all()
    return render(request, "movie_app/index.html",{'film_list':film_list})
def film_detail(request, film_title):
    film = get_object_or_404(FilmEkle, title=film_title)
    seanslar = SeansEkle.objects.filter(film=film)
    genres = film.genres.all()
    today = date.today()  # Geçerli tarih
    current_time = datetime.now().time()  # Geçerli saat
    return render(request, 'movie_app/film_detail.html', {'film': film, 'today': today, 'current_time': current_time, 'seanslar':seanslar, 'genres':genres})
def sinemalar(request):
    sinemalar = SinemaEkle.objects.all()
    context = {'sinemalar': sinemalar}
    return render(request, 'movie_app/sinemalar.html', context)
def bilet_alma(request):
    biletler = Bilet.objects.all()
    context = {'biletler': biletler}
    return render(request, 'movie_app/bilet.html', context)



