Untuk memulai project saya menggunakan:
django-admin startproject myproject eshop_pbp

Lalu, untuk membuat aplikasinya saya menggunakan:
cd eshop_pbp
python manage.py startapp main

Untuk routing proyek saya menambahkan: 
path('', include('main.urls'))
pada urlpatterns

Untuk pembuatan model, saya mengubah models.py menjadi:
from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()

Dalam views.py, saya menambahkan:
def show_main(request):
    context = {
        'aplikasi' : 'Ultrapp',
        'nama': 'Ramy Ardya Ramadhan',
        'kelas': 'D'
    }

    return render(request, "main.html", context)

Untuk routing pada main, saya menambahkan:
path('', show_main, name='show_main')
pada urlpatterns

Untuk deployment ke PWS, saya menggunakan:
git push pws main:master



Client --request--> urls.py --routing--> views.py --fetch_data--> models.py --render_template--> main.html 



Git mempermudah pengelolaan dan manajemen proyek



Django memiliki lebih banyak fitur bawaan yang banyak. Selain itu, Django memiliki modules sehingga sangat mudah untuk penggunaannya



Django disebut ORM karena memungkinkan kita berinteraksi dengan database
