#CRUD PENDATAAN HEWAN DI KEBUN BINATANG
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

    admin = [["admin1","admin#1234"],["admin2","entahlah"]]
    pengunjung = []
    hewan = [["Harimau Sumatera",7,2,5,"Felidae"],["Badak Sumatera",4,2,2,"Rhinocerotidae"],["Macan Tutul",6,2,4,"Felidae"],
             ["Buaya Muara",12,5,7,"Crocodylidae"],["Orangutan",4,2,2,"Hominidae"],["Singa Utara",5,1,4,"Felidae"]]

    pilihan = int(input("Pilihan : "))
    if pilihan == 1:
        username = input("username : ")
        password = input("password : ")
        for i in range(len(admin)):
            if admin[i][0] == username and admin[i][1] == password:
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
                    hewan.append([namahewan,jumlah,pejantan,betina,famili])
                elif pilihan == 2:
                    print("DAFTAR HEWAN YANG ADA DI KEBUN JUR-ASYIK")
                    for i in range(len(hewan)):
                        print(f"\n> {hewan[i][0]}\nJumlah Total :{hewan[i][1]} ekor\nJumlah Pejantan :{hewan[i][2]} ekor\nJumlah Betina :{hewan[i][3]} ekor\nFamili :{hewan[i][4]}")
                elif pilihan == 3:
                    nama_hewan = input("Nama Hewan Yang Ingin Diganti : ")
                    for i in range(len(hewan)):
                        if hewan[i][0] == nama_hewan:
                            namahewan_baru = input("Nama Hewan : ")
                            jumlah_baru = int(input("Jumlah : "))
                            pejantan_baru = int(input("Umlah Pejantan : "))
                            betina_baru = int(input("Jumlah Betina : "))
                            famili_baru = input("Famili : ")
                            hewan[i][0]=namahewan_baru
                            hewan[i][1]=jumlah_baru
                            hewan[i][2]=pejantan_baru
                            hewan[i][3]=betina_baru
                            hewan[i][4]=famili_baru
                elif pilihan == 4:
                    nama_hewan = input("Nama Hewan yang Ingin Dihapus : ")
                    for i in range(len(hewan)):
                        if hewan[i][0] == nama_hewan:
                            del hewan[i]
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
                if hitung > 1:
                    for i in range(len(pengunjung)):
                        if pengunjung[i][0] == username:
                            print("\n\n\nUSERNAME SUDAH DIPAKAI")
                            break
                        else:
                            pengunjung.append([username,password])
                else:
                    pengunjung.append([username,password])
            elif pilihan == 2:
                username = input("username : ")
                password = input("password : ")
                for i in range(len(pengunjung)):
                    if pengunjung[i][0] == username and pengunjung[i][1] == password:
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
                                for i in range(len(hewan)):
                                    print(f"\n> {hewan[i][0]}\nJumlah Total :{hewan[i][1]} ekor\nJumlah Pejantan :{hewan[i][2]} ekor\nJumlah Betina :{hewan[i][3]} ekor\nFamili :{hewan[i][4]}")
                            elif pilihan == 2:
                                print("Terima Kasih Telah Mengakses Sistem Daftar Hewan di Kebun Jur-Asyik.")
                                break
                    else:
                        print("username/password tidak valid")
                        break
            elif pilihan == 3:
                print("Anda telah keluar.")
                break
            else:
                print("Pilihan Invalid")
    elif pilihan == 0:
        print("Keluar dari Program")
        break
    else:
        print("Pilihan Invalid")