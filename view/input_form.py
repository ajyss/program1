from view.mahasiswa import Mahasiswa

class InputForm:
    def get_input(self):
        nama = input("Masukkan nama: ")
        nim = input("Masukkan NIM: ")
        nilai = float(input("Masukkan nilai: "))
        return Mahasiswa(nama, nim, nilai)