http://pbptugas-2.herokuapp.com/todolist/


Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
    → Inline adalah penulisan style CSS pada elemen HTML sebagai attribute dari tag elemen HTML itu sendiri,
        <h1 style="color:green;text-align:center;">PBP</h1>
        dengan kelebihan dan kekurangan :
               + Dapat mengganti atau mengcustom elemen sebebas mungkin karena tidak berpengaruh antar elemen yang lain
               + Mudah untuk melihat dan menguji perubahan pada tiap elemen
               - Attribute tiap elemen banyak atau menjadi panjang
               - Sulit untuk dibaca karena style yang terlalu banyak
    → Internal adalah penulisan style CSS pada elemen HTML sebagai attribute yang diletakkan diantara tag <style>
            <style> 
                h1 {
                    color: green;
                    text-align:center;
                } 
            </style>
            dengan kelebihan dan kekurangan :
                    + Semua attribute CSS menjadi satu
                    + Perubahan secara internal karena berlaku pada satu file HTML itu sendiri
                    - Attribute CSS bercampur dengan dokumen HTML
                    - Performa web melambat karena ukural file HTML yang menjadi besar
    → External CSS adalah penulisan style CSS pada elemen, yang mana terpisah dari kode HTML serta akan dihubungkan ke file HTML dengan tag <link>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        dengan kelebihan dan kekurangan :
                + Memudahkan membuat banyak properti
                + Struktur HTML menjadi lebih rapi 
                - Terlalu kompleks sehingga tidak efektif
                - Tampilan web akan berpengaruh apabila terdapat masalah saat file CSS dihubungkan ke file HTML


Jelaskan tag HTML5 yang kamu ketahui!
    <body> → Untuk membuat body atau isi yang ingin ditampilkan
    <br> → Untuk membuat baris kosong atau baris baru
    <div> →  Untuk melambangkan bagian tertentu dari isi
    <table> → Untuk mendefiniskan awal dan akhir table
    <th> → Untuk membuat judul pada tabel (table head)
    <tr> → Untuk membuat baris pada tabel (table row)
    <td> → Untuk membuat isi pada baris (table data)
    <title> → Untuk membuah judul halaman web
    <a> → Untuk memasukkan link aktif pada elemen HTML
    <button> → Untuk membuat tombol


Jelaskan tipe-tipe CSS selector yang kamu ketahui!
    ID selector → Untuk menerapkan style pada elemen berdasarkan ID, dengan #id-example {}
    Class selector → Untuk menerapkan style pada elemen berdasarkan class, dengan .class-example {}
    Tag selector → Untuk menerapkan syle pada elemen berdasarkan tag, dengan p {}


Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas!
    → Menambahkan navbar pada file todolist.html di folder templates yang ada pada folder todolist
        <nav class="navbar" style="background-color: rgb(140, 240, 220);font-family: monospace;">
            <div class="container-fluid">
            <span class="navbar-brand mb-0 h1">Hello {{user}}!&#9829</span>
            <a class="btn btn-warning" type="button" href="{% url 'todolist:logout' %}">Log Out</a>
            </div>
        </nav> 
    → Menambahkan code styling pada file todolist.html, register.html, login.html, create-task.html
    → Membuat keempat halaman yang dikustomisasi menjadi responsive dengan menambahkan code pada file base.html di folder templates
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    → Melakukan deploy pada heroku
