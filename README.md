# Pratikum-5
Dictionary Input Nilai Mahasiswa

_**Penjelasan Program**_

1. Pertama kita tekan _**L**_ untuk melihat daftar nilai, lalu untuk menambahkan data kita tekan _**T**_ dan bisa dilihat seperti gambar dibawah ini.
![Screenshot (1)](https://user-images.githubusercontent.com/56881488/70243335-faeaf900-17a4-11ea-9e99-7cddb3f86cad.png)

2. Kedua kita tekan _**T**_ apabila ingin menambah data lagi misalkan kita tambah data cintakuuu dan tekan _**L**_ untuk melihatnya seperti gambar dibawah ini.
![Screenshot (2)](https://user-images.githubusercontent.com/56881488/70243336-fb838f80-17a4-11ea-9f4b-b9ea2b7a5f02.png)

3. Ketiga kita tekan _**U**_ untuk mengubah data misalkan kita ubah data ray dan untuk melihatnya tekan _**L**_ seperti gambar dibawah ini.
![Screenshot (3)](https://user-images.githubusercontent.com/56881488/70243356-04746100-17a5-11ea-8e72-9fea086014ea.png)

4. Keempat kita tekan _**C**_ untuk mencari data misalkan kita cari data ray seperti gambar dibawah ini.
![Screenshot (4)](https://user-images.githubusercontent.com/56881488/70243359-04746100-17a5-11ea-9b3c-5e665e439b97.png)

5. Kelima kita tekan _**H**_ untuk menghapus data misalkan kita hapus data cintakuuu dan kita tekan _**L**_ untuk melihatnya dan untuk keluar program kita tekan _**K**_ seperti gambar dibawah ini.
![Screenshot (5)](https://user-images.githubusercontent.com/56881488/70243361-050cf780-17a5-11ea-9a4b-1844b435a461.png)

_**FLOWCHART**_
![Screenshot (60)](https://user-images.githubusercontent.com/56881488/70244817-b319a100-17a7-11ea-81f4-3e9ab2db4129.png)

_**NOTE FLOWCHART**_
1. _**while True:**_
2. c = _**input**_("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar: ")
3. _**if**_ c.lower() == 'k':
4. _**elif**_ c.lower() == 'l':
5. _**print**_ daftar nilai
   i=0
6. _**for**_ x _**in**_ data.items(): 
	i+=1
7. _**print**_ (" |  {6:2} | {0:9s}  | {1:11} | {2:6d} | {3:6d} | {4:6d} | {5:6.2f} |"\
                   .format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
8. _**elif**_ c.lower() == 't':
9. _**input**_ nama = _**input**_(" Nama        : ")
        nim = _**input**_(" NIM         : ")
        nilaiuts = _**int**_(_**input**_(" Nilai UTS   : "))
        nilaiuas = _**int**_(_**input**_(" Nilai UAS   : "))
        nilaitgs = _**int**_(_**input**_(" Nilai TUGAS : "))
10. akhir = (nilaitgs * 30/100 + nilaiuts * 35/100 + nilaiuas * 35/100)
    data[nama] = nim, nilaitgs, nilaiuts, nilaiuas, akhir
11. _**elif**_ c.lower() == 'u':
12. _**input**_ nama :
13. _**if**_ nama _**in**_ data.keys():
	nim = _**input**_("NIM         : ")
        nilaiuts = _**int**_(_**input**_("Nilai UTS   : "))
        nilaiuas = _**int**_(_**input**_("Nilai UAS   : "))
        nilaitgs = _**int**_(_**input**_("Nilai TUGAS : "))
        akhir = (nilaitgs * 30/100 + nilaiuts * 35/100 + nilaiuas * 35/100)
        data[nama] = nim, nilaitgs, nilaiuts, nilaiuas, akhir
14. _**else**_:
             _**print**_("Data {0} tidak ada".format(nama))
15. _**elif**_ c.lower() == 'h':
16. _**input**_ nama :
17. _**if**_ nama _**in**_ data.keys(): 
18. _**del**_ data[nama]
19. _**else**_:
        _**print**_("Data {0} tidak ada".format(nama))
20. _**elif**_ c.lower() == 'c':
21. _**input**_ nama :
22. _**if**_ nama _**in**_ data.keys():
	_**print**_ (" daftar nilai ")
	_**print**_ (" | {0:9s}  | {1:11} | {2:6d} | {3:6d} | {4:6d} | {5:6.2f} |"\
                   .format(nama, nim, nilaitgs, nilaiuts, nilaiuas, akhir))
23. _**else**_:
        _**print**_("Data {0} tidak ada".format(nama))
24. _**else**_:
        _**print**_("Pilih menu yang tersedia")
