#!/usr/bin/env python
""" 

"""
import os
import pygame as pg

#expect images to be located in runtime directory.
main_dir = os.path.split(os.path.abspath(__file__))[0]
#data_dir = os.path.join(main_dir, "data")
data_dir = main_dir


class tile(pg.sprite.Sprite):
    def __init__(self, image, x, y, id):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(data_dir, "arraydemo.bmp"))
        self.id = 0

class window(pg.Surface):
    def __init__(self, tiles):
        pg.Surface.__init__(self)
        self.tiles =[]
        

    def add_tile(self, tile):
        window.tiles[tile.x,tile.y] = tile
        self.


######Classes SUCK donkey dick -- why complicate this

def show(image):
    screen = pg.display.get_surface()
    screen.fill((255, 255, 255))
    screen.blit(image, (0, 0))
    pg.display.flip()
    while True:
        event = pg.event.wait()
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit
        if event.type in [pg.MOUSEBUTTONDOWN, pg.KEYDOWN]:
            break


def main():
    pg.init()

    pg.display.set_mode((255, 255))
    surface = pg.Surface((255, 255))

    pg.display.flip()

    # Create the PixelArray.
    ar = pg.PixelArray(surface)

    # Do some easy gradient effect.
    for y in range(255):
        r, g, b = y, y, y
        ar[:, y] = (r, g, b)
    del ar
    show(surface)

    
    

def second():
    pg.init()
    s = pg.image.load(os.path.join(data_dir, "arraydemo.bmp"))
    pg.display.set_mode((255, 255))
    surface = pg.Surface((255, 255))
    show(s)

if __name__ == "__main__":
    #main()
    second()
    pg.quit()