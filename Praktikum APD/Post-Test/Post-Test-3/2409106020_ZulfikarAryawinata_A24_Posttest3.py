#PROGRAM KALKULATOR KEBUTUHAN KALORI HARIAN
print("SELAMAT DATANG DI PROGRAM KALKULATOR KEBUTUHAN KALORI HARIAN")
print("=Pilih Jenis Kelamin Anda=")
print("1. Pria")
print("2. Wanita")
gender = input("Pilihan :")

if gender == "1":
    umur = int(input("Masukkan Umur Anda :"))
    Berat_Badan = float(input("Masukkan Berat Badan Anda (gr) :"))
    Tinggi_Badan = float(input("Masukkan Tinggi Badan Anda (Km) :"))
    Konversi_BB = float(Berat_Badan/1000)
    Konversi_TB = float(Tinggi_Badan*100000)
    BMR_Pria= float(10*Konversi_BB)+(6.25*Konversi_TB)-(5*umur)+5
    print("BMR anda =", BMR_Pria)

    print("======Pilihlah Level Aktivitas Harian Anda======")
    print("1. Aktivitas Minimal (jarang bergerak)")
    print("2. Aktivitas Sedang (olahraga 1-3 kali seminggu)")
    print("3. Aktivitas Tinggi (olahraga 4-7 kali seminggu)")
    pilihan = input("Pilihan :")

    if pilihan == "1":
        kalori = float(BMR_Pria*1.25)
        print("Kebutuhan Kalori Harian Anda =", kalori,"kal")
    elif pilihan == "2":
        kalori = float(BMR_Pria*1.36)
        print("Kebutuhan Kalori Harian Anda =", kalori,"kal")
    elif pilihan == "3":
        kalori = float(BMR_Pria*1.72)
        print("Kebutuhan Kalori Harian Anda =", kalori,"kal")
    else:
        print("Invalid")
elif gender == "2":
    umur = int(input("Masukkan Umur Anda :"))
    Berat_Badan = float(input("Masukkan Berat Badan Anda (gr) :"))
    Tinggi_Badan = float(input("Masukkan Tinggi Badan Anda (Km) :"))
    Konversi_BB = float(Berat_Badan/1000)
    Konversi_TB = float(Tinggi_Badan*100000)
    BMR_Wanita = (10*Konversi_BB)+(6.25*Konversi_TB)-(5*umur)-161
    print("BMR anda =", BMR_Wanita)

    print("======Pilihlah Level Aktivitas Harian Anda======")
    print("1. Aktivitas Minimal (jarang bergerak)")
    print("2. Aktivitas Sedang (olahraga 1-3 kali seminggu)")
    print("3. Aktivitas Tinggi (olahraga 4-7 kali seminggu)")
    pilihan = input("Pilihan :")

    if pilihan == "1":
        kalori = float(BMR_Wanita*1.25)
        print("Kebutuhan Kalori Harian Anda =", kalori,"kal")
    elif pilihan == "2":
        kalori = float(BMR_Wanita*1.36)
        print("Kbetuhuan Kalori Harian Anda =", kalori,"kal")
    elif pilihan == "3":
        kalori = float(BMR_Wanita*1.72)
        print("Kebutuhan Kalori Harian Anda =", kalori,"kal")
    else:
        print("Invalid")
else:
    print("Invalid")