import tkinter as tk

def jendelaInput(): 
    def saveInput1():
        a4 = inputA4.get()
        viewerA4.config(state='normal')
        viewerA4.delete(0, 'end')
        viewerA4.insert(0, a4)
        viewerA4.config(state='readonly')
        inputWindow.destroy()
    inputWindow = tk.Tk()
    inputWindow.title("Configuration Paper A4")
    inputWindow.geometry("250x120")
    inputA4 = tk.Entry(inputWindow, justify="center")

    tk.Label(inputWindow, text="Number : ").grid(row=0, column=0, sticky=tk.W)
    inputA4.grid(row=0, column=1, sticky=tk.N+tk.E+tk.S+tk.W)

    tk.Button(inputWindow, text="Save Changes", command=saveInput1).grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky=tk.E+tk.W)

def configPaper2():
    def saveInput2():
        a3 = inputA3.get()
        viewerA3.config(state='normal')
        viewerA3.delete(0, 'end')
        viewerA3.insert(0, a3)
        viewerA3.config(state='readonly')
        inputWindow2.destroy()
    inputWindow2 = tk.Tk()
    inputWindow2.title("Configuration Paper A3")
    inputWindow2.geometry("250x120")
    inputA3 = tk.Entry(inputWindow2, justify="center")

    tk.Label(inputWindow2, text="Number : ").grid(row=0, column=0, sticky=tk.W)
    inputA3.grid(row=0, column=1, sticky=tk.N+tk.E+tk.S+tk.W)

    tk.Button(inputWindow2, text="Save Changes", command=saveInput2).grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky=tk.E+tk.W)

def configPaper3():
    def saveInput3():
        b1 = inputB1.get()
        viewerB1.config(state='normal')
        viewerB1.delete(0, 'end')
        viewerB1.insert(0, b1)
        viewerB1.config(state='readonly')
        inputWindow3.destroy()
    inputWindow3 = tk.Tk()
    inputWindow3.title("Configuration Paper B1")
    inputWindow3.geometry("250x120")
    inputB1 = tk.Entry(inputWindow3, justify="center")

    tk.Label(inputWindow3, text="Number : ").grid(row=0, column=0, sticky=tk.W)
    inputB1.grid(row=0, column=1, sticky=tk.N+tk.E+tk.S+tk.W)

    tk.Button(inputWindow3, text="Save Changes", command=saveInput3).grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky=tk.E+tk.W)

def configPaper4():
    def saveInput4():
        b2 = inputB2.get()
        viewerB2.config(state='normal')
        viewerB2.delete(0, 'end')
        viewerB2.insert(0, b2)
        viewerB2.config(state='readonly')
        inputWindow4.destroy()
    inputWindow4 = tk.Tk()
    inputWindow4.title("Configuration Paper B2")
    inputWindow4.geometry("250x120")
    inputB2 = tk.Entry(inputWindow4, justify="center")

    tk.Label(inputWindow4, text="Number : ").grid(row=0, column=0, sticky=tk.W)
    inputB2.grid(row=0, column=1, sticky=tk.N+tk.E+tk.S+tk.W)

    tk.Button(inputWindow4, text="Save Changes", command=saveInput4).grid(row=2, column=0, columnspan=2, padx=20, pady=5, sticky=tk.E+tk.W)

def naik():
    global penambahan1
    penambahan1 += 1
    numberPrint3.config(state='normal')
    numberPrint3.delete(0,5)
    numberPrint3.insert(0,penambahan1)
    numberPrint3.config(state='readonly')
    if (penambahan1 >= 24):
        penambahan1 = 24
        numberPrint3.delete(0,5)
        numberPrint3.insert(0,penambahan1) #jika sudah maks

def turun():
    global penambahan2
    penambahan2 -= 1
    viewerInk.config(state='normal')
    viewerInk.delete(0,5)
    viewerInk.insert(0,penambahan2)
    viewerInk.config(state='readonly')
    if (penambahan2 <= 1):
        penambahan2 = 1
        viewerInk.delete(0,5)
        viewerInk.insert(0, penambahan2)

master = tk.Tk()
master.title("Monitor")
master.geometry("230x350")

viewerA4 = tk.Entry(master, justify="center")
viewerA4.insert(0, 0)
viewerA3 = tk.Entry(master, justify="center")
viewerA3.insert(0, 0)
viewerB1 = tk.Entry(master, justify="center")
viewerB1.insert(0, 0)
viewerB2 = tk.Entry(master, justify="center")
viewerB2.insert(0, 0)
viewerInk = tk.Entry(master, justify="center")
viewerInk.insert(0,25)
numberPrint3 = tk.Entry(master, justify="center")
numberPrint3.insert(0, 0)
status = tk.Entry(master)

tk.Label(master, text="Check Paper Availability", font = ('Google Sans','13', 'bold')).grid(row=0, column=0, columnspan = 4)
# cek ketersediaan kertas
tk.Label(master, text="A4").grid(row=1, column=0, sticky=tk.E)
viewerA4.grid(row=1, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text = "add", command = jendelaInput).grid(row=1, column = 3, sticky=tk.W)

tk.Label(master, text="A3").grid(row=2, column=0, sticky=tk.E)
viewerA3.grid(row=2, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text = "add", command = configPaper2).grid(row=2, column = 3, sticky=tk.W)

tk.Label(master, text="B1").grid(row=3, column=0, sticky=tk.E)
viewerB1.grid(row=3, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text = "add", command = configPaper3).grid(row=3, column = 3, sticky=tk.W)

tk.Label(master, text="B2").grid(row=4, column=0, sticky=tk.E)
viewerB2.grid(row=4, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
tk.Button(master, text = "add", command = configPaper4).grid(row=4, column = 3, sticky=tk.W)

# cek ketersediaan Tinta
tk.Label(master).grid(row = 6, column = 0)
tk.Label(master, text="Check Ink Availability", font = ('Google Sans','13', 'bold')).grid(row=7, column=0, columnspan = 4, sticky = tk.W)
tk.Label(master, text="Black").grid(row=8, column=0, sticky=tk.E)
tk.Button(master, text = "use", command = turun).grid(row=8, column = 3, sticky=tk.W)
viewerInk.grid(row=8, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
penambahan2 = int(viewerInk.get())

# cek sudah mencetak berapa kali cetak
tk.Label(master).grid(row = 9, column = 0)
tk.Label(master, text="Check Number of Prints", font = ('Google Sans','13', 'bold')).grid(row=10, column=0, columnspan = 4, sticky = tk.W)
tk.Label(master, text="Total").grid(row=11, column=0, sticky=tk.E)
numberPrint3.grid(row=11, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
penambahan = int(numberPrint3.get())

# Tombol print
tk.Button(master, text = "PRINT", command = naik, width = 15, font = ('Google Sans','8', 'bold')).grid(row=13, column = 0, columnspan = 4, pady = 10, padx = 5, sticky=tk.N+tk.E+tk.S+tk.W)

viewerA4.config(state='readonly')
viewerA3.config(state='readonly')
viewerB1.config(state='readonly')
viewerB2.config(state='readonly')
viewerInk.config(state='readonly')
numberPrint3.config(state='readonly')

tk.mainloop()
