def tambah(a,b):
    return a+b

def kurang(a,b):
    return a-b

def bagi(a,b):
    return a/b

def kali(a,b):
    return a*b

def menu():
    while (True):
        print("Kalkulator")
        print("=========================================")
        print("Menu....")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Pembagian")
        print("4. Perkalian")
        pilih = input("Silahkan Pilih : ")

        a = int(input("Angka Pertama : "))
        b = int(input("Angka Kedua : "))

        if pilih == '1':
            print("Hasil = ", tambah(a, b))
            lanjut = str(input("Mengulang ? (Y/N) : "))
            if lanjut == 'Y' or lanjut == 'y':
                continue
            else:
                print("=================Selesai=================")
                break

        elif pilih == '2':
            print("Hasil = ", kurang(a, b))
            lanjut = str(input("Mengulang ? (Y/N) : "))
            if lanjut == 'Y' or lanjut == 'y':
                continue
            else:
                print("=================Selesai=================")
                break

        elif pilih == '3':
            print("Hasil = ", bagi(a, b))
            lanjut = str(input("Mengulang ? (Y/N) : "))
            if lanjut == 'Y' or lanjut == 'y':
                continue
            else:
                print("=================Selesai=================")
                break

        elif pilih == '4':
            print("Hasil = ", kali(a, b))
            lanjut = str(input("Mengulang ? (Y/N) : "))
            if lanjut == 'Y' or lanjut == 'y':
                continue
            else:
                print("=================Selesai=================")
                break

        else:
            lanjut = str(input("Tidak Tersedia. Mengulang ? (Y/N) : "))
            if lanjut == 'Y' or lanjut == 'y':
                continue
            else:
                print("=================Selesai=================")
                break
menu()