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





Menurut saya, data delivery penting untung diimplementasikan karena, seperti namanya, data delivery berguna untuk menjamin kebenaran dan keefisianan pertukaran data sehingga bisa terdapat komunikasi antara server dan client dengan baik.



Menurut saya JSON lebih baik. Menurut saya JSON lebih populer karena format datanya tidak sekompleks XML sehingga ukuran filenya lebih kecil.



Method is_valid berguna untuk validasi input. Pada kasus ini, kita memerlukan is_valid untuk memastikan semua input forms diisi sesuai dengan kriteria yang kita buat.



Kita membutuhkan csrf_token saat membuat forms di django karena csrf_token dapat mengamankan kita dari serangan csrf pada input fields, salah satunya forms. Jika tidak ada csrf_token, kita akan terancam serangan csrf oleh seorang penyerang. Salah satu contohnya, penyerang dapat melakukan aktivitas ilegal sebagai user lain.



Untuk input forms, saya membuat forms.py yang berisi:
from django.forms import ModelForm
from main.models import Product

class EntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price"]

Lalu, saya mennambahkan mengubah views.py menjadi:
from django.shortcuts import render, redirect
from main.forms import EntryForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_main(request):
    entries = Product.objects.all()
    context = {
        'aplikasi' : 'Ultrapp',
        'nama': 'Ramy Ardya Ramadhan',
        'kelas': 'D',
        'entries': entries
    }

    return render(request, "main.html", context)

def create_entry(request):
    form = EntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_entry.html", context)

Lalu, untuk menampilkan akses input forms ini saya mengubah main.html menjadi:
 <p>{{ aplikasi }}<p>
<p>{{ nama }}<p>
<p>{{ kelas }}<p>
 {% block content %}
 <p>{{ aplikasi }}<p>
 <p>{{ nama }}</p>
 <p>{{ kelas }}</p>
{% if not entries %}
<p>Belum ada data.</p>
{% else %}
<table>
  <tr>
    <th>Name</th>
    <th>Description</th>
    <th>Price</th>
  </tr>

  {% comment %} Berikut cara memperlihatkan data di bawah baris ini 
  {% endcomment %} 
  {% for entry in entries %}
  <tr>
    <td>{{entry.name}}</td>
    <td>{{entry.description}}</td>
    <td>{{entry.price}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_entry' %}">
  <button>Add New Entry</button>
</a>
{% endblock content %}
Lalu, untuk pembuatan formsnya, saya membuat create_entry.html yang berisi:

{% block content %}
<h1>Add New Mood Entry</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Mood Entry" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}

Lalu, saya melakukan routing dengan mengubah urls.py menjadi:

from django.shortcuts import render, redirect
from main.forms import EntryForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_main(request):
    entries = Product.objects.all()
    context = {
        'aplikasi' : 'Ultrapp',
        'nama': 'Ramy Ardya Ramadhan',
        'kelas': 'D',
        'entries': entries
    }

    return render(request, "main.html", context)

def create_entry(request):
    form = EntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_entry.html", context)

Terakhir, untuk menjawab pertanyaan - pertanyaan pada checklist sebelum ini, saya menggunakan Google, SCELE, dan OpenAI sebagai sumber pustaka.