import pew
import time
from life import Board


def pic_from_board(board):
    return pew.Pix.from_iter([[int(el) for el in row] for row in board.grid])


def main():
    pew.init()
    board = Board(16, 16)
    scroll_x = 3
    scroll_y = 3
    cursor_x = 7
    cursor_y = 7

    while True:
        k = pew.keys()
        o_pressed = k & pew.K_O
        if k & pew.K_UP:
            if o_pressed and scroll_y > 0:
                scroll_y -= 1
            elif cursor_y > 0:
                cursor_y -= 1
        if k & pew.K_DOWN:
            if o_pressed and scroll_y < board.height - 8 - 1:
                scroll_y += 1
            elif cursor_y < board.height - 1:
                cursor_y += 1
        if k & pew.K_LEFT:
            if o_pressed and scroll_x > 0:
                scroll_x -= 1
            elif cursor_x > 0:
                cursor_x -= 1
        if k & pew.K_RIGHT:
            if o_pressed and scroll_x < board.height - 8 - 1:
                scroll_x += 1
            elif cursor_x < board.width - 1:
                cursor_x += 1
        if k & pew.K_X:
            if o_pressed:
                board.step()
            else:
                board.toggle_pixel(cursor_x, cursor_y)
        if k & ~pew.K_O:
            time.sleep(0.5)
            pew.keys()
        pic = pew.Pix()
        board_pic = pic_from_board(board)
        if not o_pressed:
            board_pic.pixel(
                cursor_x, cursor_y, (pic.pixel(cursor_x, cursor_y)) + 2
            )
        pic.blit(board_pic, -scroll_x, -scroll_y)

        pew.show(pic)


main()
