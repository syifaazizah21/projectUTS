from multiprocessing import context
from django.shortcuts import render
from .models import MataKuliah, CatatanMk, SoalMk, Blog

# Create your views here.
def index(request):
    return render(request, 'index.html')

def listMk(request):
    mk = MataKuliah.objects.all()
    conteks = {
        'mk': mk,
    }
    return render(request, 'listmk.html', conteks)

def catatanMk(request):
    catatan_mk = CatatanMk.objects.all()
    conteks = {
        'catatanMk': catatan_mk,
    }
    return render(request, 'catatanmk.html', conteks)

def soalLatihan(request):
    soal_mk = SoalMk.objects.all()
    conteks = {
        'soalMk': soal_mk,
    }
    return render(request, 'soallatihan.html', conteks)

def blog(request):
    blog = Blog.objects.all()
    conteks = {
        'blog': blog
    }
    return render(request, 'blog.html', conteks)