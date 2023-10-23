from itertools import count

from views import view
from cotrolers import controler
import tkinter as tk
if __name__ == "__main__":
    root = tk.Tk()
    control = controler.Controler()
    vista = view.GeneradorMatricesApp(root, control)
    root.mainloop()