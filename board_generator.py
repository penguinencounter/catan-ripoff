import random
import sys
from colorama import init, Fore, Back, Style
init()

DESERT = "d"
BRICK = "b"
LUMBER = "l"
WHEAT = "w"
SHEEP = "s"
ORE = "o"

tiles = [DESERT,
         BRICK, BRICK, BRICK,
         LUMBER, LUMBER, LUMBER, LUMBER,
         WHEAT, WHEAT, WHEAT, WHEAT,
         SHEEP, SHEEP, SHEEP, SHEEP,
         ORE, ORE, ORE]

numbers = [2,
           3, 3,
           4, 4,
           5, 5,
           6, 6,
           8, 8,
           9, 9,
           10, 10,
           11, 11,
           12]

board = [[None, None, None],  # 3
         [None, None, None, None],  # 4
         [None, None, None, None, None],  # 5
         [None, None, None, None],  # 4
         [None, None, None]]  # 3


class Tile:
    def __init__(self, tile: str):
        self.tile = tile
        self.number = 0

    def __repr__(self):
        return f'<Tile: {self.tile}/{self.number}>'


def randomize_board_tiles():
    global tiles, numbers, board
    random.shuffle(tiles)
    random.shuffle(numbers)
    tid = 0
    nid = 0
    for i in range(len(board)):
        # pick board_meta[i] items
        count = len(board[i])
        for j in range(count):
            board[i][j] = Tile(tiles[tid])
            if tiles[tid] != DESERT:
                board[i][j].number = numbers[nid]
                nid += 1
            tid += 1


def render_board_tiles():
    global board
    for row in board:
        pp = ''
        for tile in row:
            if tile.tile == BRICK:
                pp += Fore.RED
            elif tile.tile == LUMBER:
                pp += Fore.GREEN
            elif tile.tile == WHEAT:
                pp += Fore.YELLOW
            elif tile.tile == ORE:
                pp += Fore.CYAN
            elif tile.tile == DESERT:
                pp += Back.WHITE + Fore.BLACK
            pp += tile.tile
            if tile.number < 10:
                pp += f'0{tile.number}'
            else:
                pp += f'{tile.number}'
            pp += Style.RESET_ALL
            pp += ' '
        print(' '*int((5-len(row))*1.5)+pp)


if __name__ == '__main__':
    GEN_COUNT = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 1
    for i in range(GEN_COUNT):
        if i > 0:
            print('=================')
        randomize_board_tiles()
        render_board_tiles()
    
