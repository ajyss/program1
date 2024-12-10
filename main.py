from view.mahasiswa import Mahasiswa
from view.input_form import InputForm

def main():
    print("Selamat datang di Program Manajemen Data Mahasiswa!")

    while True:
        print("\nMenu:")
        print("1. Tambah Data Mahasiswa")
        print("2. Hapus Data Mahasiswa")
        print("3. Ubah Data Mahasiswa")
        print("4. Tampilkan Data Mahasiswa")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan (1-5): ")
class Mahasiswa:
    daftar_mahasiswa = []

    def __init__(self, nama, nim, nilai):
        self.nama = nama
        self.nim = nim
        self.nilai = nilai

    @classmethod
    def tambah_data(cls, nama, nim, nilai):
        mahasiswa_baru = Mahasiswa(nama, nim, nilai)
        cls.daftar_mahasiswa.append(mahasiswa_baru)
        print(f"Data {nama} berhasil ditambahkan.")

    @classmethod
    def hapus_data(cls, nim):
        for mahasiswa in cls.daftar_mahasiswa:
            if mahasiswa.nim == nim:
                cls.daftar_mahasiswa.remove(mahasiswa)
                print(f"Data dengan NIM {nim} berhasil dihapus.")
                return
        print(f"Data dengan NIM {nim} tidak ditemukan.")

    @classmethod
    def ubah_data(cls, nim, nama_baru=None, nilai_baru=None):
        for mahasiswa in cls.daftar_mahasiswa:
            if mahasiswa.nim == nim:
                if nama_baru:
                    mahasiswa.nama = nama_baru
                if nilai_baru is not None:
                    mahasiswa.nilai = nilai_baru
                print(f"Data dengan NIM {nim} berhasil diubah.")
                return
        print(f"Data dengan NIM {nim} tidak ditemukan.")

    @classmethod
    def tampilkan_data(cls):
        if not cls.daftar_mahasiswa:
            print("Tidak ada data mahasiswa.")
        else:
            for mahasiswa in cls.daftar_mahasiswa:
                print(f"Nama: {mahasiswa.nama}, NIM: {mahasiswa.nim}, Nilai: {mahasiswa.nilai}")


def main():
    while True:
        print("\nMenu:")
        print("1. Tambah Data")
        print("2. Hapus Data")
        print("3. Ubah Data")
        print("4. Tampilkan Data")
        print("5. Keluar")
        pilihan = input("Masukkan pilihan (1-5): ")

        if pilihan == "1":
            nama = input("Masukkan nama: ")
            nim = input("Masukkan NIM: ")
            nilai = float(input("Masukkan nilai: "))
            Mahasiswa.tambah_data(nama, nim, nilai)
        elif pilihan == "2":
            nim = input("Masukkan NIM yang akan dihapus: ")
            Mahasiswa.hapus_data(nim)
        elif pilihan == "3":
            nim = input("Masukkan NIM yang akan diubah: ")
            nama_baru = input("Masukkan nama baru (kosongkan jika tidak ingin diubah): ")
            nilai_baru = input("Masukkan nilai baru (kosongkan jika tidak ingin diubah): ")
            nilai_baru = float(nilai_baru) if nilai_baru else None
            Mahasiswa.ubah_data(nim, nama_baru, nilai_baru)
        elif pilihan == "4":
            Mahasiswa.tampilkan_data()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()