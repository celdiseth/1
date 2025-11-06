import os
import pygame as pg
import random


pg.init()

sprite_size_x = 72
sprite_size_y = 72
number_of_sprites =0
WINDOW_HEIGHT = 800
WINDOW_WIDTH  = 600
NUMBER_TILES_LR = round(WINDOW_WIDTH / sprite_size_x) + 1 #draw a little extra offscreen
NUMBER_TILES_UD = round(WINDOW_HEIGHT / sprite_size_y) +1

pg.display.set_mode((WINDOW_HEIGHT,WINDOW_WIDTH))
#expect images to be located in runtime directory.
main_dir = os.path.split(os.path.abspath(__file__))[0]
#data_dir = os.path.join(main_dir, "data")
data_dir = main_dir
sprite_image = pg.image.load(os.path.join(data_dir, "sprites.png")).convert_alpha()
sprite_list = []
layer_background = pg.surface
layer_foreground = pg.surface

def build_sprite_list():
    sprite_size_x = 72
    sprite_size_y = 72
    columns = sprite_image.get_width()  / sprite_size_x
    rows    = sprite_image.get_height() / sprite_size_y
    columns = round(columns) 
    rows = round(rows)
    number_of_sprites = rows*columns
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

#make a random list of lists of sprites to draw.
#each list is a column
def gen_random_tiles():
    list_of_tile_columns = []
    column = []
    for z in range(NUMBER_TILES_LR):
        for n in range(NUMBER_TILES_UD):
            column.append(random.randint(0, 75))  #TODO second arg needs to be variable
        list_of_tile_columns.append(column.copy())
        column.clear()
    
    return list_of_tile_columns            

#draw to current display
def draw_tile_sprites(sl):
    pg.display.set_mode((1200,900))
    surface_to_draw_upon = pg.display.get_surface()
    s=surface_to_draw_upon  #make it short bc i have bad habits
    this_row, this_col, sx, sy = 0,0,0,0
    print(sl)
    for each_column in sl:
        for each_tile in each_column:
            sx = this_col * sprite_size_x
            sy = this_row * sprite_size_y
            s.blit(sprite_list[each_tile], (sx,sy))
            this_row += 1
        this_col += 1
        this_row = 0
        pg.display.flip()



def day2_r1():
    build_sprite_list()
    all_tiles = gen_random_tiles()
    draw_tile_sprites(all_tiles)
    
    while True:
        event = pg.event.wait()
        if event.type == pg.QUIT:
            pg.quit()
            raise SystemExit
        if event.type in [pg.MOUSEBUTTONDOWN, pg.KEYDOWN]:
            break
    



if __name__ == "__main__":
    day2_r1()
    pg.quit()