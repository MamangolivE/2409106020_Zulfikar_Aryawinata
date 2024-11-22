import re
import os
import locale
from datetime import datetime
locale.setlocale(locale.LC_TIME, 'id_ID.UTF-8')
waktu = datetime.now()
hari = waktu.strftime("%A")
tanggal = waktu.strftime("%d-%m-%Y")

admin = {"admin":"admin"}
lomba_solo = ["Network","Ranking 1"]
lomba_tim = ["Robotik","UI/UX","Mobile Legends","Valorant"]
users = {}
pendaftar_network = {}
pendaftar_ranking1 = {}
pendaftar_robotik = {}
pendaftar_uiux = {}
pendaftar_mobilelegends = {}
pendaftar_valorant = {}
perlombaan = {
    "Network": pendaftar_network,
    "Ranking 1": pendaftar_ranking1,
    "Robotik": pendaftar_robotik,
    "UI/UX": pendaftar_uiux,
    "Mobile Legends": pendaftar_mobilelegends,
    "Valorant": pendaftar_valorant,
}
credit = ("Ken Bilqis Nuraini",2409106015,"Renaya Putri Alika",2409106002,"Zulfikar Aryawinata",2409106020)

# tampilan data tersimpan
def data_tersimpan():
    print('''
===================
Data Telah Disimpan
===================''')

# tampilan mengisi data
def silahkan_isi_data():
    print('''
==============================
Silahkan Isi Data yang diminta
==============================''')

# Fungsi untuk menampilkan lomba
def menampilkan_lomba_admin():
    print("""
    _______________________________________________
    |---------------------------------------------|
    |Lomba:                                       |
    |      1> Network          4> UI/UX           |
    |      2> Ranking 1        5> Mobile Legends  |
    |      3> Robotik          6> Valorant        |
    |_____________________________________________|
    """)

# tampilan menu admin
def menu_admin():
    print("""______________________________
|============================|
|1> Tampilkan Data Pendaftar |
|2> Ubah Data Pendaftar      |
|3> Tampilkan Akun Users     |
|4> Hapus Data Pendaftar     |
|5> Kembali                  |
|____________________________|
""")

# tampilan peserta lomba
def menampilkan_lomba_peserta():
    print(f"""
    =====================================================================
    |                             LOMBA                                 |
    =====================================================================
    |          Perorangan           |               Tim                 |
    |_______________________________|___________________________________|
    |                               |        3> {lomba_tim[0]}                 |
    |      1> {lomba_solo[0]}               |        4> {lomba_tim[1]}                   |
    |      2> {lomba_solo[1]}             |        5> {lomba_tim[2]}          |
    |                               |        6> {lomba_tim[3]}                |
    =====================================================================""")

# fungsi untuk menampilkan data lomba individu
def menampilkan_data_pendaftar(nama_lomba):
    if not nama_lomba:
        print('''
----------------------------------
 Belum ada peserta yang mendaftar
----------------------------------''')
    else:
        for akun, data in nama_lomba.items():
            print(f"""{"="*55}
            Akun : {akun}
                Nama     : {data["Nama"]}
                NIM      : {data["NIM"]}
                Prodi    : {data["Prodi"]}
                Instansi : {data["Instansi"]}
            Mendaftar pada Hari {data["Hari"]}, tanggal {data["Tanggal"]}.
        """)

# menampilkan data lomba bertim
def menampilkan_data_pendaftar_tim(nama_lomba):
    if not nama_lomba:
        print('''
----------------------------------
 Belum ada peserta yang mendaftar
----------------------------------''')
    else:
        for akun, data in nama_lomba.items():
            print(f"""{"="*55}
            Akun : {akun}
                Nama Tim : {data["Nama Tim"]}
                Anggota  : {data["Anggota"]}
                Prodi    : {data["Prodi"]}
                Instansi : {data["Instansi"]}
            Mendaftar pada Hari {data["Hari"]}, tanggal {data["Tanggal"]}.
        """)


# fungsi menginput nama peserta individu
def input_nama_peserta():
    while True:
        nama = input("\nNama : ")
        if re.fullmatch(r"[A-Za-z ]+", nama):
            return nama
        else:
            print("\nNama Harus Berupa Huruf.")

# mengecek nim
def cek_nim(nim, data_pendaftar):
    for username, data in data_pendaftar.items():
        if data["NIM"] == nim:
            return True
    return False

# fungsi memasukkan data ke dalam dictionary
def masukkan_data(data, username, nama, nim, prodi, instansi):
    data[username]={
        "Nama":nama,
        "NIM":nim,
        "Prodi":prodi,
        "Instansi":instansi,
        "Hari":hari,"Tanggal":tanggal
        }

# Fungsi Mendaftar Akun User
def registrasi():
    while True:
        username = input("\nMasukkan username yang ingin dipakai : ")
        password = input("Password : ")
        # Kondisi ketika username yang dimasukkan sudah ada dalam data akun user
        if username in users:
            print("username sudah dipakai")
        # Kondisi Ketika berhasil mendaftar akun user
        elif len(username) >= 4 and username.isalpha() and len(password) >= 4:
            users[username]=password
            print("username dan password telah disimpan")
            break
        # Kondisi Ketika gagal mendaftar akun user
        else:
            print("""username/password tidak valid 
(username dan password Minimal 4 Huruf dan username Terdiri Dari Huruf)""")

# Fungsi Login Sebagai User
def login_user():
    try:
        hitung = 0
        while (hitung < 3):
            hitung += 1
            username = input("\nusername : ")
            password = input("Password : ")
            # berhasil login sebagai user
            if username in users and users[username] == password:
                print(f"\n\n\nSELAMAT DATANG :^)")
                while True:
                    print(f"""
    \n1> Tampilkan Lomba
2> Daftar
3> Kembali
    """)
                    pilihan = int(input("\nMasukkan Pilihan (1/2/3): "))
                    # Menampilkan daftar lomba
                    if pilihan == 1:
                        menampilkan_lomba_peserta()
                    # User mendaftar pada lomba yang ada
                    elif pilihan == 2:
                        while True:
                            menampilkan_lomba_peserta()
                            print("""
    0> Keluar""")
                            lomba = int(input("\nLomba (1/2/3/4/5/6/0) : "))
                            # Mendaftar lomba Network
                            if lomba == 1:
                                def input_nim():
                                    while True:
                                        nim = input("\nMasukkan NIM (isi dengan 0 jika tidak memiliki NIM) : ")
                                        if nim == "0":
                                            return nim
                                        elif nim.isdigit() and len(nim) >= 10:
                                            return nim
                                        elif nim.isalpha():
                                            print("NIM Harus Berupa Angka")
                                            continue
                                        else:
                                            print("NIM Harus 10 Angka atau lebih")
                                            continue
                                #Input Data
                                hitung = 0
                                silahkan_isi_data()
                                while True:
                                    nama = input_nama_peserta()
                                    if len(nama) < 4:
                                        print("Nama Harus 4 Huruf atau Lebih")
                                        continue
                                    else:
                                        nim = input_nim()
                                        if cek_nim(nim, pendaftar_network):
                                            print("Maaf NIM sudah terdaftar! Pendaftaran gagal")
                                            break
                                        else:
                                            while True:
                                                prodi = input("\nAsal Prodi (isi dengan (-) jika tidak di prodi manapun): ")
                                                if len(prodi) >= 5 or prodi == "-":
                                                    if re.fullmatch(r"[A-Za-z -]+", prodi):
                                                        while True:
                                                            instansi = input("\nAsal Instansi: ")
                                                            if re.fullmatch(r"[A-Za-z -]+", instansi) and len(instansi) >= 3:
                                                                masukkan_data(pendaftar_network, username, nama, nim, prodi, instansi)
                                                                data_tersimpan()
                                                                break
                                                            else:
                                                                print("Instansi Harus Berupa Huruf dan Tidak kurang dari 3")
                                                                continue
                                                    else:
                                                        print("Prodi Harus Berupa Huruf")
                                                        continue
                                                    break
                                                elif not re.fullmatch(r"[A-Za-z ]+", prodi) and len(prodi) >= 5:
                                                    print("Prodi Harus Berupa Huruf")
                                                    continue
                                                elif prodi.isdigit():
                                                    print("Prodi Harus Berupa Huruf")
                                                    continue
                                                else:
                                                    print("Nama Prodi Harus Lengkap")
                                                    continue
                                    break
                            # Mendaftar lomba Ranking 1
                            elif lomba == 2:
                                def input_nim():
                                    while True:
                                        nim = input("\nMasukkan NIM (isi dengan 0 jika tidak memiliki NIM) : ")
                                        if nim == "0":
                                            return nim
                                        elif nim.isdigit() and len(nim) >= 10:
                                            return nim
                                        elif nim.isalpha():
                                            print("NIM Harus Berupa Angka")
                                            continue
                                        else:
                                            print("NIM Harus 10 Angka atau lebih")
                                            continue
                                #Input Data
                                hitung = 0
                                silahkan_isi_data()
                                while True:
                                    nama = input_nama_peserta()
                                    if len(nama) < 4:
                                        print("Nama Harus 4 Huruf Atau Lebih")
                                        continue
                                    else:
                                        nim = input_nim()
                                        if cek_nim(nim, pendaftar_ranking1):
                                            print("Maaf NIM sudah terdaftar! Pendaftaran gagal")
                                            break
                                        else:
                                            while True:
                                                prodi = input("\nAsal Prodi (isi dengan (-) jika tidak di prodi manapun): ")
                                                if len(prodi) >= 5 or prodi == "-":
                                                    if re.fullmatch(r"[A-Za-z -]+", prodi):
                                                        while True:
                                                            instansi = input("\nAsal Instansi: ")
                                                            if re.fullmatch(r"[A-Za-z -]+", instansi) and len(instansi) >= 3:
                                                                masukkan_data(pendaftar_ranking1, username, nama, nim, prodi, instansi)
                                                                data_tersimpan()
                                                                break
                                                            else:
                                                                print("Instansi Harus Berupa Huruf dan Tidak kurang dari 3")
                                                                continue
                                                    else:
                                                        print("Prodi Harus Berupa Huruf")
                                                        continue
                                                    break
                                                elif not re.fullmatch(r"[A-Za-z ]+", prodi) and len(prodi) >= 5:
                                                    print("Prodi Harus Berupa Huruf")
                                                    continue
                                                elif prodi.isdigit():
                                                    print("Prodi Harus Berupa Huruf")
                                                    continue
                                                else:
                                                    print("Nama Prodi Harus Lengkap")
                                                    continue
                                    break
                            # Mendaftar lomba Robotik
                            elif lomba == 3:
                                def input_nama_anggota(anggota_ke):
                                    while True:
                                        nama = input(f"\nNama Anggota {anggota_ke}: ")
                                        if re.fullmatch(r"[A-Za-z ]+", nama):
                                            if len(nama) >= 4:
                                                return nama
                                            else:
                                                print("Nama Harus 4 Huruf Atau Lebih")
                                                continue
                                        else:
                                            print("Nama hanya boleh terdiri dari huruf")
                                            continue
                                def input_nim(anggota_ke):
                                    while True:
                                        nim = input(f"\nMasukkan NIM Anggota {anggota_ke} (isi dengan 0 jika tidak memiliki NIM): ")
                                        if nim == "0":
                                            return nim
                                        elif nim.isdigit() and len(nim) >= 10:
                                            return nim
                                        elif nim.isalpha():
                                            print("NIM Harus Berupa Angka")
                                            continue
                                        else:
                                            print("NIM Harus 10 Angka atau lebih")
                                            continue
                                # Input data
                                silahkan_isi_data()
                                while True:
                                    nama_tim = input("\nApa Nama Tim Anda: ")
                                    if  len(nama_tim) < 4:
                                        print("Nama Tim Minimal 4 Huruf")
                                        continue
                                    else:
                                        anggota1 = input_nama_anggota(1)
                                        nim1 = input_nim(1)
                                        if cek_nim(nim1, pendaftar_robotik):
                                            print("Maaf NIM sudah terdaftar! Pendaftaran gagal")
                                            break
                                        else:
                                            anggota2 = input_nama_anggota(2)
                                            while True:
                                                nim2 = input_nim(2)
                                                if cek_nim(nim2, pendaftar_robotik):
                                                    print("Maaf NIM sudah terdaftar! Pendaftaran gagal")
                                                    break
                                                elif nim1 == nim2:
                                                    print("Maaf NIM tidak bisa sama")
                                                    continue
                                                else:
                                                    anggota3 = input_nama_anggota(3)
                                                    while True:
                                                        nim3 = input_nim(3)
                                                        if cek_nim(nim3, pendaftar_robotik):
                                                            print("Maaf NIM sudah terdaftar! Pendaftaran gagal")
                                                            break
                                                        elif nim1 == nim3 or nim2 == nim3:
                                                            print("Maaf NIM tidak bisa sama")
                                                            continue
                                                        else:
                                                            while True:
                                                                prodi = input("\nAsal Prodi (isi dengan (-) jika tidak di prodi manapun): ")
                                                                if len(prodi) >= 5 or prodi == "-":
                                                                    if re.fullmatch(r"[A-Za-z -]+", prodi):
                                                                        while True:
                                                                            instansi = input("\nAsal Instansi: ")
                                                                            if re.fullmatch(r"[A-Za-z -]+", instansi) and len(instansi) >= 3:
                                                                                pendaftar_robotik[username] = {
                                                                                "Nama Tim": nama_tim,
                                                                                "Anggota": {
                                                                                    anggota1:nim1,
                                                                                    anggota2:nim2,
                                                                                    anggota3:nim3},
                                                                                "Prodi": prodi,
                                                                                "Instansi": instansi,
                                                                                "Hari":hari,"Tanggal":tanggal
                                                                                }
                                                                                data_tersimpan()
                                                                                break
                                                                            else:
                                                                                print("Instansi Harus Berupa Huruf dan Tidak kurang dari 3")
                                                                                continue
                                                                    else:
                                                                        print("Prodi Harus Berupa Huruf")
                                                                        continue
                                                                elif not re.fullmatch(r"[A-Za-z ]+", prodi) and len(prodi) >= 5:
                                                                    print("Prodi Harus Berupa Huruf")
                                                                    continue
                                                                elif prodi.isdigit():
                                                                    print("Prodi Harus Berupa Huruf")
                                                                    continue
                                                                else:
                                                                    print("Nama Prodi Harus Lengkap")
                                                                    continue
                                                                break
                                                        break
                                                break
                                    break
                            # Mendaftar lomba UI UX
                            elif lomba == 4:
                                def input_nama_anggota(anggota_ke):
                                    while True:
                                        nama = input(f"\nNama Anggota {anggota_ke}: ")
                                        if re.fullmatch(r"[A-Za-z ]+", nama):
                                            if len(nama) >= 4:
                                                return nama
                                            else:
                                                print("Nama Harus 4 Huruf Atau Lebih")
                                                continue
                                        else:
                                            print("Nama hanya boleh terdiri dari huruf")
                                            continue
                                def input_nim(anggota_ke):
                                    while True:
                                        nim = input(f"\nMasukkan NIM Anggota {anggota_ke} (isi dengan 0 jika tidak memiliki NIM): ")
                                        if nim == "0":
                                            return nim
                                        elif nim.isdigit() and len(nim) >= 10:
                                            return nim
                                        elif nim.isalpha():
                                            print("NIM Harus Berupa Angka")
                                            continue
                                        else:
                                            print("NIM Harus 10 Angka atau lebih")
                                            continue
                                # Input data
                                silahkan_isi_data()
                                while True:
                                    nama_tim = input("\nApa Nama Tim Anda: ")
                                    if  len(nama_tim) < 4:
                                        print("Nama Tim Minimal 4 Huruf")
                                        continue
                                    else:
                                        anggota1 = input_nama_anggota(1)
                                        nim1 = input_nim(1)
                                        if cek_nim(nim1, pendaftar_uiux):
                                            print("Maaf NIM sudah terdaftar! Pendaftaran gagal")
                                            break
                                        else:
                                            anggota2 = input_nama_anggota(2)
                                            while True:
                                                nim2 = input_nim(2)
                                                if cek_nim(nim2, pendaftar_uiux):
                                                    print("Maaf NIM sudah terdaftar! Pendaftaran gagal")
                                                    break
                                                elif nim1 == nim2:
                                                    print("Maaf NIM tidak bisa sama")
                                                    continue
                                                else:
                                                    anggota3 = input_nama_anggota(3)
                                                    while True:
                                                        nim3 = input_nim(3)
                                                        if cek_nim(nim3, pendaftar_uiux):
                                                            print("Maaf NIM sudah terdaftar! Pendaftaran gagal")
                                                            break
                                                        elif nim1 == nim3 or nim2 == nim3:
                                                            print("Maaf NIM tidak bisa sama")
                                                            continue
                                                        else:
                                                            while True:
                                                                prodi = input("\nAsal Prodi (isi dengan (-) jika tidak di prodi manapun): ")
                                                                if len(prodi) >= 5 or prodi == "-":
                                                                    if re.fullmatch(r"[A-Za-z -]+", prodi):
                                                                        while True:
                                                                            instansi = input("\nAsal Instansi: ")
                                                                            if re.fullmatch(r"[A-Za-z -]+", instansi) and len(instansi) >= 3:
                                                                                pendaftar_uiux[username] = {
                                                                                "Nama Tim": nama_tim,
                                                                                "Anggota": {
                                                                                    anggota1:nim1,
                                                                                    anggota2:nim2,
                                                                                    anggota3:nim3},
                                                                                "Prodi": prodi,
                                                                                "Instansi": instansi,
                                                                                "Hari":hari,"Tanggal":tanggal
                                                                                }
                                                                                data_tersimpan()
                                                                                break
                                                                            else:
                                                                                print("Instansi Harus Berupa Huruf dan Tidak kurang dari 3")
                                                                                continue
                                                                    else:
                                                                        print("Prodi Harus Berupa Huruf")
                                                                        continue
                                                                elif not re.fullmatch(r"[A-Za-z ]+", prodi) and len(prodi) >= 5:
                                                                    print("Prodi Harus Berupa Huruf")
                                                                    continue
                                                                elif prodi.isdigit():
                                                                    print("Prodi Harus Berupa Huruf")
                                                                    continue
                                                                else:
                                                                    print("Nama Prodi Harus Lengkap")
                                                                    continue
                                                                break
                                                        break
                                                break
                                    break
                            # Mendaftar lomba ML
                            elif lomba == 5:
                                def input_nama_anggota(anggota_ke):
                                    while True:
                                        nama = input(f"\nNama Anggota {anggota_ke}: ")
                                        if re.fullmatch(r"[A-Za-z ]+", nama):
                                            if len(nama) >= 4:
                                                return nama
                                            else:
                                                print("Nama Harus 4 Huruf Atau Lebih")
                                                continue
                                        else:
                                            print("Nama hanya boleh terdiri dari huruf")
                                            continue
                                def input_nim(anggota_ke):
                                    while True:
                                        nim = input(f"\nMasukkan NIM Anggota {anggota_ke} (isi dengan 0 jika tidak memiliki NIM): ")
                                        if nim == "0":
                                            return nim
                                        elif nim.isdigit() and len(nim) >= 10:
                                            return nim
                                        elif nim.isalpha():
                                            print("NIM Harus Berupa Angka")
                                            continue
                                        else:
                                            print("NIM Harus 10 Angka atau lebih")
                                            continue
                                # Input data
                                silahkan_isi_data
                                while True:
                                    nama_tim = input("Apa Nama Tim Anda: ")
                                    if  len(nama_tim) < 4:
                                        print("Nama Tim Minimal 4 Huruf")
                                        continue
                                    else:
                                        anggota1 = input_nama_anggota(1)
                                        nim1 = input_nim(1)
                                        if cek_nim(nim1, pendaftar_mobilelegends):
                                            print("Maaf NIM sudah terdaftar! Pendaftaran gagal")
                                            break
                                        else:
                                            anggota2 = input_nama_anggota(2)
                                            while True:
                                                nim2 = input_nim(2)
                                                if cek_nim(nim2, pendaftar_mobilelegends):
                                                    print("Maaf NIM sudah terdaftar! Pendaftaran gagal")
                                                    break
                                                elif nim1 == nim2:
                                                    print("Maaf NIM tidak bisa sama")
                                                    continue
                                                else:
                                                    anggota3 = input_nama_anggota(3)
                                                    while True:
                                                        nim3 = input_nim(3)
                                                        if cek_nim(nim3, pendaftar_mobilelegends):
                                                            print("Maaf NIM sudah terdaftar! Pendaftaran gagal")
                                                            break
                                                        elif nim1 == nim3 or nim2 == nim3:
                                                            print("Maaf NIM tidak bisa sama")
                                                            continue
                                                        else:
                                                            anggota4 = input_nama_anggota(4)
                                                            while True:
                                                                nim4 = input_nim(4)
                                                                if cek_nim(nim4, pendaftar_mobilelegends):
                                                                    print("Maaf NIM sudah terdaftar! Pendaftaran gagal")
                                                                    break
                                                                elif nim4 == nim1 or nim4 == nim2 or nim4 == nim3:
                                                                    print("Maaf NIM tidak bisa sama")
                                                                    continue
                                                                else:
                                                                    anggota5 = input_nama_anggota(5)
                                                                    while True:
                                                                        nim5 = input_nim(5)
                                                                        if cek_nim(nim5, pendaftar_mobilelegends):
                                                                            print("Maaf NIM sudah terdaftar! Pendaftaran gagal")
                                                                            break
                                                                        elif nim5 == nim1 or nim5 == nim2 or nim5 == nim3 or nim5 == nim4:
                                                                            print("Maaf NIM tidak bisa sama")
                                                                            continue
                                                                        else:
                                                                            while True:
                                                                                prodi = input("\nAsal Prodi (isi dengan (-) jika tidak di prodi manapun): ")
                                                                                if len(prodi) >= 5 or prodi == "-":
                                                                                    if re.fullmatch(r"[A-Za-z -]+", prodi):
                                                                                        while True:
                                                                                            instansi = input("\nAsal Instansi: ")
                                                                                            if re.fullmatch(r"[A-Za-z -]+", instansi) and len(instansi) >= 3:
                                                                                                pendaftar_mobilelegends[username] = {
                                                                                                "Nama Tim": nama_tim,
                                                                                                "Anggota": {
                                                                                                    anggota1:nim1,
                                                                                                    anggota2:nim2,
                                                                                                    anggota3:nim3,
                                                                                                    anggota4:nim4,
                                                                                                    anggota5:nim5},
                                                                                                "Prodi": prodi,
                                                                                                "Instansi": instansi,
                                                                                                "Hari":hari,"Tanggal":tanggal
                                                                                                }
                                                                                                data_tersimpan()
                                                                                                break
                                                                                            else:
                                                                                                print("Instansi Harus Berupa Huruf dan Tidak kurang dari 3")
                                                                                                continue
                                                                                    else:
                                                                                        print("Prodi Harus Berupa Huruf")
                                                                                        continue
                                                                                elif not re.fullmatch(r"[A-Za-z ]+", prodi) and len(prodi) >= 5:
                                                                                    print("Prodi Harus Berupa Huruf")
                                                                                    continue
                                                                                elif prodi.isdigit():
                                                                                    print("Prodi Harus Berupa Huruf")
                                                                                    continue
                                                                                else:
                                                                                    print("Nama Prodi Harus Lengkap")
                                                                                    continue
                                                                                break
                                                                        break
                                                                break
                                                        break
                                                break
                                    break
                            # Mendaftar lomba Valorant
                            elif lomba == 6:
                                def input_nama_anggota(anggota_ke):
                                    while True:
                                        nama = input(f"\nNama Anggota {anggota_ke}: ")
                                        if re.fullmatch(r"[A-Za-z ]+", nama):
                                            if len(nama) >= 4:
                                                return nama
                                            else:
                                                print("Nama Harus 4 Huruf Atau Lebih")
                                                continue
                                        else:
                                            print("Nama hanya boleh terdiri dari huruf")
                                            continue
                                def input_nim(anggota_ke):
                                    while True:
                                        nim = input(f"\nMasukkan NIM Anggota {anggota_ke} (isi dengan 0 jika tidak memiliki NIM): ")
                                        if nim == "0":
                                            return nim
                                        elif nim.isdigit() and len(nim) >= 10:
                                            return nim
                                        elif nim.isalpha():
                                            print("NIM Harus Berupa Angka")
                                            continue
                                        else:
                                            print("NIM Harus 10 Angka atau lebih")
                                            continue
                                # Input data
                                silahkan_isi_data
                                while True:
                                    nama_tim = input("Apa Nama Tim Anda: ")
                                    if  len(nama_tim) < 4:
                                        print("Nama Tim Minimal 4 Huruf")
                                        continue
                                    else:
                                        anggota1 = input_nama_anggota(1)
                                        nim1 = input_nim(1)
                                        if cek_nim(nim1, pendaftar_valorant):
                                            print("Maaf NIM sudah terdaftar! Pendaftaran gagal")
                                            break
                                        else:
                                            anggota2 = input_nama_anggota(2)
                                            while True:
                                                nim2 = input_nim(2)
                                                if cek_nim(nim2, pendaftar_valorant):
                                                    print("Maaf NIM sudah terdaftar! Pendaftaran gagal")
                                                    break
                                                elif nim1 == nim2:
                                                    print("Maaf NIM tidak bisa sama")
                                                    continue
                                                else:
                                                    anggota3 = input_nama_anggota(3)
                                                    while True:
                                                        nim3 = input_nim(3)
                                                        if cek_nim(nim3, pendaftar_valorant):
                                                            print("Maaf NIM sudah terdaftar! Pendaftaran gagal")
                                                            break
                                                        elif nim1 == nim3 or nim2 == nim3:
                                                            print("Maaf NIM tidak bisa sama")
                                                            continue
                                                        else:
                                                            anggota4 = input_nama_anggota(4)
                                                            while True:
                                                                nim4 = input_nim(4)
                                                                if cek_nim(nim4, pendaftar_valorant):
                                                                    print("Maaf NIM sudah terdaftar! Pendaftaran gagal")
                                                                    break
                                                                elif nim4 == nim1 or nim4 == nim2 or nim4 == nim3:
                                                                    print("Maaf NIM tidak bisa sama")
                                                                    continue
                                                                else:
                                                                    anggota5 = input_nama_anggota(5)
                                                                    while True:
                                                                        nim5 = input_nim(5)
                                                                        if cek_nim(nim5, pendaftar_valorant):
                                                                            print("Maaf NIM sudah terdaftar! Pendaftaran gagal")
                                                                            break
                                                                        elif nim5 == nim1 or nim5 == nim2 or nim5 == nim3 or nim5 == nim4:
                                                                            print("Maaf NIM tidak bisa sama")
                                                                            continue
                                                                        else:
                                                                            while True:
                                                                                prodi = input("\nAsal Prodi (isi dengan (-) jika tidak di prodi manapun): ")
                                                                                if len(prodi) >= 5 or prodi == "-":
                                                                                    if re.fullmatch(r"[A-Za-z -]+", prodi):
                                                                                        while True:
                                                                                            instansi = input("\nAsal Instansi: ")
                                                                                            if re.fullmatch(r"[A-Za-z -]+", instansi) and len(instansi) >= 3:
                                                                                                pendaftar_valorant[username] = {
                                                                                                "Nama Tim": nama_tim,
                                                                                                "Anggota": {
                                                                                                    anggota1:nim1,
                                                                                                    anggota2:nim2,
                                                                                                    anggota3:nim3,
                                                                                                    anggota4:nim4,
                                                                                                    anggota5:nim5},
                                                                                                "Prodi": prodi,
                                                                                                "Instansi": instansi,
                                                                                                "Hari":hari,"Tanggal":tanggal
                                                                                                }
                                                                                                data_tersimpan()
                                                                                                break
                                                                                            else:
                                                                                                print("Instansi Harus Berupa Huruf dan Tidak kurang dari 3")
                                                                                                continue
                                                                                    else:
                                                                                        print("Prodi Harus Berupa Huruf")
                                                                                        continue
                                                                                elif not re.fullmatch(r"[A-Za-z ]+", prodi) and len(prodi) >= 5:
                                                                                    print("Prodi Harus Berupa Huruf")
                                                                                    continue
                                                                                elif prodi.isdigit():
                                                                                    print("Prodi Harus Berupa Huruf")
                                                                                    continue
                                                                                else:
                                                                                    print("Nama Prodi Harus Lengkap")
                                                                                    continue
                                                                                break
                                                                        break
                                                                break
                                                        break
                                                break
                                    break
                            elif lomba == 0:
                                break
                            # Eror handling ketika lomba yang dimasukkan tidak sesuai
                            else:
                                print("\nlomba tidak valid")
                    # Kembali ke menu sebelumnya
                    elif pilihan == 3:
                        return False
                    # Eror handling ketika memasukkan pilihan yang tidak sesuai
                    else:
                        print("\nPILIHAN TIDAK VALID")
            # Gagal login sebagai user
            else:
                print("\n\nusername/password salah")
                if hitung == 3:
                    print("\nsilahkan coba lagi nanti")
                    break
    # Eror handling try except
    except ValueError:
        print("\n!!!Maaf anda salah memasukan tipe data!!!")
    except SyntaxError:
        print("\n!!!Maaf ada kesalahan penulisan syntax sehingga terjadi error!!!")
    except IndexError:
        print("\n!!!Maaf ada kesalahan penulisan index sehingga terjadi error!!!")
    except AssertionError:
        print("\n!!!Maaf syarat tidak terpenuhi sehingga terjadi error!!!")
    except AttributeError:
        print("\n!!!Maaf ada kesalahan penulisan attribute sehingga terjadi error!!!")
    except ImportError:
        print("\n!!!Maaf gagal mengimport sehingga terjadi error!!!")
    except KeyError:
        print("\n!!!Maaf key tidak ditemukan sehingga terjadi error!!!")
    except NameError:
        print("\n!!!Maaf variabel belum didefinisikan sehingga terjadi error!!!")
    except MemoryError:
        print("\n!!!Maaf memory tidak cukup sehingga terjadi error!!!")
    except TypeError:
        print("\n!!!Maaf ada kesalahan penggunaan sehingga terjadi error!!!")
    except IndentationError:
        print("\n!!!Maaf ada kesalahan indentasi sehingga terjadi error!!!")
    except FileNotFoundError:
        print("\n!!!Maaf file tidak ditemukan sehingga terjadi error!!!")

# Fungsi login sebagai admin
def login_admin():
    # Eror Handling try except
    try:
        hitung = 0
        while (hitung < 3):
            hitung += 1
            username = input("\nMasukkan username : ")
            password = input("Password : ")
            # Berhasil login sebagai admin
            if username in admin and password == admin[username]:
                print("\n SELAMAT DATANG DI MENU ADMIN")
                while True:
                    menu_admin()
                    pilihan = int(input("Masukkan Pilihan Anda (1/2/3/4/5) : "))
                    # Menampilkan data pendaftar lomba-lomba yang ada
                    if pilihan == 1:
                        menampilkan_lomba_admin()
                        nama_lomba = int(input("Pilih lomba yang ingin dilihat [1/2/3/4/5/6] : "))
                        # Menampilkan data pendaftar lomba Network
                        if nama_lomba == 1:
                            print(f"\n{"="*55}\nPENDAFTAR LOMBA NETWORK")
                            menampilkan_data_pendaftar(pendaftar_network)
                            input("Tekan enter untuk melanjutan...")
                        # Menampilkan data pendaftar lomba Rangking 1
                        elif nama_lomba == 2:
                            print(f"\n{"="*55}\nPENDAFTAR LOMBA RANKING #1")
                            menampilkan_data_pendaftar(pendaftar_ranking1)
                            input("Tekan enter untuk melanjutan...")
                        # Menampilkan data pendaftar lomba Robotik
                        elif nama_lomba == 3:
                            print(f"\n{"="*55}\nPENDAFTAR LOMBA ROBOTIK")
                            menampilkan_data_pendaftar_tim(pendaftar_robotik)
                            input("Tekan enter untuk melanjutan...")
                        # Menampilkan data pendaftar lomba UI UX
                        elif nama_lomba == 4:
                            print(f"\n{"="*55}\nPENDAFTAR LOMBA UI/UX")
                            menampilkan_data_pendaftar_tim(pendaftar_uiux)
                            input("Tekan enter untuk melanjutan...")
                        # Menampilkan data pendaftar lomba ML
                        elif nama_lomba == 5:
                            print(f"\n{"="*55}\nPENDAFTAR LOMBA MOBILE LEGENDS")
                            menampilkan_data_pendaftar_tim(pendaftar_mobilelegends)
                            input("Tekan enter untuk melanjutan...")
                        # Menampilkan data pendaftar lomba Valorant
                        elif nama_lomba == 6:
                            print(f"\n{"="*55}\nPENDAFTAR LOMBA VALORANT")
                            menampilkan_data_pendaftar_tim(pendaftar_valorant)
                            input("Tekan enter untuk melanjutan...")
                        # Eror handling ketika inputan tidak benar
                        else:
                            print("\nInputan tidak valid")
                    # Mengubah data pendaftar
                    elif pilihan == 2:
                        menampilkan_lomba_admin()
                        lomba = int(input("\nPilih lomba yang ingin diubah [1/2/3/4/5/6] : "))
                        # Mengubah data pendaftar lomba Network
                        if lomba == 1:
                            print(f"\n{"="*55}\nPENDAFTAR LOMBA NETWORK")
                            if not pendaftar_network:
                                print('''
----------------------------------
 Belum ada peserta yang mendaftar
----------------------------------''')
                            else:
                                for akun, data in pendaftar_network.items():
                                    print(f"""{"="*55}
            Akun : {akun}
                Nama     : {data["Nama"]}
                NIM      : {data["NIM"]}
                Prodi    : {data["Prodi"]}
                Instansi : {data["Instansi"]}
            Mendaftar pada Hari {data["Hari"]}, tanggal {data["Tanggal"]}.
        """)
                                nama_ubah = input("Masukkan Nama Pendaftar : ")
                                for user, data in pendaftar_network.items():
                                    if nama_ubah == data["Nama"]:
                                        print("\nPROSES UBAH DATA PENDAFTAR LOMBA NETWORK")
                                        def input_nim():
                                            while True:
                                                nim = input("\nMasukkan NIM (isi dengan 0 jika tidak memiliki NIM) : ")
                                                if nim == "0":
                                                    return nim
                                                elif nim.isdigit() and len(nim) >= 10:
                                                    return nim
                                                elif nim.isalpha():
                                                    print("NIM Harus Berupa Angka")
                                                    continue
                                                else:
                                                    print("NIM Harus 10 Angka atau lebih")
                                                    continue
                                        while True:
                                            nama_update = input_nama_peserta()
                                            if len(nama_update) < 4:
                                                print("Nama Harus 4 Huruf atau Lebih")
                                                continue
                                            else: 
                                                NIM_update = input_nim()
                                                if cek_nim(NIM_update, pendaftar_network):
                                                    print("Maaf NIM sudah terdaftar! Pendaftaran gagal")
                                                    break
                                                else:
                                                    while True:
                                                        prodi_update = input("\nAsal Prodi (isi dengan (-) jika tidak di prodi manapun): ")
                                                        if len(prodi_update) >= 5 or prodi_update == "-":
                                                            if re.fullmatch(r"[A-Za-z -]+", prodi_update):
                                                                while True:
                                                                    instansi_update = input("\nAsal Instansi: ")
                                                                    if re.fullmatch(r"[A-Za-z -]+", instansi_update) and len(instansi_update) >= 3:
                                                                        masukkan_data(pendaftar_network, user, nama_update, NIM_update, prodi_update, instansi_update)
                                                                        data_tersimpan()
                                                                        break
                                                                    else:
                                                                        print("Instansi Harus Berupa Huruf dan Tidak kurang dari 3")
                                                                        continue
                                                            else:
                                                                print("Prodi Harus Berupa Huruf")
                                                                continue
                                                            break
                                                        elif not re.fullmatch(r"[A-Za-z ]+", prodi_update) and len(prodi_update) >= 5:
                                                            print("Prodi Harus Berupa Huruf")
                                                            continue
                                                        elif prodi_update.isdigit():
                                                            print("Prodi Harus Berupa Huruf")
                                                            continue
                                                        else:
                                                            print("Nama Prodi Harus Lengkap")
                                                            continue
                                            break
                                    else:
                                        print("\nNama Tidak Ditemukan")
                        # Mengubah data pendaftar lomba Rangking 1
                        elif lomba == 2:
                            print(f"\n{"="*55}\nPENDAFTAR LOMBA RANKING #1")
                            if not pendaftar_ranking1:
                                print('''
----------------------------------
 Belum ada peserta yang mendaftar
----------------------------------''')
                            else:
                                for akun, data in pendaftar_ranking1.items():
                                    print(f"""{"="*55}
            Akun : {akun}
                Nama     : {data["Nama"]}
                NIM      : {data["NIM"]}
                Prodi    : {data["Prodi"]}
                Instansi : {data["Instansi"]}
            Mendaftar pada Hari {data["Hari"]}, tanggal {data["Tanggal"]}.
        """)
                                nama_ubah = input("Masukkan Nama Pendaftar : ")
                                for user, data in pendaftar_ranking1.items():
                                    if nama_ubah == data["Nama"]:
                                        print("\nPROSES UBAH DATA PENDAFTAR LOMBA RANGKING 1")
                                        def input_nim():
                                            while True:
                                                nim = input("\nMasukkan NIM (isi dengan 0 jika tidak memiliki NIM) : ")
                                                if nim == "0":
                                                    return nim
                                                elif nim.isdigit() and len(nim) >= 10:
                                                    return nim
                                                elif nim.isalpha():
                                                    print("NIM Harus Berupa Angka")
                                                    continue
                                                else:
                                                    print("NIM Harus 10 Angka atau lebih")
                                                    continue
                                        while True:
                                            nama_update = input_nama_peserta()
                                            if len(nama_update) < 4:
                                                print("Nama Harus 4 Huruf atau Lebih")
                                                continue
                                            else: 
                                                NIM_update = input_nim()
                                                if cek_nim(NIM_update, pendaftar_ranking1):
                                                    print("Maaf NIM sudah terdaftar! Pendaftaran gagal")
                                                    break
                                                else:
                                                    while True:
                                                        prodi_update = input("\nAsal Prodi (isi dengan (-) jika tidak di prodi manapun): ")
                                                        if len(prodi_update) >= 5 or prodi_update == "-":
                                                            if re.fullmatch(r"[A-Za-z -]+", prodi_update):
                                                                while True:
                                                                    instansi_update = input("\nAsal Instansi: ")
                                                                    if re.fullmatch(r"[A-Za-z -]+", instansi_update) and len(instansi_update) >= 3:
                                                                        masukkan_data(pendaftar_ranking1, user, nama_update, NIM_update, prodi_update, instansi_update)
                                                                        data_tersimpan()
                                                                        break
                                                                    else:
                                                                        print("Instansi Harus Berupa Huruf dan Tidak kurang dari 3")
                                                                        continue
                                                            else:
                                                                print("Prodi Harus Berupa Huruf")
                                                                continue
                                                            break
                                                        elif not re.fullmatch(r"[A-Za-z ]+", prodi_update) and len(prodi_update) >= 5:
                                                            print("Prodi Harus Berupa Huruf")
                                                            continue
                                                        elif prodi_update.isdigit():
                                                            print("Prodi Harus Berupa Huruf")
                                                            continue
                                                        else:
                                                            print("Nama Prodi Harus Lengkap")
                                                            continue
                                            break
                                    else:
                                        print("\nNama Tidak Ditemukan")
                        # Mengubah data pendaftar lomba Robotik
                        elif lomba == 3:
                            print(f"\n{"="*55}\nPENDAFTAR LOMBA ROBOTIK")
                            for akun, data in pendaftar_robotik.items():
                                print(f"""{"="*55}
        Akun : {akun}
            Nama Tim : {data["Nama Tim"]}
            Anggota  : {data["Anggota"]}
            Prodi    : {data["Prodi"]}
            Instansi : {data["Instansi"]}
        Mendaftar pada Hari {data["Hari"]}, tanggal {data["Tanggal"]}.
    """)
                            nama_ubah = input("Masukkan Nama Tim Pendaftar : ")
                            for user, data in pendaftar_robotik.items():
                                if nama_ubah == data["Nama Tim"]:
                                    print("\nPROSES UBAH DATA PENDAFTAR LOMBA ROBOTIK")
                                    def input_nama_anggota(anggota_ke):
                                        while True:
                                            nama = input(f"\nNama Anggota {anggota_ke}: ")
                                            if re.fullmatch(r"[A-Za-z ]+", nama):
                                                if len(nama) >= 4:
                                                    return nama
                                                else:
                                                    print("Nama Harus 4 Huruf Atau Lebih")
                                                    continue
                                            else:
                                                print("Nama hanya boleh terdiri dari huruf")
                                                continue
                                    def input_nim(anggota_ke):
                                        while True:
                                            nim = input(f"\nMasukkan NIM Anggota {anggota_ke} (isi dengan 0 jika tidak memiliki NIM): ")
                                            if nim == "0":
                                                return nim
                                            elif nim.isdigit() and len(nim) >= 10:
                                                return nim
                                            elif nim.isalpha():
                                                print("NIM Harus Berupa Angka")
                                                continue
                                            else:
                                                print("NIM Harus 10 Angka atau lebih")
                                                continue
                                    while True:
                                        nama_tim_update = input("Apa Nama Tim Anda: ")
                                        if  len(nama_tim_update) < 4:
                                            print("Nama Tim Minimal 4 Huruf")
                                        else:
                                            anggota1_update = input_nama_anggota(1)
                                            NIM1_update = input_nim(1)
                                            anggota2_update = input_nama_anggota(2)
                                            NIM2_update = input_nim(2)
                                            anggota3_update = input_nama_anggota(3)
                                            NIM3_update = input_nim(3)
                                            while True:
                                                prodi_update = input("Asal Prodi (isi dengan (-) jika tidak di prodi manapun): ")
                                                if len(prodi_update) >= 5 or prodi_update == "-":
                                                    instansi_update = input("Masukkan Asal Instansi : ")
                                                    pendaftar_robotik[user] = {
                                                        "Nama Tim":nama_tim_update,
                                                        "Anggota":{
                                                            anggota1_update:NIM1_update,
                                                            anggota2_update:NIM2_update,
                                                            anggota3_update:NIM3_update},
                                                        "Prodi":prodi_update,
                                                        "Instansi":instansi_update,
                                                        "Hari":hari,"Tanggal":tanggal
                                                    }
                                                    data_tersimpan()
                                                    break
                                                else:
                                                    print("Nama Prodi Tidak Valid")
                                                    continue
                                        break
                                else:
                                    print("\nNama Tim Tidak Ditemukan")
                                break
                        # Mengubah data pendaftar lomba UI UX
                        elif lomba == 4:
                            print(f"\n{"="*55}\nPENDAFTAR LOMBA UI/UX")
                            for akun, data in pendaftar_uiux.items():
                                print(f"""{"="*55}
        Akun : {akun}
            Nama Tim : {data["Nama Tim"]}
            Anggota  : {data["Anggota"]}
            Prodi    : {data["Prodi"]}
            Instansi : {data["Instansi"]}
        Mendaftar pada Hari {data["Hari"]}, tanggal {data["Tanggal"]}.
    """)
                            nama_ubah = input("Masukkan Nama Tim Pendaftar : ")
                            for user, data in pendaftar_uiux.items():
                                if nama_ubah == data["Nama Tim"]:
                                    print("\nPROSES UBAH DATA PENDAFTAR LOMBA UI/UX")
                                    def input_nama_anggota(anggota_ke):
                                        while True:
                                            nama = input(f"\nNama Anggota {anggota_ke}: ")
                                            if re.fullmatch(r"[A-Za-z ]+", nama):
                                                if len(nama) >= 4:
                                                    return nama
                                                else:
                                                    print("Nama Harus 4 Huruf Atau Lebih")
                                                    continue
                                            else:
                                                print("Nama hanya boleh terdiri dari huruf")
                                                continue
                                    def input_nim(anggota_ke):
                                        while True:
                                            nim = input(f"\nMasukkan NIM Anggota {anggota_ke} (isi dengan 0 jika tidak memiliki NIM): ")
                                            if nim == "0":
                                                return nim
                                            elif nim.isdigit() and len(nim) >= 10:
                                                return nim
                                            elif nim.isalpha():
                                                print("NIM Harus Berupa Angka")
                                                continue
                                            else:
                                                print("NIM Harus 10 Angka atau lebih")
                                                continue
                                    while True:
                                        nama_tim_update = input("Apa Nama Tim Anda: ")
                                        if  len(nama_tim_update) <= 4:
                                            print("Nama Tim Minimal 4 Huruf")
                                        else:
                                            anggota1_update = input_nama_anggota(1)
                                            NIM1_update = input_nim(1)
                                            anggota2_update = input_nama_anggota(2)
                                            NIM2_update = input_nim(2)
                                            anggota3_update = input_nama_anggota(3)
                                            NIM3_update = input_nim(3)
                                            while True:
                                                prodi_update = input("Asal Prodi (isi dengan (-) jika tidak di prodi manapun): ")
                                                if len(prodi_update) >= 5 or prodi_update == "-":
                                                    instansi_update = input("Masukkan Asal Instansi : ")
                                                    pendaftar_uiux[user] = {
                                                        "Nama Tim":nama_tim_update,
                                                        "Anggota":{
                                                            anggota1_update:NIM1_update,
                                                            anggota2_update:NIM2_update,
                                                            anggota3_update:NIM3_update},
                                                        "Prodi":prodi_update,
                                                        "Instansi":instansi_update,
                                                        "Hari":hari,"Tanggal":tanggal
                                                    }
                                                    data_tersimpan()
                                                    break
                                                else:
                                                    print("Nama Prodi Tidak Valid")
                                                    continue
                                        break
                                else:
                                    print("\nNama Tim Tidak Ditemukan")
                                break
                        # Mengubah data pendaftar lomba ML
                        elif lomba == 5:
                            print(f"\n{"="*55}\nPENDAFTAR LOMBA MOBILE LEGENDS")
                            for akun, data in pendaftar_mobilelegends.items():
                                print(f"""{"="*55}
        Akun : {akun}
            Nama Tim : {data["Nama Tim"]}
            Anggota  : {data["Anggota"]}
            Prodi    : {data["Prodi"]}
            Instansi : {data["Instansi"]}
        Mendaftar pada Hari {data["Hari"]}, tanggal {data["Tanggal"]}.
    """)
                            nama_ubah = input("Masukkan Nama Tim Pendaftar : ")
                            for user, data in pendaftar_mobilelegends.items():
                                if nama_ubah == data["Nama Tim"]:
                                    print("\nPROSES UBAH DATA PENDAFTAR LOMBA MOBILE LEGENDS")
                                    def input_nama_anggota(anggota_ke):
                                        while True:
                                            nama = input(f"\nNama Anggota {anggota_ke}: ")
                                            if re.fullmatch(r"[A-Za-z ]+", nama):
                                                if len(nama) >= 4:
                                                    return nama
                                                else:
                                                    print("Nama Harus 4 Huruf Atau Lebih")
                                                    continue
                                            else:
                                                print("Nama hanya boleh terdiri dari huruf")
                                                continue
                                    def input_nim(anggota_ke):
                                        while True:
                                            nim = input(f"\nMasukkan NIM Anggota {anggota_ke} (isi dengan 0 jika tidak memiliki NIM): ")
                                            if nim == "0":
                                                return nim
                                            elif nim.isdigit() and len(nim) >= 10:
                                                return nim
                                            elif nim.isalpha():
                                                print("NIM Harus Berupa Angka")
                                                continue
                                            else:
                                                print("NIM Harus 10 Angka atau lebih")
                                                continue
                                    while True:
                                        nama_tim = input("Apa Nama Tim Anda: ")
                                        if  len(nama_tim) < 4:
                                            print("Nama Tim Minimal 4 Huruf")
                                        else:
                                            anggota1 = input_nama_anggota(1)
                                            NIM1 = input_nim(1)
                                            anggota2 = input_nama_anggota(2)
                                            NIM2 = input_nim(2)
                                            anggota3 = input_nama_anggota(3)
                                            NIM3 = input_nim(3)
                                            anggota4 = input_nama_anggota(4)
                                            NIM4 = input_nim(4)
                                            anggota5 = input_nama_anggota(5)
                                            NIM5 = input_nim(5)
                                            while True:
                                                prodi = input("Asal Prodi (isi dengan (-) jika tidak di prodi manapun): ")
                                                if len(prodi) >= 5 or prodi == "-":
                                                    instansi = input("Asal Instansi: ")
                                                    pendaftar_mobilelegends[user] = {
                                                        "Nama Tim": nama_tim,
                                                        "Anggota": {
                                                            anggota1:NIM1,
                                                            anggota2:NIM2,
                                                            anggota3:NIM3,
                                                            anggota4:NIM4,
                                                            anggota5:NIM5},
                                                        "Prodi": prodi,
                                                        "Instansi": instansi,
                                                        "Hari":hari,"Tanggal":tanggal
                                                        }
                                                    data_tersimpan()
                                                    break
                                                else:
                                                    print("\nNama Prodi Harus Lengkap")
                                                    continue
                                        break
                                else:
                                    print("\nNama Tim Tidak Ditemukan")
                                break
                        # Mengubah data pendaftar lomba Valorant
                        elif lomba == 6:
                            print(f"\n{"="*55}\nPENDAFTAR LOMBA VALORANT")
                            for akun, data in pendaftar_valorant.items():
                                print(f"""{"="*55}
        Akun : {akun}
            Nama Tim : {data["Nama Tim"]}
            Anggota  : {data["Anggota"]}
            Prodi    : {data["Prodi"]}
            Instansi : {data["Instansi"]}
        Mendaftar pada Hari {data["Hari"]}, tanggal {data["Tanggal"]}.
    """)
                            nama_ubah = input("Masukkan Nama Tim Pendaftar : ")
                            for user, data in pendaftar_valorant.items():
                                if nama_ubah == data["Nama Tim"]:
                                    print("\nPROSES UBAH DATA PENDAFTAR LOMBA VALORANT")
                                    def input_nama_anggota(anggota_ke):
                                        while True:
                                            nama = input(f"\nNama Anggota {anggota_ke}: ")
                                            if re.fullmatch(r"[A-Za-z ]+", nama):
                                                if len(nama) >= 4:
                                                    return nama
                                                else:
                                                    print("Nama Harus 4 Huruf Atau Lebih")
                                                    continue
                                            else:
                                                print("Nama hanya boleh terdiri dari huruf")
                                                continue
                                    def input_nim(anggota_ke):
                                        while True:
                                            nim = input(f"\nMasukkan NIM Anggota {anggota_ke} (isi dengan 0 jika tidak memiliki NIM): ")
                                            if nim == "0":
                                                return nim
                                            elif nim.isdigit() and len(nim) >= 10:
                                                return nim
                                            elif nim.isalpha():
                                                print("NIM Harus Berupa Angka")
                                                continue
                                            else:
                                                print("NIM Harus 10 Angka atau lebih")
                                                continue
                                    while True:
                                        nama_tim = input("Apa Nama Tim Anda: ")
                                        if  len(nama_tim) < 4:
                                            print("Nama Tim Minimal 4 Huruf")
                                        else:
                                            anggota1 = input_nama_anggota(1)
                                            NIM1 = input_nim(1)
                                            anggota2 = input_nama_anggota(2)
                                            NIM2 = input_nim(2)
                                            anggota3 = input_nama_anggota(3)
                                            NIM3 = input_nim(3)
                                            anggota4 = input_nama_anggota(4)
                                            NIM4 = input_nim(4)
                                            anggota5 = input_nama_anggota(5)
                                            NIM5 = input_nim(5)
                                            while True:
                                                prodi = input("Asal Prodi (isi dengan (-) jika tidak di prodi manapun): ")
                                                if len(prodi) >= 5 or prodi == "-":
                                                    instansi = input("Asal Instansi: ")
                                                    pendaftar_valorant[user] = {
                                                        "Nama Tim": nama_tim,
                                                        "Anggota": {
                                                            anggota1:NIM1,
                                                            anggota2:NIM2,
                                                            anggota3:NIM3,
                                                            anggota4:NIM4,
                                                            anggota5:NIM5},
                                                        "Prodi": prodi,
                                                        "Instansi": instansi,
                                                        "Hari":hari,"Tanggal":tanggal
                                                        }
                                                    data_tersimpan()
                                                    break
                                                else:
                                                    print("\nNama Prodi Harus Lengkap")
                                                    continue
                                        break
                                else:
                                    print("\nNama Tim Tidak Ditemukan")
                                break
                        # Eror handling ketika lomba yang diinput salah/ tidak ada
                        else:
                            print("Nama Lomba Tidak Valid")
                    # Menampilkan data akun user
                    elif pilihan == 3:
                        print("\nDaftar Akun User :")
                        for akun, pw in users.items():
                            print(akun)
                            print("Tekan enter untuk melanjutkan...")
                    # Menghapus data akun user
                    elif pilihan == 4:
                        print("""
    _______________________________________________
    |---------------------------------------------|
    |Pilih Lomba:                                 |
    |      1> Network          4> UI/UX           |
    |      2> Ranking 1        5> Mobile Legends  |
    |      3> Robotik          6> Valorant        |
    |_____________________________________________|
    """)
                        pilih_lomba = int(input("\nPilih Lomba : "))
                        if pilih_lomba == 1:
                            print(f"\n{"="*55}\nPENDAFTAR LOMBA NETWORK")
                            menampilkan_data_pendaftar(pendaftar_network)
                            lomba = "Network"
                        elif pilih_lomba == 2:
                            print(f"\n{"="*55}\nPENDAFTAR LOMBA RANKING #1")
                            menampilkan_data_pendaftar(pendaftar_ranking1)
                            lomba = "Ranking 1"
                        elif pilih_lomba == 3:
                            print(f"\n{"="*55}\nPENDAFTAR LOMBA ROBOTIK")
                            menampilkan_data_pendaftar_tim(pendaftar_robotik)
                            lomba = "Robotik"
                        elif pilih_lomba == 4:
                            print(f"\n{"="*55}\nPENDAFTAR LOMBA UI/UX")
                            menampilkan_data_pendaftar_tim(pendaftar_uiux)
                            lomba = "UI/UX"
                        elif pilih_lomba == 5:
                            print(f"\n{"="*55}\nPENDAFTAR LOMBA MOBILE LEGENDS")
                            menampilkan_data_pendaftar_tim(pendaftar_mobilelegends)
                            lomba = "Mobile Legends"
                        elif pilih_lomba == 6:
                            print(f"\n{"="*55}\nPENDAFTAR LOMBA VALORANT")
                            menampilkan_data_pendaftar_tim(pendaftar_valorant)
                            lomba = "Valorant"
                        else:
                            print("Pilihan Lomba Tidak Valid")
                        username = input("Masukkan username peserta yang ingin dihapus: ")
                        if lomba in perlombaan :
                            if username in perlombaan[lomba]:
                                del perlombaan[lomba][username]
                                print(f"Data pendaftar '{username}' di lomba '{lomba}' telah dihapus.")
                            else:
                                print(f"Tidak ditemukan pendaftar dengan username '{username}' di lomba '{lomba}'.")
                        else:
                            print(f"\nPenulisan '{lomba}' tidak sesuai.")
                    # Kembali ke menu sebelumnya
                    elif pilihan == 5:
                        hitung += 4
                        break
                    # Eror handling ketika memasukkan pilihan yang tidak sesuai
                    else:
                        print("\nPILIHAN TIDAK VALID")
            else:
                print("\nusername/password salah")
    # Eror handling try except
    except ValueError:
        print("\n!!!Maaf anda salah memasukan tipe data!!!")
    except SyntaxError:
        print("\n!!!Maaf ada kesalahan sehingga terjadi error!!!")
    except IndexError:
        print("\n!!!Maaf ada kesalahan sehingga terjadi error!!!")
    except AssertionError:
        print("\n!!!Maaf ada kesalahan sehingga terjadi error!!!")
    except AttributeError:
        print("\n!!!Maaf ada kesalahan sehingga terjadi error!!!")
    except ImportError:
        print("\n!!!Maaf ada kesalahan sehingga terjadi error!!!")
    except KeyError:
        print("\n!!!Maaf ada kesalahan sehingga terjadi error!!!")
    except NameError:
        print("\n!!!Maaf ada kesalahan sehingga terjadi error!!!")
    except MemoryError:
        print("\n!!!Maaf ada kesalahan sehingga terjadi error!!!")
    except TypeError:
        print("\n!!!Maaf ada kesalahan sehingga terjadi error!!!")
    except IndentationError:
        print("\n!!!Maaf ada kesalahan sehingga terjadi error!!!")
    except FileNotFoundError:
        print("\n!!!Maaf ada kesalahan sehingga terjadi error!!!")

# Fungsi utama/ program utama
def menu_utama():
    try:
        # Menampilkan menu utama
        print("""
    ______________________
    |        Menu        |
    ======================
    |   1.Buat Akun User |
    |   2.Masuk          |
    |====================|
    |   3.Login Admin    |
    |====================|
    |   0.Keluar         |
    ====================== 
    """)
        pilihan = int(input("\nMasukkan Pilihan Anda (1/2/3/0): "))
        # Pilihan membuat akun user
        if pilihan == 1:
            registrasi()
        
        # Login sebagai user
        elif pilihan == 2:
            login_user()
        
        # Login sebagai admin
        elif pilihan == 3:
            login_admin()
        
        # Keluar dari program/ memberhentikan program
        elif pilihan == 0:
            print(f"""Made by :
        > {credit[0]}
            NIM: {credit[1]}
        > {credit[2]}
            NIM: {credit[3]}
        > {credit[4]}
            NIM: {credit[5]}""")
            exit()
        
        # Eror handling ketika memasukkan pilihan yang tidak sesuai
        else:
            print("\n\nINPUTAN TIDAK VALID")

    # Eror handling try except
    except ValueError:
        print("\n!!!Maaf anda salah memasukan tipe data!!!")
    except SyntaxError:
        print("\n!!!Maaf ada kesalahan sehingga terjadi error!!!")
    except IndexError:
        print("\n!!!Maaf ada kesalahan sehingga terjadi error!!!")
    except AssertionError:
        print("\n!!!Maaf ada kesalahan sehingga terjadi error!!!")
    except AttributeError:
        print("\n!!!Maaf ada kesalahan sehingga terjadi error!!!")
    except ImportError:
        print("\n!!!Maaf ada kesalahan sehingga terjadi error!!!")
    except KeyError:
        print("\n!!!Maaf ada kesalahan sehingga terjadi error!!!")
    except NameError:
        print("\n!!!Maaf ada kesalahan sehingga terjadi error!!!")
    except MemoryError:
        print("\n!!!Maaf ada kesalahan sehingga terjadi error!!!")
    except TypeError:
        print("\n!!!Maaf ada kesalahan sehingga terjadi error!!!")
    except IndentationError:
        print("\n!!!Maaf ada kesalahan sehingga terjadi error!!!")
    except FileNotFoundError:
        print("\n!!!Maaf ada kesalahan sehingga terjadi error!!!")


    
    # melakukan perulangan menggunakan fungsi rekursif
    menu_utama()

# Memanggil/ memunculkan fungsi menu utama
menu_utama()