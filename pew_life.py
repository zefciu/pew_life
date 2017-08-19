import pew
import time
from life import Board


def pic_from_board(board):
    return pew.Pix.from_iter([[int(el) for el in row] for row in board.grid])


def main():
    pew.init()

    board = Board(8, 8)
    board.toggle_pixel(3, 3)
    board.toggle_pixel(3, 4)
    board.toggle_pixel(3, 5)
    board.toggle_pixel(4, 5)
    board.toggle_pixel(5, 4)

    while True:
        pic = pic_from_board(board)
        pew.show(pic)
        time.sleep(1)
        board.step()


main()
