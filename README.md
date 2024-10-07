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





HttpResponseRedirect() hanya bisa menerima url sebagai argument sehingga redirect() lebih fleksibel



Menggunakan ForeignKey yang bersifat many-to-one



Authentication adalah verifikasi apakah user asli sedangkan authorization adalah pengecekan hak ases user. Authetication diimplementasikan dengan login form (user password) dan authorization diimplementasikan dengan @login_required



Django mengingat user dengan ID pada cookies. Cookies dapat digunakan untuk menyimpan hal lain sesuai parameter yang diberikan. Tidak semua cookies aman digunakan.



Untuk mengimplementasikan ungsi registrasi, login, dan logout, saya menambahkan fungsi tersebut pada view.y seperi berikut:
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

Setelah itu saya routing pada urls.py
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),




Untuk data dummy, saya register 2 user lalu login ke dua - duanya  dan melakukan add entry 3x untuk masing - masing user.



Untuk menghubungkan product dengan user saya menggunakan foreignkey pada models.py user = models.ForeignKey(User, on_delete=models.CASCADE) dan entries = Product.objects.filter(user=request.user) pada show_main views.py


 
Untuk last login saya menambahkan <h5>Sesi terakhir login: {{ last_login }}</h5> pada main.html dan 'last_login': request.COOKIES['last_login'] pada show_main views.py



Untuk pertanyaan-pertanyaan di README.md saya mencari referensi dengan berselancar internet.




,
Urutan prioritas dari tinggi ke rendah: inline styles > IDs > classes, attribute selectors, pseudoclasses > elements, pseudoelements



Meningkatkan pengalaman pengguna. 
Contoh yang menerapkan: https://scele.cs.ui.ac.id/
Contoh yang tidak menerapkan: https://dequeuniversity.com/library/responsive/1-non-responsive



Padding adalah Jarak antara border dengan konten. Border adalah garis pembatas box. Margin adalah area di luar box.
Cara implementasinya menggunakan property. Contohnya:
div {
  border: 10px solid green;
  padding: 20px;
  margin: 30px;
}



Flex box adalah modul layout yang fleksibel. Grid llayout adalah modul layout yang berbasis grid. Keduanya berguna untuk memudahkan web desain tanpa memerlukan floats dan positioning 



Membuat fungsi delete yang menggunakan object.delete() pada views.pw dan melakukan routing pada urls.py
Membuat fungsi edit yang mirip dengan create pada views.py dan melakukan routing pada urls.py
Menambahkan <script src="https://cdn.tailwindcss.com"> pada main.html
Menambahkan desain pada login, register, create dengan menggunakan css pada html masing - masing
Membuat card dengan menambahkan card.html dan card_info.html
Membuat png file pada static/image dan menambahkannya pada main.html
Membuat 2 button edit dan delete dengan href halaman masing - masing pada card
Membuat navbar.html pada templates
Menjawab README.md dengan W3Schools sebagai sumber utama jawaban



Manfaat dari penggunaan JavaScript dalam pengembangan aplikasi web adalah membuat aplikasi web menjadi interaktif. JavaScript memungkinkan kita untuk menambahkan elemen - elemen interaktif.
Fungsi dari penggunaan await ketika kita menggunakan fetch() adalah memastikan kebenaran hasil fetch(). Dengan await, eksekusi kode akan berhenti sejenak sampai fetch mengembalikan hasilnya. Jika kita tidak menggunakan await, ada kemungkinan hasil fetch tidak lengkap. 
Kita perlu menggunakan decorator csrf_exempt pada view yang akan digunakan untuk AJAX POST agar dikecualikan dari verifikasi CSRF dan bisa dijalankan.
Pembersihan data input pengguna tidak dilakukan di frontend saja karena masih terdapat risiko untuk di bypass, sedangkan backend lebih dapat dikendalikan sehingga untuk memastikan keduanya, pembersihan data input di backend harus dilakukan.
Untuk AJAX, saya menambahkan kode di bawah pada views.py
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
@csrf_exempt
@require_POST
def add_mood_entry_ajax(request):
    name = strip_tags(request.POST.get("name")) # strip HTML tags!
    description = strip_tags(request.POST.get("descrption"))
    price = request.POST.get("price")
    user = request.user
    new_mood = Product(
        name=name, description=description,
        price=price,
        user=user
    )
    new_mood.save()
    return HttpResponse(b"CREATED", status=201)
Lalu, routing ke urls.py dengan kode di bawah
from main.views import add_mood_entry_ajax
path('create-ajax', add_mood_entry_ajax, name='add_mood_entry_ajax'),
Membersihkan forms.py menggunakan strip_tags()
Menambahkan script dan modal pada main.html yang dapat dilihat pada main.html (terlalu Panjang jika diletakkan di sini)
