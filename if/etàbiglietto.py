import tkinter as tk
window=tk.Tk()

lblbiglietto=tk.Label(text="Costo del biglietto",
            fg="white",
            bg="gray").pack()

txtbiglietto=tk.Entry(fg="yellow",bg="blue",width=50).pack()

lbleta=tk.Label(text="Età",
        fg="white",
        bg="red").pack()

txteta=tk.Entry(fg="yellow",bg="blue",width=50).pack()

btncalcolo=tk.Button(text="Calcola",
            fg="white",
            bg="red",
            height=10,
            width=30).pack()
window.mainloop()