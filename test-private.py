import numpy as np
import typing
import unittest

from connect import ConnectFour
from connect import RED, BLUE, RED_WIN, BLUE_WIN, DRAW, IN_PROGRESS


class PrivateTestCF(unittest.TestCase):

    def test_large_diagonal_check(self):
        cf = ConnectFour(6, 6)
        cf.board = np.array([[0, 0, 0, 0, 0, BLUE],
                             [0, 0, 0, 0, RED, BLUE],
                             [0, 0, 0, RED, BLUE, RED],
                             [0, 0, RED, RED, RED, RED],
                             [0, RED, RED, BLUE, BLUE, RED],
                             [BLUE, BLUE, RED, RED, BLUE, RED]
                             ])
        self.assertTrue(cf.is_diagonal_win(RED))
        self.assertTrue(cf.is_vertical_win(RED))
        self.assertTrue(cf.is_horizontal_win(RED))
        self.assertFalse(cf.is_diagonal_win(BLUE))
        self.assertFalse(cf.is_vertical_win(BLUE))
        self.assertFalse(cf.is_horizontal_win(BLUE))

    def test_is_horizontal_long(self):
        cf = ConnectFour(10,4)
        cf.board = np.array([[0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,RED,RED,RED,RED],
                             [RED,RED,BLUE,BLUE,RED,BLUE,RED,RED,BLUE,BLUE]
                             ])
        self.assertTrue(cf.is_horizontal_win(RED))

    # def test_can_player_win_empty_board(self):
    #     cf = ConnectFour(4,4)
    #     cf.board=np.array([[0, 0, 0, 0],
    #                        [0, 0, 0, 0],
    #                        [0, 0, 0, 0],
    #                        [0, 0, 0, 0]])
    #     self.assertFalse(cf.can_player_win(BLUE))
    #     self.assertTrue(cf.can_player_win(RED))
    #
    #
    # def test_can_player_win_empty_board_45(self):
    #     cf = ConnectFour(4,5)
    #     cf.board=np.array([[0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0],
    #                        [0, 0, 0, 0, 0]])
    #     self.assertTrue(cf.can_player_win(BLUE))
    #     self.assertTrue(cf.can_player_win(RED))

