import tkinter as tk

from Class.ComputerSimulator import ComputerSimulator

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("1000x700")
    app = ComputerSimulator(root)
    root.mainloop()
