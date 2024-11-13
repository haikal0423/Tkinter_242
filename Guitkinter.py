import tkinter as tk
from tkinter import messagebox

# Fungsi untuk memvalidasi input dan menampilkan hasil prediksi
def hasil_prediksi():
    try:
        # Mengecek setiap nilai yang diinput di entries
        for entry in entries:
            nilai = int(entry.get())  # Mengambil nilai dari kotak input dan mengubahnya jadi integer
            if not (0 <= nilai <= 100):  # Cek apakah nilai antara 0 sampai 100
                raise ValueError("Nilai harus antara 0 dan 100.")  # Kalau tidak, munculkan error
        # Kalau semua nilai valid, tampilkan hasil prediksi
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError as ve:
        # Munculkan pesan error kalau ada input yang tidak valid
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

# Buat jendela utama aplikasi
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Judul jendela
root.geometry("500x600")  # Ukuran jendela
root.configure(bg="#eb3434")  # Warna background jendela

# Label Judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 18, "bold"), bg="#eb3434")
judul_label.pack(pady=20)  # Posisi label judul dengan jarak atas-bawah

# Frame untuk input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#eb3434")
frame_input.pack(pady=10)  # Jarak frame dari atas

# List untuk menyimpan semua kotak input nilai
entries = []
for i in range(10):
    # Label untuk setiap input nilai mata pelajaran
    label = tk.Label(frame_input, text=f"Nilai Mata Pelajaran {i + 1}:", font=("Arial", 12), bg="#eb3434")
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")  # Atur posisi label dalam grid
    
    # Kotak input untuk setiap nilai
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))
    entry.grid(row=i, column=1, padx=10, pady=5)  # Atur posisi kotak input dalam grid
    entries.append(entry)  # Simpan kotak input ke dalam list entries

# Tombol untuk melihat hasil prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi, font=("Arial", 12, "bold"), bg="#4CAF50", fg="black")
prediksi_button.pack(pady=30)  # Posisi tombol dengan jarak atas-bawah

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 14, "italic", "bold"), fg="black", bg="#eb3434")
hasil_label.pack(pady=20)  # Jarak label hasil dari elemen lainnya

# Menjalankan aplikasi
root.mainloop()  # Mulai event loop aplikasi, supaya jendela tetap muncul