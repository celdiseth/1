#!/usr/bin/env python
""" 

"""
import os
import pygame as pg

#expect images to be located in runtime directory.
main_dir = os.path.split(os.path.abspath(__file__))[0]
#data_dir = os.path.join(main_dir, "data")
data_dir = main_dir



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
    #show(s)


    a_tile = pg.image.load(os.path.join(data_dir, "arraydemo.bmp"))
    tile_rect = a_tile.get_rect
    x_stride = a_tile.get_width
    y_stride = a_tile.get_height
    a_tile_row = [1,0]
    another_tile_row = [0,1]
    all_tiles = []   #representation of the tiles. each unique sprite gets a number assigned. 
    all_tiles.append(a_tile_row)
    all_tiles.append(another_tile_row)
    print(all_tiles)

    this_row = 0
    this_col = 0
    screen = pg.display.get_surface()
    for row in all_tiles:
        
        for tile in row:
            if tile == 1:
                #sx = this_col * x_stride
                #sy = this_row * y_stride
                #screen.blit(a_tile, tile_rect)
                sx=+1
            this_col =+ 1
        
        this_col = 0
        this_row =+ 1
            
    screen.blit(a_tile, (0,0))
    screen.blit(a_tile,(77,77))

    while True:
        event = pg.event.wait()
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit
        if event.type in [pg.MOUSEBUTTONDOWN, pg.KEYDOWN]:
            break


if __name__ == "__main__":
    #main()
    second()
    pg.quit()