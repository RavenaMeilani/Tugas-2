Jelaskan perbedaan antara JSON, XML, dan HTML!
    → JSON merupakan singkatan dari JavaScript Object Notation, yang didesain menjadi self-describing sehingga mudah untuk dimengerti. JSON digunakan pada banyak aplikasi web maupun mobile, yaitu untuk menyimpan dan mengirimkan data. Sintaks JSON merupakan turunan dari Object JavaScript, akan tetapi format JSON berbentuk text, sehingga kode untuk membaca dan membuat JSON banyak terdapat di banyak bahasa pemrograman.
    → XML merupakan singkatan dari eXtensible Markup Language, yang didesain menjadi self-descriptive sehingga dengan membaca XML dapat mengerti informasi apa yang ingin disampaikan dari data tertulis. XML digunakan pada banyak aplikasi web maupun mobile, yaitu untuk menyimpan dan mengirimkan data. XML hanyalah informasi yang dibungkus dalam tag, sehingga perlu menulis lagi program untuk mengirim, menerima, menyimpan, dan menampilkan informasi.
    → HTML merupakan singkatan dari HyperText Markup Language, yaitu bahasa markup standar untuk membuat serta menyusun halaman dan aplikasi web. HTML digunakan untuk mendeskripsikan struktur dan layout pada web. HTML tidak dianggap sebagai bahasa pemrograman karena tak bisa memberikan fungsi yang dinamis. Umumnya, fungsi HTML adalah untuk mengelola serangkaian data serta informasi sehingga suatu dokumen dapat diakses dan ditampilkan di web.


Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform!
    → Format untuk pertukaran data, pengiriman data, atau request response bisa dalam bentuk JSON, XML, maupun HTML, yang mana format-format data tersebut merupakan data delivery, yang digunakan untuk menyimpan dan mengirimkan data, serta komunikasi antar program, guna pengimplementasian sebuah platform.


Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!
    → setelah mengaktifkan virtual environtment di cmd, menjalankan printah python manage.py startapp mywatchlist.
    → pada file settings.py di folder project_djanggo menambahkan ‘mywatchlist’, di dalam variable INSTALLED-APP.
    → pada file models.py di folder mywatchlist menambahkan potongan kode :
        from django.db import models

        class MyWatchlist(models.Model):
            watched = models.CharField(max_length=50)
            title = models.CharField(max_length=50)
            rating = models.FloatField()
            release_data = models.CharField(max_length=50)
            review = models.TextField()
    → menjalankan perintah python manage.py makemigrations dilanjut dengan python manage.py migrate di cmd.
    → pada folder fixtures di folder mywatchlist membuat file bernama initial_mywatchlist_data.json dengan isi potongan kode :
        [
            {
                “model”:”mywatchlist.MyWatchlist”,
                “pk”:(1-10), 
                “fields”:{
                    “watched”:”...”,
                    “title”:”...”,
                    “rating”:”...”,
                    “release_date”:”...”,
                    “review”: ”...”
                } 
            }
        ]
    → menjalankan perintah python manage.py loaddata initial_mywatchlist_data.json di cmd
    pada file views.py di folder mywatchlist menambahkan kode : 
        def show_mywatchlist (request):
            return render(request, "mywatchlist.html", context)
    → pada folder templates di folder mywatchlist membuat sebuah file mywatchlist.html dengan isi :
        {% extends 'base.html' %}

        {% block content %}
        <h5>Nama: </h5>
        <p>{{nama}}</p>
        <h5>NPM: </h5>
        <p>{{npm}}</p>

        <table>
            <tr>
            <th>Watched</th>
            <th>Title</th>
            <th>Rating</th>
            <th>Release Date</th>
            <th>Review</th>
            </tr>
            {% comment %} Tambahkan data di bawah baris ini {% endcomment %}
            {% for watchlist in my_watchlist %}
                <tr>
                    <th>{{watchlist.watched}}</th>
                    <th>{{watchlist.title}}</th>
                    <th>{{watchlist.rating}}</th>
                    <th>{{watchlist.release_date}}</th>
                    <th>{{watchlist.review}}</th>
                </tr>
            {% endfor %}
        </table>

        {% endblock content %}
    → pada folder mywatchlist terdapat file bernama urls.py berisi kode :
        from django.urls import path
        from mywatchlist.views import show_mywatchlist 

        app_name = ‘My Watchlist ’

        urlpatterns = [
            path('', show_mywatchlist, name='show_mywatchlist '),
        ]
    → menambahkan kode path('wishlist/', include('wishlist.urls')), ke dalam urls.py di folder project_django.
    → pada file views.py di folder mywatchlist ditambahkan :
        from django.shortcuts import render
        from mywatchlist.models import MyWatchlist 
    → menambahkan potongan kode di fungsi show_mywatchlist yaitu :
            data_mywatchlistt =MyWatchlist.objects.all()
            context = {
                'list_barang': data_barang_wishlist,
                'nama': 'Ravena Meilani'
                'npm': '2106631923'
            }
    → mengakses URL melalui :
        http://localhost:8000/mywatchlist/html 
        http://localhost:8000/mywatchlist/xml
        http://localhost:8000/mywatchlist/json
    → melakukan deployment ke Heroku.



Sources :
    https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-2
    https://www.hostinger.co.id/tutorial/apa-itu-html
    https://lmsspada.kemdikbud.go.id/mod/page/view.php?id=57743
    https://drive.google.com/file/d/1HrSrBaxfdouWJKskgQuA0e59Kv-DO3he/view
    https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-1