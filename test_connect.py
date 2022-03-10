import numpy as np
import typing
import unittest

from connect import ConnectFour
from connect import RED, BLUE, RED_WIN, BLUE_WIN, DRAW, IN_PROGRESS


class TestCF(unittest.TestCase):

    def test_print(self):
        cf = ConnectFour(4,4)
        cf.board = np.array([[RED, 0, 0, 0],
                             [RED, 0, 0, 0],
                             [RED, BLUE, BLUE, 0],
                             [RED, BLUE, BLUE, 0]])
        cf.print_board()

   
    def test_place_disc(self):
        cf = ConnectFour(4,4)
        # place a red disk at the bottom left corner - location = (3,0)
        row_idx = 3
        col_idx = 0
        # place red disc there
        cf.place_disc(row_idx,col_idx, RED)
        self.assertTrue(cf.board[row_idx, col_idx] == RED)

        # overwrite with a blue disc
        cf.place_disc(row_idx,col_idx, BLUE)
        self.assertTrue(cf.board[row_idx, col_idx] == BLUE)


    def test_get_available_moves_empty_board(self):
        cf = ConnectFour(4,4)
        all_true_moves = [(3,col_idx) for col_idx in range(4)]
        moves = set(cf.get_available_moves())

        # check if every truly possible move is already returned
        for true_move in all_true_moves:
            self.assertTrue(true_move in moves)
        
        # check if not more moves were returned than the real ones
        self.assertTrue(len(all_true_moves) == len(moves))

    
    def test_get_available_moves_empty_board(self):
        cf = ConnectFour(4,4)
        all_true_moves = [(3,col_idx) for col_idx in range(4)]
        moves = set(cf.get_available_moves())

        # check if every truly possible move is already returned
        for true_move in all_true_moves:
            self.assertTrue(true_move in moves)
        
        # check if not more moves were returned than the real ones
        self.assertTrue(len(all_true_moves) == len(moves))
    

    def test_is_horizontal_win(self):
        cf = ConnectFour(4,4)
        cf.board = np.array([[RED, 0, 0, 0],
                             [RED, 0, 0, 0],
                             [RED, BLUE, BLUE, 0],
                             [RED, BLUE, BLUE, 0]])

        self.assertFalse(cf.is_horizontal_win(RED))
        self.assertFalse(cf.is_horizontal_win(BLUE))

        cf.board = np.array([[RED, 0, 0, 0],
                             [RED, 0, 0, 0],
                             [RED, BLUE, BLUE, 0],
                             [BLUE, BLUE, BLUE, BLUE]])

        self.assertTrue(cf.is_horizontal_win(BLUE))
        self.assertFalse(cf.is_horizontal_win(RED))

    def test_is_horizontal_long(self):
        cf = ConnectFour(10,4)
        cf.board = np.array([[0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0],
                             [0,0,0,0,0,0,0,0,0,0,0,0],
                             [RED,RED,BLUE,BLUE,RED,RED,RED,RED,BLUE,BLUE]
                             ])
        self.assertTrue(cf.is_horizontal_win(RED))
        self.assertFalse(cf.is_horizontal_win(BLUE))

    def test_is_vertical_win(self):
        cf = ConnectFour(4,4)
        cf.board = np.array([[RED, 0, 0, 0],
                             [RED, 0, 0, 0],
                             [RED, BLUE, BLUE, 0],
                             [RED, BLUE, BLUE, 0]])

        self.assertTrue(cf.is_vertical_win(RED))
        self.assertFalse(cf.is_vertical_win(BLUE))




    def test_is_diagonal_win(self):
        # these are not real boards that can be achieved with real play because
        # some discs are levitating but for the tests that's alright :)
        cf = ConnectFour(4,4)
        cf.board = np.array([[RED, 0, 0, 0],
                             [RED, RED, 0, 0],
                             [RED, BLUE, RED, 0],
                             [RED, BLUE, BLUE, RED]])

        self.assertTrue(cf.is_diagonal_win(RED))
        self.assertFalse(cf.is_diagonal_win(BLUE))


        cf.board = np.array([[BLUE, 0, 0, RED],
                             [BLUE, RED, RED, 0],
                             [RED, RED, RED, 0],
                             [RED, BLUE, BLUE, RED]])

        self.assertTrue(cf.is_diagonal_win(RED))
        self.assertFalse(cf.is_diagonal_win(BLUE))


    def test_has_player_won(self):
        # diagonal win for red
        cf = ConnectFour(4,4)
        cf.board = np.array([[RED, 0, 0, 0],
                             [RED, RED, 0, 0],
                             [RED, BLUE, RED, 0],
                             [RED, BLUE, BLUE, RED]])
        self.assertTrue(cf.has_player_won(RED))
        self.assertFalse(cf.has_player_won(BLUE))

        # vertical win for red
        cf = ConnectFour(4,4)
        cf.board = np.array([[RED, 0, 0, 0],
                             [RED, 0, 0, 0],
                             [RED, BLUE, BLUE, 0],
                             [RED, BLUE, BLUE, 0]])

        self.assertTrue(cf.has_player_won(RED))
        self.assertFalse(cf.has_player_won(BLUE))

        # horizontal win for blue
        cf.board = np.array([[RED, 0, 0, 0],
                             [RED, 0, 0, 0],
                             [RED, BLUE, BLUE, 0],
                             [BLUE, BLUE, BLUE, BLUE]])

        self.assertTrue(cf.has_player_won(BLUE))
        self.assertFalse(cf.has_player_won(RED))
    
    def test_get_game_status(self):
        cf = ConnectFour(4,4)
        # in progress
        self.assertEqual(cf.get_game_status(), IN_PROGRESS)

        # blue win
        cf.board = np.array([[RED, 0, 0, 0],
                             [RED, 0, 0, 0],
                             [RED, BLUE, BLUE, 0],
                             [BLUE, BLUE, BLUE, BLUE]])
        self.assertEqual(cf.get_game_status(), BLUE_WIN)  

        # red win
        cf = ConnectFour(4,4)
        self.assertEqual(cf.get_game_status(), IN_PROGRESS)

        cf.board = np.array([[RED, 0, 0, 0],
                             [RED, 0, 0, 0],
                             [RED, BLUE, BLUE, 0],
                             [RED, BLUE, BLUE, 0]])
        self.assertEqual(cf.get_game_status(), RED_WIN)       


    def test_can_player_win(self):
        cf = ConnectFour(4,4)
        cf.board = np.array([[0, 0, 0, 0],
                             [RED, BLUE,0,0],
                             [RED,BLUE,0,0],
                             [RED, BLUE, 0,0]])

        self.assertTrue(cf.can_player_win(BLUE)) 
        self.assertTrue(cf.can_player_win(RED))


        cf.board = np.array([[0, 0, 0, 0],
                             [RED, 0,0,0],
                             [RED,BLUE,0,0],
                             [RED, BLUE, BLUE,0]])

        self.assertFalse(cf.can_player_win(BLUE)) 
        self.assertTrue(cf.can_player_win(RED))

    def test_can_player_win_empty_board(self):
        cf = ConnectFour(4,4)
        cf.board=np.array([[0, 0, 0, 0],
                           [0, 0, 0, 0],
                           [0, 0, 0, 0],
                           [0, 0, 0, 0]])
        self.assertFalse(cf.can_player_win(BLUE))
        self.assertTrue(cf.can_player_win(RED))


    def test_best_move_greedy(self):
        cf = ConnectFour(4,4)
        cf.board=np.array([[0,0,0,0],
                        [1,2,1,1],
                        [1,1,2,2],
                        [1,2,2,2]])
        bm1 = cf.best_move_greedy(1)
        bm2 = cf.best_move_greedy(2)
        self.assertEqual(bm1, (0,0))
        self.assertEqual(bm2, (0,0))