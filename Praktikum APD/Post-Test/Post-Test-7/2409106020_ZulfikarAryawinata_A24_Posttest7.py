admin = {
        "admin1" : "admin#1234",
        "admin2" : "entahlah"
    }
pengunjung = {}
hewan = {
        "Harimau Sumatera" : {
            "Jumlah Total" : 7,
            "Jumlah Pejantan" : 2,
            "Jumlah Betina" : 5,
            "Famili" : "Felidae"
        },
        "Badak Sumatera" : {
            "Jumlah Total" : 4,
            "Jumlah Pejantan" : 2,
            "Jumlah Betina" : 2,
            "Famili" : "Rhinocerotidae"
        },
        "Macan Tutul" : {
            "Jumlah Total" : 6,
            "Jumlah Pejantan" : 2,
            "Jumlah Betina" : 4,
            "Famili" : "Felidae"
        },
        "Buaya Muara" : {
            "Jumlah Total" : 12,
            "Jumlah Pejantan" : 5,
            "Jumlah Betina" : 7,
            "Famili" : "Crocodylidae"
        },
        "Orangutan" : {
            "Jumlah Total" : 4,
            "Jumlah Pejantan" : 2,
            "Jumlah Betina" : 2,
            "Famili" : "Hominidae"
        },
        "Singa Utara" : {
            "Jumlah Total" : 5,
            "Jumlah Pejantan" : 1,
            "Jumlah Betina" : 4,
            "Famili" : "Felidae"
        }
    }

def tambah_data():
    while True:
        namahewan = input("Nama Hewan : ")
        jumlah = int(input("Jumlah Total : "))
        pejantan = int(input("Jumlah Pejantan : "))
        betina = int(input("Jumlah Betina : "))
        famili = input("Famili : ")
        if pejantan + betina != jumlah:
            print("\nDATA TIDAK VALID") 
        else:
            hewan[namahewan] = {
                "Jumlah Total" : jumlah,
                "Jumlah Pejantan" : pejantan,
                "Jumlah Betina" : betina,
                "Famili" : famili
                }
            break
    
def tampilkan_data():
    print("\n\nDAFTAR HEWAN YANG ADA DI KEBUN JUR-ASYIK")
    for spesies, info in hewan.items():
        print(f"\n{spesies}\nJumlah Total : {info["Jumlah Total"]} ekor\nJumlah Pejantan : {info["Jumlah Pejantan"]} ekor\nJumlah Betina : {info["Jumlah Betina"]} ekor\nFamili : {info["Famili"]}")

def ubah_data():
    nama_hewan = input("Nama Hewan Yang Ingin Diganti Datanya : ")
    for spesies, info in hewan.items():
        if spesies == nama_hewan:
            jumlah_update = int(input("Jumlah : "))
            pejantan_update = int(input("Jumlah Pejantan : "))
            betina_update = int(input("Jumlah Betina : "))
            famili_update = input("Famili : ")
            if pejantan_update + betina_update != jumlah_update:
                print("DATA TIDAK VALID")
                break
            else:
                hewan[spesies] = {
                    "Jumlah Total" : jumlah_update,
                    "Jumlah Pejantan" : pejantan_update,
                    "Jumlah Betina" : betina_update,
                    "Famili" : famili_update
                    }
            
def hapus_data():
    hapus = input("\n\nNama Hewan yang Ingin Dihapus : ")
    del hewan[hapus]

def login_admin():
    username = input("\nusername : ")
    password = input("password : ")
    if username in admin and admin[username] == password:
        print("\n\n\nSELAMAT DATANG DI SISTEM PENDATAAN HEWAN DI KEBUN JUR-ASYIK")
        return True
    else:
        print("\nusername/password salah")
        return False

def regis_pengunjung():
    username = input("\nMasukkan username yang ingin anda gunakan : ")
    password = input("Masukkan password yang ingin anda gunakan : ")
    if username in pengunjung:
        print("\nUsername Telah Dipakai")
    else:
        pengunjung[username] = password

def login_pengunjung():
    username = input("\nusername : ")
    password = input("password : ")
    if username in pengunjung and pengunjung[username] == password:
        print("\n\n\nSELAMAT DATANG DI SISTEM PENDATAAN HEWAN DI KEBUN JUR-ASYIK")
        return True
    else:
        print("\nusername/password salah")
        return False

def sistem_data_hewan():
    while True:
        print("""
========================
|===MASUK SEBAGAI : ===|
|                      |
| 1. Admin             |
| 2. Pengunjung        |
|                      |
| 0. Keluar            |
========================
""")
        pilihan = int(input("Masukkan Pilihan : "))
        if pilihan == 1:
            if login_admin():
                while True:
                    print("""____________________________
|Pilih Menu                |
|==========================|
|   1. Tambah Data         |
|   2. Tampilkan Data Hewan|
|   3. Ubah Data Hewan     |
|   4. Hapus Data          |
|   5. Keluar              |
|__________________________|
""")
                    pilihan = int(input("Masukkan Pilihan : "))
                    if pilihan == 1:
                        tambah_data()
                    elif pilihan == 2:
                        tampilkan_data()
                    elif pilihan == 3:
                        ubah_data()
                    elif pilihan == 4:
                        hapus_data()
                    elif pilihan == 5:
                        break
        elif pilihan == 2:
            while True:
                print("""
|======================================================|
|  1. Register                                         |
|    (jika anda belum memiliki akun/membuat akun baru) |
|  2. Login                                            |
|    (jika sudah memiliki akun)                        |
|  3. Keluar                                           |
|------------------------------------------------------|
""")
                pilihan = int(input("Pilihan : "))
                if pilihan == 1:
                    regis_pengunjung()
                elif pilihan == 2:
                    if login_pengunjung():
                        while True:
                            print("""
===================================
| 1. Tampilkan Daftar Data Hewan  |
| 2. Keluar                       |
===================================
""")
                            pilihan = int(input("Masukkan Pilihan : "))
                            if pilihan == 1:
                                tampilkan_data()
                            elif pilihan == 2:
                                break
                elif pilihan == 3:
                    print("\n\nAnda telah keluar.")
                    break
                else:
                    print("\n\nPilihan Invalid")
        elif pilihan == 0:
            print("\n\nTerima Kasih atas Kunjungannya")
            exit()
        else:
            print("\n\nPilihan Tidak Valid")
            break

sistem_data_hewan()