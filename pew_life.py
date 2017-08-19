import pew
import time
from life import Board


def pic_from_board(board):
    return pew.Pix.from_iter([[int(el) for el in row] for row in board.grid])


def main():
    pew.init()
    board = Board(8, 8)
    cursor_x = 3
    cursor_y = 3
    
    while True:
        k = pew.keys()
        if k & pew.K_UP and cursor_y >= 0:
            cursor_y -= 1
        if k & pew.K_DOWN and cursor_x < 8:
            cursor_y += 1
        if k & pew.K_LEFT and cursor_y >= 0:
            cursor_x -= 1
        if k & pew.K_RIGHT and cursor_y < 8:
            cursor_x += 1
        if k & pew.K_O:
            board.toggle_pixel(cursor_x, cursor_y)
        if k & pew.K_X:
            board.step()
        if k:
            time.sleep(0.5)
            pew.keys()
        pic = pic_from_board(board)
        pic.pixel(cursor_x, cursor_y, (pic.pixel(cursor_x, cursor_y)) + 2)
        pew.show(pic)


main()
