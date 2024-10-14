# MiniProject2


![cesa minipro 2 drawio](https://github.com/user-attachments/assets/0e6b79aa-ad10-4ef9-91c4-ae93d8dac916)









1. Import Library
   
   from prettytable import PrettyTable

PrettyTable digunakan untuk menampilkan data dalam bentuk tabel yang rapi di konsol.


2. Inisialisasi Data

pengaduan = []
users = {}
admins = {"cesa": "554"}  # Admin default

pengaduan: List untuk menyimpan semua pengaduan yang diajukan.
users: Dictionary untuk menyimpan username dan password user.
admins: Dictionary untuk menyimpan username dan password admin.

3. Menu Utama

   def menu():
    ...
Menampilkan menu utama dan mengarahkan pengguna berdasarkan pilihan mereka.


4. Fungsi Mendaftar User

   def daftar_user():
    ...
   
   Menerima input username dan password untuk pendaftaran. Jika username sudah ada, akan menampilkan pesan bahwa username sudah terdaftar.


5. Fungsi Login Admin

   def login_admin():
    ...

Menerima input username dan password admin. Jika valid, mengarahkan ke menu admin.


6. Fungsi Login User

   def login_user():
    ...
   
Menerima input username dan password user. Jika valid, mengarahkan ke menu user.


7. Fungsi Membuat Pengaduan
   
   def buat_pengaduan(username):
    ...

Menerima pengaduan dari user dan menambahkannya ke list pengaduan.


8. Fungsi Melihat Semua Pengaduan (Admin)

   def lihat_pengaduan():
    ...

Menampilkan semua pengaduan dalam bentuk tabel. Jika tidak ada pengaduan, akan memberi tahu pengguna.


9. Melihat Pengaduan User Tertentu

    def lihat_pengaduan_user(username):
    ...

Menampilkan pengaduan yang dibuat oleh user tertentu.


10. Mengubah Pengaduan oleh User

    def ubah_pengaduan(username):
    ...

  User dapat memilih pengaduan yang ingin diubah berdasarkan nomor. Mengubah pengaduan jika nomor valid.


11. Mengubah Pengaduan oleh Admin

    def ubah_pengaduan_admin():
    ...

    Admin dapat mengubah pengaduan yang ada.


12. Menghapus Pengaduan (Admin)

  def hapus_pengaduan():
    ...

Admin dapat menghapus pengaduan berdasarkan nomor.


13. Menambah Admin Baru

def tambah_admin_baru():
    ...

Admin dapat menambah admin baru dengan username dan password.


14. Menu untuk User

 def menu_user(username):
    ...
    
Menyediakan opsi untuk user: membuat pengaduan, melihat pengaduan mereka, mengubah pengaduan, dan keluar.


15. Menu untuk Admin    

def menu_admin():
    ...
    
Menyediakan opsi untuk admin: melihat semua pengaduan, menghapus pengaduan, mengubah pengaduan, menambah admin baru, dan keluar.
    

16. Inisialisasi dan Jalankan Aplikasi

    menu()

Menjalankan fungsi menu() yang memulai aplikasi.

