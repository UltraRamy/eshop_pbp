from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'aplikasi' : 'Ultrapp',
        'nama': 'Ramy Ardya Ramadhan',
        'kelas': 'D'
    }

    return render(request, "main.html", context)