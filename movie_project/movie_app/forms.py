from django import forms
from .models import SinemaEkle
class ListForm(forms.ModelForm):
    class Meta:
        model= SinemaEkle
        fields = ["sinema","film","seans","bilet_türü","koltuk","ödeme"]
