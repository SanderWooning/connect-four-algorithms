import numpy as np
import typing
import unittest

from connect import ConnectFour
from connect import RED, BLUE, RED_WIN, BLUE_WIN, DRAW, IN_PROGRESS


class PrivateTestCF(unittest.TestCase):

    def test_no_avail_moves(self):
        cf = ConnectFour(4, 4)
        cf.board = np.array([[RED,RED,RED,RED],
                             [RED,RED,RED,RED],
                             [RED,RED,RED,RED],
                             [RED,RED,RED,RED],
                             ])
        self.assertTrue(len(cf.get_available_moves()) == 0)

    def test_win_asymatric_board(self):
        cf = ConnectFour(6, 4)
        cf.board = np.array([[0, 0, 0, 0, RED, BLUE],
                             [0, 0, 0, RED, 0, BLUE],
                             [0, 0, RED, 0, 0, RED],
                             [0, RED, BLUE, BLUE, BLUE, BLUE]
                             ])
        self.assertTrue(cf.has_player_won(RED))
        self.assertTrue(cf.has_player_won(BLUE))

        cf = ConnectFour(4, 7)
        cf.board = np.array([[RED, 0, 0, BLUE],
                             [0, RED, RED, 0],
                             [0, BLUE, RED, 0],
                             [BLUE, 0, 0, RED],
                             [0, BLUE, 0, 0],
                             [0, 0, BLUE, 0],
                             [0, 0, 0, BLUE]
                             ])

        self.assertTrue(cf.has_player_won(RED))
        self.assertTrue(cf.has_player_won(BLUE))

        cf = ConnectFour(10, 4)
        cf.board = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, RED, RED, RED, RED],
                             [RED, RED, BLUE, BLUE, RED, BLUE, RED, RED, BLUE, BLUE]
                             ])
        self.assertTrue(cf.is_horizontal_win(RED))
        self.assertFalse(cf.is_horizontal_win(BLUE))

    def test_large_diagonal_check(self):
        """
        A testcase for large diagonal wins.
        Floating discs don't affect test-case.

        1. First

        :return:
        """

        cf = ConnectFour(6, 6)
        cf.board = np.array([[0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, RED, 0],
                             [0, 0, 0, RED, 0, 0],
                             [0, 0, RED, 0, 0, 0],
                             [0, RED, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0]
                             ])

        self.assertTrue(cf.is_diagonal_win(RED))
        self.assertFalse(cf.is_diagonal_win(BLUE))

        cf = ConnectFour(6, 6)
        cf.board = np.array([[0, 0, 0, 0, 0, 0],
                             [0, BLUE, 0, 0, 0, 0],
                             [0, 0, BLUE, 0, 0, 0],
                             [0, 0, 0, BLUE, 0, 0],
                             [0, 0, 0, 0, BLUE, 0],
                             [0, 0, 0, 0, 0, 0],
                             ])

        self.assertTrue(cf.is_diagonal_win(BLUE))
        self.assertFalse(cf.is_diagonal_win(RED))


    def test_best_move_greedy_weird(self):
        """
        Greedy search test-cases for shorter sequences such as a 2-long sequence.

        Three different test-cases are used.

        1. Checks for blocking move against a 2-long vertical sequence
        2. Checks for a blocking move against a 2-long horizontal sequence.
        3. Check for a blocking move against a 2-long anti-diagonal sequence.

        :return:
        """


        cf = ConnectFour(4,4)
        cf.board=np.array([[0,0,0,0],
                           [0,0,0,0],
                           [2,1,0,0],
                           [2,1,0,0]])
        bm1 = cf.best_move_greedy(1)
        bm2 = cf.best_move_greedy(2)
        self.assertEqual(bm1, (1,0))
        self.assertEqual(bm2, (1,1))

        cf = ConnectFour(4,4)
        cf.board=np.array([[0,0,0,0],
                           [0,0,0,0],
                           [2,2,0,0],
                           [1,1,0,0]])
        bm2 = cf.best_move_greedy(2)
        self.assertEqual(bm2, (3,2))

        cf = ConnectFour(4,4)
        cf.board=np.array([[0,0,0,0],
                           [0,0,0,0],
                           [0,2,1,0],
                           [2,1,1,1]])
        bm1 = cf.best_move_greedy(1)
        self.assertEqual(bm1, (1,2))

