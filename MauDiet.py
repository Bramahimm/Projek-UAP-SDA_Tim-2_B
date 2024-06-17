import csv

class Food:
    def __init__(self, nama, kalori, berat):
        self.nama = nama
        self.kalori = kalori
        self.berat = berat

    def __repr__(self):
        return f"Nama Makanan: {self.nama}\nJumlah Kalori: {self.kalori} kcal\nBerat Makanan: {self.berat} gram"

class CalorieManager:
    def __init__(self):
        self.daftar = []

    def add_food(self, nama, kalori, berat):
        new_food = Food(nama, kalori, berat)
        self.daftar.append(new_food)
        print(f"Ditambahkan:\n {new_food}")

    def view_foods(self):
        if not self.daftar:
            print("Makanan tidak ditemukan dalam list.")
        else:
            for food in self.daftar:
                print(food)

    def update_food(self, nama, kalori_baru, berat_baru):
        for food in self.daftar:
            if food.nama == nama:
                food.kalori = kalori_baru
                food.berat = berat_baru
                print(f"Diupdate: {food}")
                return
        print("Makanan tidak ditemukan.")

    def delete_food(self, nama):
        for food in self.daftar:
            if food.nama == nama:
                self.daftar.remove(food)
                print(f"Dihapus: {food}")
                return
        print("Makanan tidak ditemukan.")

    def search_food(self, nama):
        for food in self.daftar:
            if food.nama == nama:
                return food
        return None

    def sort_foods_by_calories(self):
        self.daftar.sort(key=lambda food: food.kalori)
        print("Makanan diurutkan berdasarkan kalori.")

    def export_to_csv(self, nama_file):
        with open(nama_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Nama Makanan", "Kalorinya", "Berat"])
            for food in self.daftar:
                writer.writerow([food.nama, food.kalori, food.berat])
        print(f"Data berhasil diexport dengan nama {nama_file}")

    def import_from_csv(self, path_file):
        try:
            with open(path_file, mode='r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if row:
                        nama, kalori, berat = row
                        self.add_food(nama, int(kalori), int(berat))
            print(f"Data diimport dari {path_file}")
        except FileNotFoundError:
            print(f"File {path_file} tidak ditemukan.")
        except Exception as e:
            print(f"Error tidak diketahui: {e}")

def main():
    manager = CalorieManager()

    while True:
        print("\nCalorie Manager")
        print("1. Tambah Makanan")
        print("2. Lihat Makanan")
        print("3. Perbarui Makanan")
        print("4. Hapus Makanan")
        print("5. Cari Makanan")
        print("6. Urutin Makanan berdasarkan Kalori")
        print("7. Export ke CSV")
        print("8. Import dari CSV")
        print("9. Exit")
        
        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            nama = input("Masukkan nama makanan: ")
            kalori = int(input("Jumlah kalori: "))
            berat = int(input("Masukkan berat makanan (gram): "))
            manager.add_food(nama, kalori, berat)
        elif pilihan == '2':
            manager.view_foods()
        elif pilihan == '3':
            nama = input("Nama makanan yang akan diedit: ")
            kalori_baru = int(input("Jumlah kalori baru: "))
            berat_baru = int(input("Berat baru (gram): "))
            manager.update_food(nama, kalori_baru, berat_baru)
        elif pilihan == '4':
            nama = input("Nama makanan yang akan dihapus: ")
            manager.delete_food(nama)
        elif pilihan == '5':
            nama = input("Nama makanan yang akan dicari: ")
            food = manager.search_food(nama)
            if food:
                print(f"Ketemu: {food}")
            else:
                print("Makanan tidak ditemukan.")
        elif pilihan == '6':
            manager.sort_foods_by_calories()
        elif pilihan == '7':
            nama_file = input("Masukkan nama file untuk diexport: ")
            manager.export_to_csv(nama_file)
        elif pilihan == '8':
            path_file = input("Masukkan path file untuk diimport: ")
            manager.import_from_csv(path_file)
        elif pilihan == '9':
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
