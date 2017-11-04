import Tkinter as tk
import random
import time

window = tk.Tk()

def pickColor():
    return "#%06x" % random.randint(0, 0xFFFFFF)
canvas = tk.Canvas(window, width=1600, height=1600, bg=pickColor())
canvas.pack()
window.wm_title("Circles")

    
while True:
    xc = random.randint(0,1600)
    yc = random.randint(0,1600)
    r = random.randint(10,11)
    if r % 2 == 0:
        canvas.create_rectangle( xc-r, yc-r, xc+r, yc+r, fill = pickColor())
    else:
        canvas.create_oval( xc-r, yc-r, xc+r, yc+r, fill = pickColor())
    window.update()
    

window.mainloop()
    
