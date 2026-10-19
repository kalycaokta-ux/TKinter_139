import tkinter as tk

#root menjadi wadah utama tempat semua komponen GUI diletakkan.
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("450x550")

#root = wadahnya, sedangkan judul = komponen yang dimasukkan ke wadah tersebut.
judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 14, "bold")
)
judul.pack(pady=15)

#frame diperlukan supaya 10 nama mata pelajaran dan 10 kotak input bisa dikelompokkan 
#menjadi satu bagian.
frame = tk.Frame(root)
frame.pack()

#list digunakan agar tidak perlu menulis kode label 
#dan input sebanyak 10 kali secara manual.
mapel = [
    "Matematika",
    "Bahasa Indonesia",
    "Bahasa Inggris",
    "Fisika",
    "Kimia",
    "Biologi",
    "Ekonomi",
    "Geografi",
    "Sejarah",
    "Informatika"
]

#untuk menyimpan semua kotak input yang dibuat.
nilai = []

#jalankan kode di dalamnya sebanyak 10 kali, var i akan bernilai dari 0 - 9
# tk label = membuat label mata pelajaran
#grid = mengatur posisi label
#tk.Entry = agar pengguna bisa mengetikkan nilai mata pelajaran
#kotak input ditempatkan pada baris yang sama dengan label, tetapi di kolom kedua
#masukkan kotak input yang baru dibuat ke dalam list nilai
#Dengan begitu, pengulangan menghasilkan 10 baris, masing-masing berisi nama mata pelajaran dan kotak input.

for i in range(10):
    label = tk.label(
        frame,
        text=mapel[i],
        width=18,
        anchor="w"
    )
    
    label.grid(row=i, column=0, padx=5, pady=5)

    entry = tk.Entry(frame, width=20)
    entry.grid(row=i, column=1, padx=5, pady=5)

    nilai.append(entry)
 
#instruksi tugas menyatakan hasil harus tetap Teknologi Informasi apa pun inputnya.
def prediksi():
    hasil.config(text="Teknologi Informasi")

tombol = tk.Button(
    root,
    text="Hasil Prediksi",
    command=prediksi
)
    
tombol.pack(pady=20)

hasil = tk.Label(root, text="Hasil Prediksi:")
hasil.pack()

root.mainloop()