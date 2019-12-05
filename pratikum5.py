print("PROGRAM INPUT NILAI")
print("===================")
data = {}
while True:
    print("")
    c = input("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar: ")
    if c.lower() == 'k':
        break
    elif c.lower() == 'l':
        print ("'.'.'.'.'.'.'.'.'.'.'.'.'.'.  DAFTAR NILAI  .'.'.'.'.'.'.'.'.'.'.'.'.'.'")
        print ("========================================================================")
        print (" |  N0 |   NAMA     |     NIM     |  TUGAS |   UTS  |   UAS  |  AKHIR |" )
        print ("========================================================================")
        i=0
        for x in data.items():
            i+=1
            print (" |  {6:2} | {0:9s}  | {1:11} | {2:6d} | {3:6d} | {4:6d} | {5:6.2f} |"\
                   .format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
        print ("========================================================================")
    elif c.lower() == 't':
        print(" Tambah Data ")
        nama = input(" Nama        : ")
        nim = input(" NIM         : ")
        nilaiuts = int(input(" Nilai UTS   : "))
        nilaiuas = int(input(" Nilai UAS   : "))
        nilaitgs = int(input(" Nilai TUGAS : "))
        akhir = (nilaitgs * 30/100 + nilaiuts * 35/100 + nilaiuas * 35/100)
        data[nama] = nim, nilaitgs, nilaiuts, nilaiuas, akhir
    elif c.lower() == 'u':
        print("Ubah Data")
        nama = input("Nama        : ")
        if nama in data.keys():
            nim = input("NIM         : ")
            nilaiuts = int(input("Nilai UTS   : "))
            nilaiuas = int(input("Nilai UAS   : "))
            nilaitgs = int(input("Nilai TUGAS : "))
            akhir = (nilaitgs * 30/100 + nilaiuts * 35/100 + nilaiuas * 35/100)
            data[nama] = nim, nilaitgs, nilaiuts, nilaiuas, akhir
        else:
            print("Data {0} tidak ada".format(nama))
    elif c.lower() == 'h':
        print("Hapus Data")
        nama = input("Nama : ")
        if nama in data.keys():
            del data[nama]
        else:
            print("Data {0} tidak ada".format(nama))
    elif c.lower() == 'c':
        print("Cari Data")
        nama = input("Nama : ")
        if nama in data.keys():
            print ("'.'.'.'.'.'.'.'.'.'.'.'.'. DAFTAR NILAI .'.'.'.'.'.'.'.'.'.'.'.'.'")
            print ("==================================================================")
            print (" |   Nama     |     NIM     |  Tugas |   UTS  |   UAS  |  AKHIR |")
            print ("==================================================================")
            print (" | {0:9s}  | {1:11} | {2:6d} | {3:6d} | {4:6d} | {5:6.2f} |"\
                   .format(nama, nim, nilaitgs, nilaiuts, nilaiuas, akhir))
            print ("==================================================================")
        else:
            print("Data {0} tidak ada".format(nama))
    else:
        print("Pilih menu yang tersedia")
