from prettytable import PrettyTable

# List untuk menyimpan data pengaduan dan users
pengaduan = []
users = {}
admins = {"cesa": "554"}  # Admin default

def menu():
    while True:
        print("\n=== Menu Utama ===")
        print("1. Login sebagai Admin")
        print("2. Login sebagai User")
        print("3. Daftar User Baru")
        print("4. Keluar")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            login_admin()
        elif pilihan == '2':
            login_user()
        elif pilihan == '3':
            daftar_user()
        elif pilihan == '4':
            print("Terima kasih telah melakukan pengaduan.")
            break
        else:
            print("Pilihan tidak valid.")

# Fungsi untuk mendaftar user baru
def daftar_user():
    username = input("Masukkan username baru: ")
    if username in users:
        print("Username sudah terdaftar.")
    else:
        password = input("Masukkan password: ")
        users[username] = password
        print("User berhasil terdaftar.")

# Fungsi untuk login admin
def login_admin():
    username = input("Masukkan username admin: ")
    password = input("Masukkan password admin: ")

    if username in admins and admins[username] == password:
        print(f"Selamat datang, Admin {username}.")
        menu_admin()
    else:
        print("Username atau password salah.")

# Fungsi untuk login user
def login_user():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username in users and users[username] == password:
        print(f"Selamat datang, {username}.")
        menu_user(username)
    else:
        print("Username atau password salah.")

# Fungsi untuk membuat pengaduan
def buat_pengaduan(username):
    aduan = input("Masukkan pengaduan Anda: ")
    pengaduan.append({"user": username, "aduan": aduan})
    print("Pengaduan berhasil dikirim.")

# Fungsi untuk melihat semua pengaduan (admin)
def lihat_pengaduan():
    table = PrettyTable()
    table.field_names = ["No", "User", "Pengaduan"]

    if not pengaduan:
        print("Belum ada pengaduan.")
    else:
        for idx, aduan in enumerate(pengaduan, 1):
            table.add_row([idx, aduan['user'], aduan['aduan']])
        print(table)

# Fungsi untuk melihat pengaduan user tertentu
def lihat_pengaduan_user(username):
    pengaduan_user = [aduan for aduan in pengaduan if aduan['user'] == username]
    table = PrettyTable()
    table.field_names = ["No", "Pengaduan"]

    if not pengaduan_user:
        print("Anda belum membuat pengaduan.")
    else:
        for idx, aduan in enumerate(pengaduan_user, 1):
            table.add_row([idx, aduan['aduan']])
        print(table)

# Fungsi untuk mengubah pengaduan oleh user
def ubah_pengaduan(username):
    lihat_pengaduan_user(username)
    pengaduan_user = [aduan for aduan in pengaduan if aduan['user'] == username]

    if pengaduan_user:
        nomor = int(input("Masukkan nomor pengaduan yang ingin diubah: ")) - 1
        if 0 <= nomor < len(pengaduan_user):
            pengaduan_baru = input("Masukkan pengaduan baru: ")
            pengaduan[nomor]['aduan'] = pengaduan_baru
            print("Pengaduan berhasil diubah.")
        else:
            print("Nomor pengaduan tidak valid atau Anda tidak berhak mengubah pengaduan ini.")

# Fungsi untuk mengubah pengaduan oleh admin
def ubah_pengaduan_admin():
    lihat_pengaduan()
    if pengaduan:
        nomor = int(input("Masukkan nomor pengaduan yang ingin diubah: ")) - 1
        if 0 <= nomor < len(pengaduan):
            pengaduan_baru = input("Masukkan pengaduan baru: ")
            pengaduan[nomor]['aduan'] = pengaduan_baru
            print("Pengaduan berhasil diubah.")
        else:
            print("Nomor pengaduan tidak valid.")

# Fungsi untuk menghapus pengaduan (admin)
def hapus_pengaduan():
    lihat_pengaduan()
    if pengaduan:
        nomor = int(input("Masukkan nomor pengaduan yang ingin dihapus: ")) - 1
        if 0 <= nomor < len(pengaduan):
            del pengaduan[nomor]
            print("Pengaduan berhasil dihapus.")
        else:
            print("Nomor pengaduan tidak valid.")

# Fungsi untuk menambah admin baru
def tambah_admin_baru():
    print("\n=== Tambah Admin Baru ===")
    new_admin_username = input("Masukkan username admin baru: ")
    if new_admin_username in admins:
        print("Admin dengan username tersebut sudah ada.")
    else:
        new_admin_password = input("Masukkan password untuk admin baru: ")
        admins[new_admin_username] = new_admin_password
        print(f"Admin baru {new_admin_username} berhasil ditambahkan.")

# Menu untuk User
def menu_user(username):
    while True:
        print("\n=== Menu User ===")
        print("1. Buat Pengaduan")
        print("2. Lihat Pengaduan Saya")
        print("3. Ubah Pengaduan Saya")
        print("4. Keluar")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            buat_pengaduan(username)
        elif pilihan == '2':
            lihat_pengaduan_user(username)
        elif pilihan == '3':
            ubah_pengaduan(username)
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid.")

# Menu untuk Admin
def menu_admin():
    while True:
        print("\n=== Menu Admin ===")
        print("1. Lihat Semua Pengaduan")
        print("2. Hapus Pengaduan")
        print("3. Ubah Pengaduan")
        print("4. Tambah Admin Baru")
        print("5. Keluar")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            lihat_pengaduan()
        elif pilihan == '2':
            hapus_pengaduan()
        elif pilihan == '3':
            ubah_pengaduan_admin()
        elif pilihan == '4':
            tambah_admin_baru()
        elif pilihan == '5':
            break
        else:
            print("Pilihan tidak valid.")

# Inisialisasi dan jalankan aplikasi
menu()