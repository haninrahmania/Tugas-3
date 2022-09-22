Link menuju aplikasi Heroku Tugas 3: https://tugas3pbphanin.herokuapp.com/mywatchlist/

1. Perbedaan antara JSON, XML dan HTML:
- Penyimpanan Elemen. Cara penyimpanan elemen pada JSON efisien, namun kurang rapi untuk dilihat. XML menyimpan elemen elemennya secara kurang efisien, namun terstruktur sehingga mudah dibaca oleh manusia dan mesin. Sedangkan HTML elemennya tersimpan secara sederhana dan relatif mudah dibaca, dengan kode sederhana (tag dan attribute) untuk mark up halaman website.
- Ekstensi File. File JSON diakhiri ekstensi .json, file XML .xml, dan file HTML .html atau .htm.
- Implementasi. JSON digunakan untuk mengirimkan data dengan cara diuraikan dan dikirim melalui internet. Data XML lebih terstruktur dan user dapat menggunakannya untuk menambah catatan. HTML digunakan sebagai bahasa markup yang kini dianggap sebagai standar web resmi.

2. Pentingnya data delivery dalam pengimplementasian sebuah platform:
Data delivery penting dalam pengimplementasian sebuah platform karena data delivery merupakan suatu proses memindahkan data dari suatu platform menuju platform lainnya. Data tersebut dapan berupa berbagai format, seperti JSON, XML, dan HTML.

3. Pertama saya membuat folder mywatchlist dan membuka views.py yang terdapat pada folder mywatchlist dan membuat suatu fungsi show_watchlist yang menerima parameter 'request' dan mengembalikan 'render(request,"mywatchlist.html")'. Lalu saya import models yang sudah tersedia kedalam berkas views.py untuk melakukan pengambilan data dari database dengan 'from mywatchlist.models import WatchlistItem'. Kedalam fungsi show_watchlist saya masukkan kode untuk memanggil fungsi query ke model database dan menyimpan hasil query tersebut ke dalam variabel dan menambahkan parameter ketiga yaitu 'context' pada pengembalian fungsi render supaya data pada variabel context tersebut akan dirender oleh django sehingga data tersebut dapat muncul pada halaman html. Kemudian saya mengubah beberapa hal pada berkas mywatchlist.html pada folder templates dalam mywatchlist, seperti item yang akan di display. Pada berkas urls.py dalam folder mywatchlist saya membuat routing terhadap fungsi views yang sudah dibuat sebelumnya sehingga halaman html, xml, dan json dapat ditampilan pada browser, yang berisikan app name, yaitu mywatchlist, dan urlpatterns yang berisi 'path('', show_watchlist, name='show_watchlist'),'. Setelah itu saya daftarkan aplikasi mywatchlist ke dalam berkas urls.py pada folder project_django dengan memasukkan 'path('mywatchlist/', include('mywatchlist.urls')),'. Saya melakukan iterasi terhadap variabel 'data_watchlist' untuk menampilkan details watchlist. Untuk melakukan deployment ke Heroku terhadap aplikasi yang sudah saya buat saya melakukan step-step berikut:

Buat aplikasi di Heroku

Ke github bagian settings, cari secrets dan pilih actions, klik 'Create new secret repository'

Membuat 2 secret repo, yang satu HEROKU_API_KEY isinya api key Heroku. Satunya lagi HEROKU_APP_NAME isinya nama aplikasi yang dibuat pada Heroku.

Membuka 'actions' pada repo github lalu mere-run all jobs untuk failed deployment.

Membuka aplikasi melalui link https://tugas3pbphanin.herokuapp.com/mywatchlist/

![image](https://user-images.githubusercontent.com/112334401/191660882-00a6f171-e749-4c18-b063-312c8c6fcc7a.png)
![image](https://user-images.githubusercontent.com/112334401/191661007-959b0c07-be2c-4ebc-8986-8e06c7a2c472.png)
![image](https://user-images.githubusercontent.com/112334401/191661092-4a189133-f616-4b23-9c21-5bbe6733f9ed.png)

