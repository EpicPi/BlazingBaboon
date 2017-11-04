import pygame
import pygame.camera
import Tkinter as tk
import Image
import tkMessageBox
import random
from pygame.locals import *

DEVICE = '/dev/video0'
SIZE = (640, 480)
FILENAME = 'capture.png'

def camstream():
    count = 0
    pygame.init()
    pygame.camera.init()
    display = pygame.display.set_mode(SIZE, 0)
    camera = pygame.camera.Camera(DEVICE, SIZE)
    camera.start()
    screen = pygame.surface.Surface(SIZE, 0, display)

    capture = True
    while capture:
        screen = camera.get_image(screen)
        display.blit(screen, (0,0))
        pygame.display.flip()
        pygame.time.wait(100)
        pygame.image.save(screen, "frame%d.jpg" % count)
        count += 1
        if count > 20:
            break


        # for event in pygame.event.get():
        #     if event.type == QUIT:
        #         capture = False
        #     elif event.type == KEYDOWN and event.key == K_x:
        #         pygame.image.save(screen, "frame%d.jpg" % count)
        #         count += 1
    camera.stop()
    pygame.quit()
    return
num = 0
def looper():
    if __name__ == '__main__':
        camstream()
    Image.open('frame20.jpg').show()
    window = tk.Tk()
    canvas = tk.Canvas(window, width=300, height=300, bg="yellow")
    canvas.pack()
    window.wm_title("Warning")
    canvas.create_text(150, 150, width = 100, text = "you have been staring at your screen for too long")
    window.mainloop()
while num == 0:
    looper()
    num = 1

