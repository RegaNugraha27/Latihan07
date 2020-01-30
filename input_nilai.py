from Model.Daftar_Nilai import tambah_data
def inputan():
    nama = input("NAMA : ")
    nim = int(input("NIM : "))
    tugas = int(input("TUGAS : "))
    uts = int(input("UTS : "))
    uas = int(input("UAS : "))
    tambah_data(nama, nim, tugas, uts, uas)

def edit():
    from Model.Daftar_Nilai import edit_data
    edit_data(nama=input("Masukan nama untuk edit data : "))

def delete():
    from Model.Daftar_Nilai import delete_data
    delete_data(nama=input("Masukan nama untuk menghapus data : "))

def cari():
    from Model.Daftar_Nilai import cari_data
    cari_data(nama=input("Masukan nama yang di cari : "))