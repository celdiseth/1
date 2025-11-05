#!/usr/bin/env python
""" 

"""
import os
import pygame as pg

#expect images to be located in runtime directory.
main_dir = os.path.split(os.path.abspath(__file__))[0]
#data_dir = os.path.join(main_dir, "data")
data_dir = main_dir
sprite_image = pg.image.load(os.path.join(data_dir, "sprites.png"))
sprite_list = []

def build_sprite_list():
    sprite_size_x = 72
    sprite_size_y = 72
    columns = sprite_image.get_width()  / sprite_size_x
    rows    = sprite_image.get_height() / sprite_size_y
    columns = round(columns) 
    rows = round(rows)
    row,column = 0,0
    
    print("columns = ", columns)
    print("rows = ", rows)
    print("total sprites =", rows*columns)
    for row in range(rows):
        
        for column in range(columns):
            left = row*sprite_size_x
            top = column*sprite_size_y
            '''
            print("column = ", column)
            print("row = ", row)    
            print("top = ", top)
            print("left = ", left)     
            '''
            #show(sprite_image.subsurface((top,left),(sprite_size_x,sprite_size_y)))
            sprite_list.append(sprite_image.subsurface((top,left),(sprite_size_x,sprite_size_y)))

        

    
    '''
    while row <= rows:
        while column <= columns:
            top = row*sprite_size_x
            left = column*sprite_size_y
            #sprite_list.append(sprite_image.subsurface((top,left),sprite_size_x,sprite_size_y))
            show(sprite_image.subsurface((top,left),(sprite_size_x,sprite_size_y)))
            row+=1
            print("column = ", column)
            print("row = ", row)
            
        column+=1
    #end while
    

    for row in rows:
        
        for tile in row:
            if tile == 1:
                sx = this_col * x_stride
                sy = this_row * y_stride
                screen.blit(a_tile, (sx,sy))
                sx=+1
            this_col =+ 1
        
        this_col = 0
        this_row =+ 1'''




######Classes SUCK donkey dick -- why complicate this
class tile_layer():
    def __init__(self, layer_columns, layer_rows, sprites):
        self.layer_columns = 24
        self.layer_rows = 12

    #def set_sprites_image(self, all_sprites_image):

'''class sprite_list():
    def __init__(self, sprite_image,list):
        sprite_size_x = 72
        sprite_size_y = 72
        sprite_rect = (sprite_size_x,sprite_size_y)
        self.sprite_image = pg.image.load(os.path.join(data_dir, "sprites.png"))
        a_sprite = pg.surface.subsurface(sprite_rect)
'''



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

    #show(s)


    a_tile = pg.image.load(os.path.join(data_dir, "arraydemo.bmp"))
    tile_rect = a_tile.get_rect()
    x_stride = a_tile.get_width()
    y_stride = a_tile.get_height()
    display_rect = (x_stride * 2, y_stride*2)
    pg.display.set_mode(display_rect)
    surface = pg.Surface(display_rect)

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
                sx = this_col * x_stride
                sy = this_row * y_stride
                screen.blit(a_tile, (sx,sy))
                sx=+1
            this_col =+ 1
        
        this_col = 0
        this_row =+ 1
            
    #screen.blit(a_tile, (0,0))
    #screen.blit(a_tile,(77,77))
    print(x_stride)
    print(y_stride)
    pg.display.flip()

    while True:
        event = pg.event.wait()
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit
        if event.type in [pg.MOUSEBUTTONDOWN, pg.KEYDOWN]:
            break
def third():
    pg.init()
    s = pg.image.load(os.path.join(data_dir, "sprites.png"))
    tile_layer.layer_rows = 12
    display_rect = (622, 622)
    pg.display.set_mode(display_rect) 
    #rrr=pg.rect(120,120,22,22)
    #sprite_collection=[]
    #sprite_collection.append(s.subsurface(72,0,72*2,72))
    #sprite_collection.append(s.subsurface(0,0,72,72))
    #show(sprite_list.get(1,1))
    pg.display.flip()
    #show(sprite_collection[1])

    while True:
        event = pg.event.wait()
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit
        if event.type in [pg.MOUSEBUTTONDOWN, pg.KEYDOWN]:
            break
def fourth():
    pg.init()
    
    display_rect = (622, 622)
    pg.display.set_mode(display_rect) 
    
    pg.display.flip()

    build_sprite_list()
    while True:
        event = pg.event.wait()
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit
        if event.type in [pg.MOUSEBUTTONDOWN, pg.KEYDOWN]:
            break

if __name__ == "__main__":
    #main()
    #second()
    #third()
    fourth()
    pg.quit()