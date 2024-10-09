# daftar_buku={
#      #key         #value
#     "buku1" : "Harry Potter",
#     "buku2" : "Percy Jackson",
#     "buku3" : "Twilight"
# }
# print(daftar_buku["buku1"])
# # print(daftar_buku["buku2"])
# # print(daftar_buku["buku3"])
# #key tidak boleh sama, kalau sama yang atas akan tertimpa yang bawah.

# Biodata = {
#     "Nama" : "Aldy Ramadhan Syahputra",
#     "NIM" : 2109106079, #int
#     "KRS" : ["Program Web","Struktur Data","Basis Data"],
#     "Mahasiswa_Aktif" :True, #bool
#     "Social Media" : { #dictionary
#         "instagram" : "@aldyrmdhn",
#         "Discord" : "\'Izanami#6948"
#     }
# }

#perulangan
# for i, j in Biodata.items():
#     print(f"Key = {i} dan Valeu = {j}")

# for i in Biodata:
#     print(Biodata[i])

#membuat dictionary
# games = dict(Sekiro = "Action", Genshin = "Adventure", Valorant = "FPS")

# print(Biodata["Alamat"])
# print(Biodata.get("Alamat", "Kosong Bang"))

# Film = {
#     "Avenger Endgame" : "Action",
#     "Sherlock Holmes" : "Mystery",
#     "The Conjuring" : "Horror"
# }

#menambah dictionary
# Film["Zombieland"] = "Comedy" #kurung siku
# print(Film)

# Film.update({"Hour" : "Thriller"}) #update
# print(Film)

#menghapus
# print(Film)
# # del Film["The Conjuring"]
# #hapus = Film.pop("The Conjuring")
# Film.clear()
# print(Film)
# # print(f"Item yang dihapus = {hapus}")

# print("Jumlah data dalam dict Biodata = ", len(Biodata))
# pinjamdict = Biodata.copy()
# print(pinjamdict)

# key = "Apel", "Jeruk", "Mangga"
# valeu = 1

# buah = dict.fromkeys(key, valeu)
# print(buah)

#for i in Film.keys():
#for i in Film.valeus():
#     print(i end=" ")

# print(Film)
# print("Film : ", Film.setdefault("Oldbook", "Horror"))
# print(Film)

# Musik = {
#     "The Chainsmoker" : ["All We Know", "TheParis"],
#     "Alan Walker" : ["Alone", "Lily"],
#     "Neffex" : ["Best of Me", "Memmories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for lagu in j:
#         print(lagu)
#     print("")

# mahasiswa = {
#     101 : {"Nama" : "Aldy", "Umur" : 19},
#     111 : {"Nama" : "Abdul", "Umur" : 18}
# }
# # for i, j in mahasiswa.items():
# #     print(f"ID : {i}")
# #     for keynested, valeunested in j.items():
# #         print(f"{keynested} : {valeunested}")

# print(f"sebelum : {mahasiswa}")
# # mahasiswa[101]["Angkatan"] = 2023
# # print(f"Sesudah : {mahasiswa}")
# del mahasiswa[111]["Umur"]
# print(f"Sesudah : {mahasiswa}")

#STUDI KASUS
# data = {
#     "Nama1" : "Juki",
#     "Nama2" : "Reja",
#     "Nama3" : "Adit",
#     "Nama4" : "Raja Iblis",
#     "Nama5" : "Ellol"
# }

# print("Data awal")
# print(data)
# print("")
# print("Menampilkan salah satu")
# print(data["Nama2"])
# print("")
# print("Menambah data")
# data.update({"Nama6" : "Natos"})
# print(data)
# print("")
# print("Mengubah data")
# data["Nama2"] = "Supri"
# print(data)
# print("")
# print("Mengahpus data")
# del data["Nama4"]
# print(data)

#CRUD SEDERHANA MENGGUNAKAN DICTIONARY
# Biodata = {}

# while True:
#     print("1. Tambah")
#     print("2. Tampilkan")
#     print("3. Exit")
#     pilihan = int(input("1/2/3 : "))

#     if pilihan == 1:
#         nama = input("Masukkan Nama : ")
#         umur = input("Masukkan Umur : ")
#         alamat = input("Masukkan Alamat : ")

#         Biodata[nama] = {
#             'Umur' : umur,
#             'Alamat' : alamat
#         }

#     elif pilihan == 2:
#         for nama, info in Biodata.items():
#             print(f"Nama : {nama}")
#             print(f"Umur : {info['Umur']}")
#             print(f"Alamat : {info['Alamat']}")

#     elif pilihan == 3:
#         print("exit ...")
#         break

#     else:
#         print("Invalid ... ... ")