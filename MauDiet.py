import csv

class Food:
    def __init__(self, nama, kalori, berat):
        self.nama = nama
        self.kalori = kalori
        self.berat = berat

    def __repr__(self):
        return f">Nama Makanan: {self.nama}\nJumlah Kalori: {self.kalori} kkal\nBerat Makanan: {self.berat} gram\n"

class CalorieManager:
    def __init__(self):
        self.daftar = []

    def tambahMakanan(self, nama, kalori, berat):
        new_food = Food(nama, kalori, berat)
        self.daftar.append(new_food)
        print(f"\n\nDitambahkan:\n{new_food}")

    def lihatMakanan(self):
        if not self.daftar:
            print("Makanan tidak ditemukan dalam list.")
        else:
            for food in self.daftar:
                print(food)

    def perbarui(self, nama, kalori_baru, berat_baru):
        for food in self.daftar:
            if food.nama == nama:
                food.kalori = kalori_baru
                food.berat = berat_baru
                print(f"Diupdate: {food}")
                return
        print("Makanan tidak ditemukan.")

    def hapusMakanan(self, nama):
        for food in self.daftar:
            if food.nama == nama:
                self.daftar.remove(food)
                print(f"Dihapus: {food}")
                return
        print("Makanan tidak ditemukan.")

    def cariMakanan(self, nama):
        for food in self.daftar:
            if food.nama == nama:
                return food
        return None

    def sortingMakanan(self):
        angka = len(self.daftar)
        if angka == 0:
            print("Tidak ada makanan untuk diurutkan.")
            return
        
        for i in range(angka):
            for j in range(0, angka-i-1):
                if self.daftar[j].kalori > self.daftar[j+1].kalori:
                    self.daftar[j], self.daftar[j+1] = self.daftar[j+1], self.daftar[j]
        
        print("\n\nBerikut adalaah Makananmu yang udah diurutin berdasarkan kalori :")
        self.lihatMakanan()

    def exporKecsv(self, nama_file):
        with open(nama_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Nama Makanan", "Kalorinya", "Berat"])
            for food in self.daftar:
                writer.writerow([food.nama, food.kalori, food.berat])
        print(f"Data berhasil diexport dengan nama {nama_file}")

    def imporDaricsv(self, path_file):
        try:
            with open(path_file, mode='r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if row:
                        nama, kalori, berat = row
                        self.tambahMakanan(nama, int(kalori), int(berat))
            print(f"Data diimport dari {path_file}")
        except FileNotFoundError:
            print(f"File {path_file} tidak ditemukan.")
        except Exception as e:
            print(f"Error tidak diketahui: {e}")

def main():
    manager = CalorieManager()

    while True:
        print("========================================")
        print("||          <Calorie Manager>         ||")
        print("||>>>>>>>>>>>>>>>>>||<<<<<<<<<<<<<<<<<||")
        print("||1. Tambah Makanan                   ||")
        print("||2. Lihat Makanan                    ||")
        print("||3. Perbarui Makanan                 ||")
        print("||4. Hapus Makanan                    ||")
        print("||5. Cari Makanan                     ||")
        print("||6. Urutin Makanan berdasarkan Kalori||")
        print("||7. Export ke CSV                    ||")
        print("||8. Import dari CSV                  ||")
        print("||9. Keluar                           ||")
        print("========================================")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            penentu = True
            while penentu:
                try:
                    nama = input("Masukkan nama makanan: ")
                    kalori = int(input("Jumlah kalori: "))
                    berat = int(input("Masukkan berat makanan (gram): "))
                    manager.tambahMakanan(nama, kalori, berat)
                except ValueError:
                    print("\n\n>>> Input tidak valid. Kembali ke menu utama <<<\n\n")
                    penentu = False
                continue
            
        elif pilihan == '2':
            manager.lihatMakanan()
            
        elif pilihan == '3':
            nama = input("Nama makanan yang akan diedit: ")
            kalori_baru = int(input("Jumlah kalori baru: "))
            berat_baru = int(input("Berat baru (gram): "))
            manager.perbarui(nama, kalori_baru, berat_baru)
            
        elif pilihan == '4':
            nama = input("Nama makanan yang akan dihapus: ")
            manager.hapusMakanan(nama)
            
        elif pilihan == '5':
            nama = input("Nama makanan yang akan dicari: ")
            food = manager.cariMakanan(nama)
            if food:
                print(f"Ketemu: {food}")
            else:
                print("Makanan tidak ditemukan.")
        elif pilihan == '6':
            manager.sortingMakanan()
            
        elif pilihan == '7':
            nama_file = input("Masukkan nama file untuk diexport: ")
            manager.exporKecsv(nama_file)
            
        elif pilihan == '8':
            path_file = input("Masukkan path file untuk diimport: ")
            manager.imporDaricsv(path_file)
            
        elif pilihan == '9':
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
