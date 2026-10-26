
# PROGRAM SISTEM PENGHITUNG SLOT PARKIR ITB GANESHA


# KAMUS

# Max : kapasitas maksimum parkir
# Sk : jumlah kendaraan yang sedang terparkir
# S : jumlah slot parkir tersedia
# peran : pilihan menu utama
# kartu : input tap kartu
# pilihan : pilihan transaksi
# riwayat : array untuk menyimpan riwayat transaksi
# jumlah_riwayat : jumlah transaksi yang tercatat
# i : indeks untuk menampilkan riwayat



# FUNGSI MENENTUKAN STATUS

def tentukan_status(S, Max):
    if S == 0:
        return "SLOT TIDAK TERSEDIA"
    elif S <= 0.1 * Max:
        return "SLOT HAMPIR PENUH"
    else:
        return "SLOT TERSEDIA"
    


# FUNGSI MENAMPILKAN STATUS

def tampilkan_status(S, Max):
    print("\n==============================")
    print("    SISTEM PARKIR ITB GANESHA")
    print("==============================")
    print("Kapasitas maksimum :", Max)
    print("Kendaraan terparkir:", Max - S)
    print("Slot tersedia      :", S)
    print("Status             :", tentukan_status(S, Max))
    print("==============================")



# ALGORITMA

Max = 0
Sk = 0
S = 0
data_tersedia = False

# ARRAY RIWAYAT TRANSAKSI
riwayat = [""] * 100
jumlah_riwayat = 0

while True:
    print("\n========== MENU UTAMA ==========")
    print("1. Pengelola parkir")
    print("2. Pengguna parkir")
    print("3. Keluar")

    peran = input("Pilih menu: ")

    
    # PENGELOLA PARKIR
    
    if peran == "1":
        Max = int(input("Masukkan kapasitas maksimum: "))

        if Max <= 0:
            print("Kapasitas harus lebih dari 0.")

        else:
            Sk = int(input("Masukkan jumlah kendaraan yang sedang terparkir: "))

            if Sk < 0 or Sk > Max:
                print("Jumlah kendaraan tidak valid.")

            else:
                S = Max - Sk
                data_tersedia = True

                print("Data parkir berhasil diperbarui.")
                tampilkan_status(S, Max)

    
    # PENGGUNA PARKIR
    
    elif peran == "2":

        if data_tersedia == False:
            print("Data parkir belum diatur oleh pengelola.")

        else:
            # MODE PENGGUNA BERJALAN TERUS
            while True:
                tampilkan_status(S, Max)

                kartu = input( "\nTap kartu (y) atau ketik off untuk mematikan sistem: ")

                
                # MEMATIKAN SISTEM
                
                if kartu == "off":
                    print("\nSISTEM PARKIR DIMATIKAN")
                    print("\n====== RIWAYAT TRANSAKSI ======")

                    if jumlah_riwayat == 0:
                        print("Belum ada transaksi.")

                    else:
                        for i in range(jumlah_riwayat):
                            print(i + 1, ".", riwayat[i])

                    
                    print("Program selesai.")
                    exit()

                
                # KARTU DITERIMA
                
                elif kartu == "y":
                    print("\n1. Kendaraan masuk")
                    print("2. Kendaraan keluar")

                    pilihan = input("Pilih transaksi: ")

                    
                    # KENDARAAN MASUK
                    
                    if pilihan == "1":

                        if S > 0:
                            S = S - 1
                            Sk = Sk + 1

                            print("Transaksi berhasil: kendaraan masuk.")

                            if jumlah_riwayat < 100:
                                riwayat[jumlah_riwayat] = ( "Kendaraan masuk | Slot tersedia: " + str(S))
                                jumlah_riwayat = jumlah_riwayat + 1
                            else:
                                print("Riwayat transaksi sudah penuh.")

                        else:
                            print("Transaksi gagal: parkir penuh.")

                    
                    # KENDARAAN KELUAR
                    
                    elif pilihan == "2":

                        if Sk > 0:
                            S = S + 1
                            Sk = Sk - 1

                            print("Transaksi berhasil: kendaraan keluar." )

                            if jumlah_riwayat < 100:
                                riwayat[jumlah_riwayat] = ("Kendaraan keluar | Slot tersedia: " + str(S))
                                jumlah_riwayat = jumlah_riwayat + 1
                            else:
                                print("Riwayat transaksi sudah penuh.")

                        else:
                            print("Transaksi gagal: tidak ada kendaraan.")
                    else:
                        print("Pilihan transaksi tidak valid.")

                else:
                    print("Kartu tidak dikenali.")

    
    # KELUAR DARI MENU UTAMA
    
    elif peran == "3":
        print("Program selesai.")
        break

    else:
        print("Pilihan menu tidak valid.")
