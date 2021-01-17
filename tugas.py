import tkinter as tk

master = tk.Tk()
master.title("Project Akhir")
master.geometry("300x300")

# cek ketersediaan kertas
tk.Label(master, text="Check Paper Availability", font = ('Google Sans','13', 'bold')).grid(row=0, column=0, columnspan = 4)
tk.Label(master, text="A4", font = ('Google Sans','10')).grid(row=1, column=0, sticky=tk.E)
tk.Entry(master, justify="left").grid(row=1, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text = "add").grid(row=1, column = 3, sticky=tk.W)

tk.Label(master, text="A3", font = ('Google Sans','10')).grid(row=2, column=0, sticky=tk.E)
tk.Entry(master, justify="left").grid(row=2, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text = "add").grid(row=2, column = 3, sticky=tk.W)

tk.Label(master, text="B1", font = ('Google Sans','10')).grid(row=3, column=0, sticky=tk.E)
tk.Entry(master, justify="left").grid(row=3, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text = "add").grid(row=3, column = 3, sticky=tk.W)

tk.Label(master, text="B2", font = ('Google Sans','10')).grid(row=4, column=0, sticky=tk.E)
tk.Entry(master, justify="left").grid(row=4, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text = "add").grid(row=4, column = 3, sticky=tk.W)

# cek ketersediaan Tinta
tk.Label(master, text="Check Ink Availability", font = ('Google Sans','13', 'bold')).grid(row=5, column=0, columnspan = 4, sticky = tk.W)
tk.Label(master, text="Dark", font = ('Google Sans','10')).grid(row=6, rowspan = 2, column=0, sticky=tk.E+tk.N)
tk.Entry(master, justify="left").grid(row=6, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text = "add").grid(row=6, column = 3, sticky=tk.W)

# cek sudah mencetak berapa kali cetak
tk.Label(master, text="Check Number of Prints", font = ('Google Sans','13', 'bold')).grid(row=7, column=0, columnspan = 4, pady = 15, sticky = tk.W)
tk.Label(master, text="Total", font = ('Google Sans','10')).grid(row=8, column=0, sticky=tk.E)
tk.Entry(master, justify="left").grid(row=8, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
# tk.Button(master, text = "add").grid(row=8, column = 3, sticky=tk.W)

# Tombol print
tk.Button(master, text = "PRINT", width = 15,  font = ('Google Sans','8', 'bold')).grid(row=9, column = 0, columnspan = 4, pady = 10, sticky=tk.N+tk.E+tk.S+tk.W)

tk.mainloop()
