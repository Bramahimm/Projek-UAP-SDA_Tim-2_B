import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv

class Food:
    def __init__(self, nama, kalori, berat):
        self.nama = nama
        self.kalori = kalori
        self.berat = berat

    def __repr__(self):
        return f"Nama Makanan: {self.nama}\nJumlah Kalori: {self.kalori} kkal\nBerat Makanan: {self.berat} gram\n"

class CalorieManager:
    def __init__(self):
        self.daftar = []

    def tambahMakanan(self, nama, kalori, berat):
        new_food = Food(nama, kalori, berat)
        self.daftar.append(new_food)
        return new_food

    def lihatMakanan(self):
        return self.daftar

    def perbarui(self, nama, kalori_baru, berat_baru):
        for food in self.daftar:
            if food.nama == nama:
                food.kalori = kalori_baru
                food.berat = berat_baru
                return food
        return None

    def hapusMakanan(self, nama):
        for food in self.daftar:
            if food.nama == nama:
                self.daftar.remove(food)
                return food
        return None

    def cariMakanan(self, nama):
        for food in self.daftar:
            if food.nama == nama:
                return food
        return None

    def sortingMakanan(self):
        self.daftar.sort(key=lambda x: x.kalori)

    def exporKecsv(self, nama_file):
        with open(nama_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Nama Makanan", "Kalori", "Berat"])
            for food in self.daftar:
                writer.writerow([food.nama, food.kalori, food.berat])

    def imporDaricsv(self, path_file):
        try:
            with open(path_file, mode='r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    if row:
                        nama, kalori, berat = row
                        self.tambahMakanan(nama, int(kalori), int(berat))
        except FileNotFoundError:
            return f"File {path_file} tidak ditemukan."
        except Exception as e:
            return f"Error tidak diketahui: {e}"
        return f"Data diimport dari {path_file}"

class CalorieManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calorie Manager")
        self.manager = CalorieManager()
        self.setup_ui()

    def setup_ui(self):
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        ttk.Label(frame, text="Nama Makanan").grid(row=0, column=0, sticky=tk.W)
        self.nama_entry = ttk.Entry(frame, width=20)
        self.nama_entry.grid(row=0, column=1, sticky=tk.W)

        ttk.Label(frame, text="Kalori").grid(row=1, column=0, sticky=tk.W)
        self.kalori_entry = ttk.Entry(frame, width=20)
        self.kalori_entry.grid(row=1, column=1, sticky=tk.W)

        ttk.Label(frame, text="Berat (gram)").grid(row=2, column=0, sticky=tk.W)
        self.berat_entry = ttk.Entry(frame, width=20)
        self.berat_entry.grid(row=2, column=1, sticky=tk.W)

        ttk.Button(frame, text="Tambah Makanan", command=self.tambah_makanan).grid(row=3, column=0, columnspan=2)
        ttk.Button(frame, text="Lihat Makanan", command=self.lihat_makanan).grid(row=4, column=0, columnspan=2)
        ttk.Button(frame, text="Impor Data CSV", command=self.impor_data_csv).grid(row=5, column=0, columnspan=2)
        ttk.Button(frame, text="Ekspor Data CSV", command=self.ekspor_data_csv).grid(row=6, column=0, columnspan=2)

        self.makanan_listbox = tk.Listbox(frame, width=50, height=10)
        self.makanan_listbox.grid(row=7, column=0, columnspan=2)

        ttk.Label(frame, text="Nama Makanan yang akan dihapus").grid(row=8, column=0, sticky=tk.W)
        self.nama_hapus_entry = ttk.Entry(frame, width=20)
        self.nama_hapus_entry.grid(row=8, column=1, sticky=tk.W)

        ttk.Button(frame, text="Hapus Makanan", command=self.hapus_makanan).grid(row=9, column=0, columnspan=2)

        ttk.Label(frame, text="Nama Makanan yang akan diupdate").grid(row=10, column=0, sticky=tk.W)
        self.nama_update_entry = ttk.Entry(frame, width=20)
        self.nama_update_entry.grid(row=10, column=1, sticky=tk.W)

        ttk.Label(frame, text="Kalori Baru").grid(row=11, column=0, sticky=tk.W)
        self.kalori_update_entry = ttk.Entry(frame, width=20)
        self.kalori_update_entry.grid(row=11, column=1, sticky=tk.W)

        ttk.Label(frame, text="Berat Baru (gram)").grid(row=12, column=0, sticky=tk.W)
        self.berat_update_entry = ttk.Entry(frame, width=20)
        self.berat_update_entry.grid(row=12, column=1, sticky=tk.W)

        ttk.Button(frame, text="Update Makanan", command=self.update_makanan).grid(row=13, column=0, columnspan=2)

    def tambah_makanan(self):
        nama = self.nama_entry.get()
        kalori = self.kalori_entry.get()
        berat = self.berat_entry.get()
        if not nama or not kalori or not berat:
            messagebox.showwarning("Input Salah", "Semua kolom harus diisi.")
            return
        try:
            kalori = int(kalori)
            berat = int(berat)
        except ValueError:
            messagebox.showwarning("Input Salah", "Kalori dan Berat harus berupa angka.")
            return
        self.manager.tambahMakanan(nama, kalori, berat)
        self.lihat_makanan()
        self.nama_entry.delete(0, tk.END)
        self.kalori_entry.delete(0, tk.END)
        self.berat_entry.delete(0, tk.END)

    def lihat_makanan(self):
        self.makanan_listbox.delete(0, tk.END)
        for makanan in self.manager.lihatMakanan():
            self.makanan_listbox.insert(tk.END, f"Nama: {makanan.nama} - Kalori: {makanan.kalori} kkal - Berat: {makanan.berat} gram")

    def hapus_makanan(self):
        nama = self.nama_hapus_entry.get()
        if not nama:
            messagebox.showwarning("Input Salah", "Nama harus diisi.")
            return
        self.manager.hapusMakanan(nama)
        self.lihat_makanan()
        self.nama_hapus_entry.delete(0, tk.END)

    def update_makanan(self):
        nama = self.nama_update_entry.get()
        kalori = self.kalori_update_entry.get()
        berat = self.berat_update_entry.get()
        if not nama or not kalori or not berat:
            messagebox.showwarning("Input Salah", "Semua kolom harus diisi.")
            return
        try:
            kalori = int(kalori)
            berat = int(berat)
        except ValueError:
            messagebox.showwarning("Input Salah", "Kalori dan Berat harus berupa angka.")
            return
        self.manager.perbarui(nama, kalori, berat)
        self.lihat_makanan()
        self.nama_update_entry.delete(0, tk.END)
        self.kalori_update_entry.delete(0, tk.END)
        self.berat_update_entry.delete(0, tk.END)

    def impor_data_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            message = self.manager.imporDaricsv(file_path)
            messagebox.showinfo("Impor Data", message)
            self.lihat_makanan()

    def ekspor_data_csv(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.manager.exporKecsv(file_path)
            messagebox.showinfo("Ekspor Berhasil", f"Data berhasil diekspor ke {file_path}")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalorieManagerApp(root)
    root.mainloop()
