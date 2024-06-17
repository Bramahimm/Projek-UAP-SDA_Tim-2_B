import csv

class Food:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f"{self.name}: {self.calories} Kalori"

class CalorieManager:
    def __init__(self):
        self.food_list = []

    def add_food(self, name, calories):
        new_food = Food(name, calories)
        self.food_list.append(new_food)
        print(f"Ditambahkan: {new_food}")

    def view_foods(self):
        if not self.food_list:
            print("Makanan tidak ditemukan dalam list.")
        else:
            for food in self.food_list:
                print(food)

    def update_food(self, name, new_calories):
        for food in self.food_list:
            if food.name == name:
                food.calories = new_calories
                print(f"Diupdate: {food}")
                return
        print("Makanan tidak ditemukan.")

    def delete_food(self, name):
        for food in self.food_list:
            if food.name == name:
                self.food_list.remove(food)
                print(f"Ditambahkan: {food}")
                return
        print("Makanan tidak ditemukan.")

    def search_food(self, name):
        for food in self.food_list:
            if food.name == name:
                return food
        return None

    def sort_foods_by_calories(self):
        self.food_list.sort(key=lambda food: food.calories)
        print("Makanan diurutkan berdasarkan kalori.")

    def export_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Nama", "Kalori"])
            for food in self.food_list:
                writer.writerow([food.name, food.calories])
        print(f"Data berhasil di export dengan nama {filename}")

    def import_from_csv(self, filepath):
        try:
            with open(filepath, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  
                for row in reader:
                    if row:
                        name, calories = row
                        self.add_food(name, int(calories))
            print(f"Data diimport dari {filepath}")
        except FileNotFoundError:
            print(f"File {filepath} tidak ditemukan.")
        except Exception as e:
            print(f"Error tidak diketahui: {e}")

def main():
    manager = CalorieManager()

    while True:
        print("\nCalorie Manager")
        print("1. Add food")
        print("2. View foods")
        print("3. Update food")
        print("4. Delete food")
        print("5. Search food")
        print("6. Sort foods by calories")
        print("7. Export to CSV")
        print("8. Import from CSV")
        print("9. Exit")
        
        choice = input("Masukan pilihan: ")

        if choice == '1':
            name = input("Masukan nama makanan: ")
            calories = int(input("Jumlah kalori: "))
            manager.add_food(name, calories)
        elif choice == '2':
            manager.view_foods()
        elif choice == '3':
            name = input("Nama makanan yang akan diedit: ")
            new_calories = int(input("Jumlah kalori baru: "))
            manager.update_food(name, new_calories)
        elif choice == '4':
            name = input("Nama makanan yang akan dihapus: ")
            manager.delete_food(name)
        elif choice == '5':
            name = input("Nama makanan yang akan dicari: ")
            food = manager.search_food(name)
            if food:
                print(f"Ketemu: {food}")
            else:
                print("Makanan tidak ditemukan.")
        elif choice == '6':
            manager.sort_foods_by_calories()
        elif choice == '7':
            filename = input("Masukan nama file CSV yang akan diexport: ")
            manager.export_to_csv(filename)
        elif choice == '8':
            filepath = input("Masukkan path file CSV untuk mengimpor: ")
            manager.import_from_csv(filepath)
        elif choice == '9':
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
