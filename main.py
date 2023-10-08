from itertools import count

from views import presenter
from cotrolers import controler
import tkinter as tk
if __name__ == "__main__":
    root = tk.Tk()
    control = controler.Controler()
    vista = presenter.GeneradorMatricesApp(root, control)
    root.mainloop()