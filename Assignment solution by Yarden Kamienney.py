import sqlite3
from PIL import Image
import os

defined_size_of_tile = 37
src_w = 0
src_h = 1
dst_w = 2
dst_h = 3
rotation_location = 4
left_spin = -90
right_spin = 90
photo_path = 'assignment.jpg'
dataset_path = 'assignment.sqlite'


def tiles_to_list(tile_size, tiles_in_row, tiles_in_col, image):
    """
    This function extract all the tiles from a given image and organizing them into a list for further processing. 
    :param tile_size: an integer represent the size (in pixels) of each tile in the image
    :param tiles_in_row: an integer represent the number of tiles in the width of the image
    :param tiles_in_col: an integer represent the number of tiles in the height of the image
    :param image: an image to extract her tiles
    :return: a list containing all the tiles of the given image.
    """
    tiles_list = []
    for row in range(tiles_in_row):
        for col in range(tiles_in_col):
            tiles_list.append(image.crop((row*tile_size, col*tile_size, (row+1)*tile_size, (col+1)*tile_size)))
    return tiles_list


def image_reconstruction(database, tile_size, tiles_in_row, im_reconstructed, tiles_list):
    """
    This function descrambling an image based on a provided SQLite database and save it.
    :param database: an SQLite database containing information about the tiles positions and rotation.
    :param tile_size: an integer represent the size (in pixels) of each tile in the image
    :param tiles_in_row: an integer represent the number of tiles in the width of the image
    :param im_reconstructed: a Pillow image object that represents the descrambled image
    :param tiles_list: a list containing all the tiles of the scrambled image
    """
    for row in database:
        current_tile = tiles_list[row[dst_w]*tiles_in_row+row[dst_h]]
        if row[rotation_location] == 'left':
            current_tile = current_tile.rotate(left_spin)
        else:
            current_tile = current_tile.rotate(right_spin)
        im_reconstructed.paste(current_tile, (row[src_w]*tile_size, row[src_h]*tile_size))
    im_reconstructed.save('descrambled.jpg')


if __name__ == '__main__':
    if not os.path.exists(photo_path) or not os.path.exists(dataset_path):
        print('Some of the files are missing!')
        exit()

    # Load the photo's database
    conn = sqlite3.connect(dataset_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transform")  # transform is the table name inside the sqlite file
    transform = cursor.fetchall()

    # Load the scrambled image
    im = Image.open(photo_path)

    im_descrambled = Image.new('RGB', (im.width, im.height))

    # extracting the tiles info
    tile_size = defined_size_of_tile
    tiles_in_row = im.width // tile_size
    tiles_in_col = im.height // tile_size

    tiles = tiles_to_list(tile_size, tiles_in_row, tiles_in_col, im)

    image_reconstruction(transform, tile_size, tiles_in_row, im_descrambled, tiles)

    cursor.close()
    conn.close()
