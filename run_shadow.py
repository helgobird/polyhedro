#!/usr/bin/env -S python3 -B

from time import time
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr


tk = TkDrawer()
try:
    for name in ["tri_hor", "ccc", "cube", "box", "king", "cow"]:
        print("=============================================================")
        print(f"Начало работы с полиэдром '{name}'")
        start_time = time()
        pol = Polyedr(f"data/{name}.geom")
        pol.draw(tk)
        pol.ihwfunc()
        delta_time = time() - start_time
        print("Сумма площадей проеций граней,", end=' ')
        print(f"удовлетворяющих условию задачи, равно {pol.oxyarea}")
        print(f"Изображение полиэдра '{name}' заняло {delta_time} сек.")
        input("Hit 'Return' to continue -> ")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
