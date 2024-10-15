

# CRUD PENDATAAN HEWAN DI KEBUN BINATANG

while True:
    print(
    """
========================
|===MASUK SEBAGAI : ===|
|                      |
| 1. Admin             |
| 2. Pengunjung        |
|                      |
| 0. Keluar            |
========================
""")

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

    pilihan = int(input("Pilihan : "))
    if pilihan == 1:
        username = input("username : ")
        password = input("password : ")
        for i, j in admin.items():
            if i == username and j == password:
                print("\n\n\nSELAMAT DATANG DI SISTEM PENDATAAN HEWAN DI KEBUN JUR-ASYIK")
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
                pilihan = int(input("Pilihan Anda : "))
                if pilihan == 1:
                    namahewan = input("Nama Hewan : ")
                    jumlah = int(input("Jumlah Total : "))
                    pejantan = int(input("Jumlah Pejantan : "))
                    betina = int(input("Jumlah Betina : "))
                    famili = input("Famili : ")
                    
                    hewan[namahewan] = {
                        "Jumlah Total" : jumlah,
                        "Jumlah Pejantan" : pejantan,
                        "Jumlah Betina" : betina,
                        "Famili" : famili
                    }
                elif pilihan == 2:
                    print("DAFTAR HEWAN YANG ADA DI KEBUN JUR-ASYIK")
                    for spesies, info in hewan.items():
                        print(f"\n{spesies}\nJumlah Total : {info["Jumlah Total"]} ekor\nJumlah Pejantan : {info["Jumlah Pejantan"]} ekor\nJumlah Betina : {info["Jumlah Betina"]} ekor\nFamili : {info["Famili"]}")
                elif pilihan == 3:
                    nama_hewan = input("Nama Hewan Yang Ingin Diganti Datanya : ")
                    for spesies, info in hewan.items():
                        if spesies == nama_hewan:
                            jumlah_update = int(input("Jumlah : "))
                            pejantan_update = int(input("Umlah Pejantan : "))
                            betina_update = int(input("Jumlah Betina : "))
                            famili_update = input("Famili : ")
                            hewan[spesies] = {
                                "Jumlah Total" : jumlah_update,
                                "Jumlah Pejantan" : pejantan_update,
                                "Jumlah Betina" : betina_update,
                                "Famili" : famili_update
                            }
                elif pilihan == 4:
                    hapus = input("Nama Hewan yang Ingin Dihapus : ")
                    del hewan[hapus]
                elif pilihan == 5:
                    print("Anda Telah Keluar dari Sistem Pendataan Hewan di Kebun Jur-Asyik")
                    break
                else:
                    print("Pilihan Invalid")
    elif pilihan == 2:
        hitung = 0
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
                hitung += 1
                username = input("Masukkan username yang ingin anda gunakan : ")
                password = input("Masukkan password yang ingin anda gunakan : ")
                if hitung == 1:
                    pengunjung[username] = password
                elif hitung > 1:
                    for i, j in pengunjung.items():
                        if i == username:
                            print("\n\n\nUSERNAME SUDAH DIPAKAI")
                        else:
                            i = username
                            j = password
            elif pilihan == 2:
                username = input("username : ")
                password = input("password : ")
                for i, j in pengunjung.items():
                    if i == username and j == password:
                        print("SELAMAT DATANG DI SISTEM PENDATAAN HEWAN DI KEBUN JUR-ASYIK")
                        while True:
                            print("""
===================================
| 1. Tampilkan Daftar Data Hewan  |
| 2. Keluar                       |
===================================
""")
                            pilihan = int(input("Pilihan : "))
                            if pilihan == 1:
                                for spesies, info in hewan.items():
                                    print(f"\n{spesies}\nJumlah Total : {info["Jumlah Total"]} ekor\nJumlah Pejantan : {info["Jumlah Pejantan"]} ekor\nJumlah Betina : {info["Jumlah Betina"]} ekor\nFamili : {info["Famili"]}")
                            elif pilihan == 2:
                                print("Terima Kasih Telah Mengakses Sistem Daftar Hewan di Kebun Jur-Asyik.")
                                break
                    else:
                        print("username/password tidak valid")
                        break
            elif pilihan == 3:
                pilihan
                print("Anda telah keluar.")
                break
            else:
                print("Pilihan Invalid")
    elif pilihan == 0:
        print("Keluar dari Program")
        break
    else:
        print("Pilihan Invalid")