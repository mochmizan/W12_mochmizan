#Soal 3
from tkinter import *

root = Tk()

# Judul dan Ukuran
root.title("Aplikasi Paint")
root.geometry("500x500")

# Fungsi mewarna
def paint(event):
    # Koordinat mouse
    x1, y1, x2, y2 = (event.x - 2), (event.y - 2), (event.x + 2), (event.y + 2)
    # Warna
    Colour = "#000000"
    # Membuat garis
    w.create_line(x1, y1, x2, y2, fill=Colour)

drawing_frame = Frame(root)
drawing_frame.grid(row=0, column=0, pady=10, padx=10, sticky="ew")
root.grid_columnconfigure(0, weight=1)

# Label
instruction_label = Label(drawing_frame, text="Klik dan Drag untuk Menggambar")
instruction_label.pack()

# Canvas
w = Canvas(drawing_frame, width=400, height=250, highlightthickness=1,
           highlightbackground="black", bg="white")
w.pack(pady=5)
w.bind("<B1-Motion>", paint)

# fungsi hapus entry
def hapus():
    entry.delete(0, END)

# ---  Text, Entry, dan Button ---
jlabel = Label(root, text="Nama:")
jlabel.grid(row=2, column=0, sticky="w", padx=45, pady=(0, 10))
nama_text = Text(root, height = 1, width = 6)
nama_text.grid(row=2, column=0, padx=0, pady=(0, 10))
reset_button = Button(root, text="Reset Entry", command=hapus)
reset_button.grid(row=3, column=0, sticky="w", padx=45, pady=(0, 10))
entry = Entry(root, width=30)
entry.grid(row=3, column=0, padx=45, pady=(0, 10))

mainloop()
