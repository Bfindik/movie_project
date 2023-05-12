from django.shortcuts import render
from django.http import HttpResponse
from .models import FilmEkle
from .models import SinemaEkle
from django.shortcuts import get_object_or_404
from django.views.generic.detail import DetailView

# Create your views here.
def index(request):
    film_list = FilmEkle.objects.all()
    return render(request, "movie_app/index.html",{'film_list':film_list})
def film_detail(request, film_title):
    film = get_object_or_404(FilmEkle, title=film_title)
    sinemalar = SinemaEkle.objects.all()
    context = {'film': film, 'sinemalar': sinemalar}
    return render(request, 'movie_app/film_detail.html', context)
def sinemalar(request):
    sinemalar = SinemaEkle.objects.all()
    context = {'sinemalar': sinemalar}
    return render(request, 'movie_app/sinemalar.html', context)

