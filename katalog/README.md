Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;


Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
    Secara umum, virtual environment merupakan sebuah tool yang memungkinkan untuk membentuk lingkup kerja python terisolasi. Sesuai definisi tersebut, virtual environment digunakan karena setiap project pasti memiliki dependent yang berbeda antara satu dengan yang lainnya, sehingga virtual environment digunakan untuk menjalankan project tersebut tanpa merubah configurasi pada sustem operasi yang dipakai. Sedarhananya, agar menecegah adanya salung ganggu antar project yang sedang di develop. Akan tetapi, virtual environment dapat tidak diinstall atau tidak dibuat untuk pembuatan aplikasi web berbasis Django, dengan resiko hanya bisa menggunakan satu versi Django saja di satu PC. Hal tersebut didasarkan karena virtual environment pada Django berfungsi sebagai tempat penginstallan Djanggo sendiri dan beberapa depedency aplikasi tersebut.


Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas!
    Pada file views.py di folder katalog membuat fungsi yang menerima parameter request dan mengembalikan render :  def show_katalog(request):
                                return render(request, "katalog.html", context).

    Pada folder katalog terdapat folder templates yang di dalamnya terdapat file katalog.html beserta isinya. Pada template isi tersebut terdapat code   <h5>Name: </h5> dan <h5>Student ID: </h5> diubah menjadi <h5>Name: </h5> dan <h5>Student ID: </h5>
                    <p>Fill me!</p>     <p>Fill me!</p>                      <p>{{nama}}</p>     <p>{{NPM}}</p>
    Selain itu juga menambahkan {% for katalog in list_katalog_barang %}
                                    <tr>
                                        <th>{{katalog.item_name}}</th>
                                        <th>{{katalog.item_price}}</th>
                                        <th>{{katalog.item_stock}}</th>
                                        <th>{{katalog.rating}}</th>
                                        <th>{{katalog.description}}</th>
                                        <th>{{katalog.item_url}}</th>
                                    </tr>
                                {% endfor %}
                                </table>.

    Pada folder katalog dengan file urls.py ditambahkan code from django.urls import path
                                                            from katalog.views import show_katalog
                                                            app_name = 'katalog'
                                                            urlpatterns = [
                                                                path('', show_katalog, name='show_katalog'),
                                                            ]
    yang berguna untuk melakukan routing terhadap fungsi views.py sehingga halaman HTML dapat dapat ditampilkan pada browser.

    Pada folder project_django terdapat file urls.py dimana ditambahkan code path('katalog/', include('katalog.urls')).

    Selanjutnya menjalankan perintah python manage.py runserver pada command prompt, lalu membuka url http://localhost:8000/katalog/ untuk melihat halaman yang sudah dibuat.

    Terakhir, melakukan deployment ke Heroku.



Sources :
https://pbp-fasilkom-ui.github.io/ganjil-2023/assignments/tutorial/tutorial-1/
https://edikartono.com/python/cara-membuat-virtual-environment-python
https://dev.notnoob.com/tutorial-virtual-environment/#what
https://ridoannasution.medium.com/belajar-membuat-aplikasi-music-crud-menggunakan-framework-django-a44872859183