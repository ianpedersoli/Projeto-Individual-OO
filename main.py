import tkinter as tk
from package.controllers.interface import Interface

if __name__ == "__main__":
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()