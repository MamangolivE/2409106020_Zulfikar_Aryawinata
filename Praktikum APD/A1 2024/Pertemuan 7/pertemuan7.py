# # Pertemuan Ke-7
# def salam(salam):
#     # print(iso)
#     print(salam)

# iso = "Salam Iso"
# salam(iso)

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# luas = luas_persegi(2)
# print(luas)


# # membuat variabel global
# Nama = "Informatika"
# Mata_Kuliah = "Algoritma dan Pemrograman Dasar"
# # membuat variabel lokal
# def info():
#     Nama = "Teknik Elektro"
#     Mata_Kuliah = "Pengantar Teknik ELektro"
#     # mengakses variabel lokal
#     print("Prodi:", Nama)
#     print("Mata Kuliah:", Mata_Kuliah)

# def info2():
#     print("Prodi", Nama)
#     print("Mata Kuliah :", Mata_Kuliah)

# # mengakses variabel global
# print("Prodi:", Nama)
# print("Mata Kuliah:", Mata_Kuliah)
# # memanggil fungsi info
# info()
# info2()

# CRUD DENGAN FUNGSI

# buku = []

# def show_data():
#     if len(buku) <= 0:
#         print ("Belum Ada data")
#     else:
#         print("ID", "Nama Buku")
#         for indeks in range(len(buku)):
#             print (indeks, buku[indeks])
            
# def insert_data():
#     buku_baru = input("Judul Buku : ")
#     buku.append(buku_baru)

# def edit_data():
#     show_data()
#     indeks = int(input("Masukkan ID Buku : "))
#     if indeks >= len(buku) or indeks < 0 :
#         print("ID salah")
#     else:
#         judul_baru = input("Masukkan Judul Buku Baru : ")
#         buku[indeks] = judul_baru

# def delete_data():
#     show_data()
#     indeks = int(input("Masukkan ID Buku : "))
#     if indeks >= len(buku) or indeks < 0 :
#         print("ID salah")
#     else:
#         buku.remove(buku[indeks])

# def show_menu():
#     print("Menu")
#     print("1. Read")
#     print("2. Create")
#     print("3. Update")
#     print("4. Delete")
#     print("5. Keluar")
#     pilihan = int(input("Masukkan Pilihan : "))
#     if pilihan == 1:
#         show_data()
#     elif pilihan == 2:
#         insert_data()
#     elif pilihan == 3:
#         edit_data()
#     elif pilihan == 4:
#         delete_data()
#     elif pilihan ==5:
#         exit()
#     else:
#         print("Pilihan Tidak Valid")

# while(True):
#     show_menu()

# def square_root(num):
#     procesion = 0.00001
#     if num < 0:
#         return "angka negatif tidak memiliki akar yang terdefinisi"
#     guess = num / 2.0
#     while abs(guess * guess - num) > 

# import math
# angka = 9
# print(math.sqrt(angka))

# STUDI KASUS
# def luas_segitiga():
#     alas = float(input("Alas Segitiga : "))
#     tinggi = float(input("Tinggi Segitiga : "))
#     luas = (1/2 * alas * tinggi)
#     return luas

# print(luas_segitiga())


# def luas_persegipanjang():
#     panjang = float(input("Masukkan Panjang : "))
#     lebar = float(input("Masukkan Lebar : "))
#     luas = panjang * lebar
#     return luas

# print(luas_persegipanjang())