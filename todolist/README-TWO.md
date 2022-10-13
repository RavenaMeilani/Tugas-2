Link heroku : http://pbptugas-2.herokuapp.com/todolist/


**Jelaskan perbedaan antara asynchronous programming dengan synchronous programming!**
    
→ Pada asynchronous programming, code dieksekusi secara bersamaan dan tidak perlu menunggu baris code sebelumnya selesai. Code function selanjutnya dapat dijalankan tanpa menunggu function sebelumnya selesai.
   
→ Pada synchronous programming, code dieksekusi secara berurutan dan perlu menunggun baris code sebelumnya selesai. Code function selanjutnya tidak dapat dijalankan apabila code function sebelumnya belum selesai.


**Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini!**

→ Paradigma Event-Driven programming merupakan alur yang dijalankan untuk  mengeksekusi program  didasarkan pada event (tindakan antar user dan client). Contohnya adalah pada tugas 6 ini, ketika memencet tombol submit pada form addTask maka data akan ditambahkan dan ditampilkan dengan card.


**Jelaskan penerapan asynchronous programming pada AJAX!**

→ Browser tidak perlu menangguhkan operasi yang dilakukan selama req AJAX berlangsung, bahkan dapat melaksanakan perintah yang lain selama request tersebut berjalan di latar belakang. Sehingga AJAX dapat mengubah tampilan web berdasar hasil tanpa memerlukan reload. 


**Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!**

→ Dimulai dengan membuat perubahan pada views.py sesuai dengan persyaratan yang dituliskan pada soal, yakni membuat fungsi bernama todolist_json yang berfungsi untuk mengembalikan seluruh data task dalam bentuk json lalu pengembalikan data task tersebut akan diambil menggunakan AJAX GET.
Slanjutnya membuat sebuah fungsi baru show_addTask pada views.py serta membuat perubahan pada todolist.html untuk menyambungkan AJAX.
