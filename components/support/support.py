import csv
import os
import pygame
from components.support.settings import tile_size, scale, base_dir


def import_level_data(path: str) -> list[list[str]]:
    """
    Import level data from a csv file

    :param path: The path of the csv file
    :return: The level data
    """
    filepath = os.path.join(base_dir, path)
    data = []

    # Open and parse csv
    with open(filepath, newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            data.append([element for element in row])

    return data


def import_tile_set(path) -> list[pygame.Surface]:
    """
    Import a tile set

    :param path: The path of the tile set
    :return: The tile set
    """
    surface = pygame.image.load(os.path.join(base_dir, path))
    resized_surface = pygame.transform.scale(
        surface,
        (int(surface.get_width() * 2 * scale),
         surface.get_height() * 2 * scale))

    # Calculate the new tile size including the border
    tile_size_with_border = tile_size + 2 * scale

    tile_amount_x = 48
    tile_amount_y = 59

    tiles = []

    # Create a list of tiles
    for row in range(tile_amount_y):
        for col in range(tile_amount_x):
            x = col * tile_size_with_border
            y = row * tile_size_with_border
            new_surf = pygame.Surface((tile_size, tile_size))
            new_surf.blit(resized_surface,
                          (0, 0),
                          pygame.Rect(x + 2 * scale,
                                      y + 2 * scale,
                                      tile_size,
                                      tile_size))
            tiles.append(new_surf)

    return tiles
