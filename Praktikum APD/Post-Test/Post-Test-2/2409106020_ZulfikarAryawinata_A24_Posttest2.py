Nama = input("Masukkan Nama Lengkap Anda :")
NIM:int = input("Masukkan NIM Anda :")
Panggilan = input("Nama Panggilan :")
Prodi = input("Masukkan Prodi Anda :")
Fakultas = input("Masukkan Fakultas Anda :")
Universitas = input("Masukkan Universitas Anda :")
usia:float = (input("Berapa Usia Anda :"))
Tinggi:float = (input("Berapa Tinggi Badan Anda :"))
BB:float = (input("Berapa Berat Badan Anda :"))
Hobi = input("Apa Hobi Anda :")

print("Halo, perkenalkan nama saya ", Nama, "biasa dipanggil ", Panggilan,". NIM saya adalah", NIM,
      ", saya dari Program Studi", Prodi,", Fakultas", Fakultas,"," ,Universitas,". Sekarang saya berusia", usia,"tahun"
      ". Tinggi badan saya adalah", Tinggi,"cm"" dan berat badan saya adalah", BB,"Kg"". Saya memiliki hobi", Hobi,".")
if int(NIM[7:10])>=100:
    print("3 digit terakhir NIM =", NIM[7:10], "% 6")
else:
    print("2 digit terakhir NIM =", NIM[8:10], "% 6")
