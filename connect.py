import typing
import numpy as np

# Codes that we use. DO NOT CHANGE THESE.
RED = 1
BLUE = 2
DRAW = -2
IN_PROGRESS = -1
BLUE_WIN = BLUE
RED_WIN = RED


class ConnectFour:
    def __init__(self, width: int, height: int):
        """
        The ConnectFour object, containing all information and functions required for the assignment

        :param width: The width of the rectangular board
        :param height: The height of the board
        """
        self.width = width
        self.height = height
        assert self.width >= 4 and self.height >= 4, "The width and height should be at least 4"

        self.board = np.zeros((self.height, self.width))

    def print_board(self) -> None:
        """
        Print the board in human readable format in the terminal.
        Where red is O and blue is X.


        :return:
        """

        for i in range(self.height):
            for j in range(self.width):

                print("|", end="")

                if self.board[i][j] == 0:
                    print('\033[0m' + "    " + '\033[0m', end="")

                if self.board[i][j] == 1:
                    print('\33[41m' + "REDD" + '\033[0m', end="")

                if self.board[i][j] == 2:
                    print('\33[44m' + "BLUE" + '\033[0m', end="")

                if j == (self.height - 1):
                    print("|")

        return self.board

    def place_disc(self, row_idx: int, col_idx: int, player: int) -> None:

        """
        Place a disc of the current player on the given location, assuming that it is a legal move 
        (this legality check should be done in a different function)

        :param row_idx: The row id (0 = top, self.height-1 = bottom)
        :param col_idx: The column id (0 = leftmost, self.width-1 = rightmost)
        :param player: The player to make the move
        """

        self.board[row_idx][col_idx] = player

        return self.board

    def is_legal(self, row_idx: int, col_idx: int) -> bool:
        if self.board[row_idx][col_idx] == 0:
            return True
        else:
            return False

    def get_available_moves(self) -> typing.List[typing.Tuple[int, int]]:
        """
        Goal:
            Return a list with all possible moves in tuples.

        Steps:
            1. Initiate an empty list where to put the ID's into
            2. Start a loop over all the columns by utilising the width of the board.
            3. Start a reverse loop over the height of the column.
            4. Find the first empty spot in the column
            5. Append the list with ID's
            6. Then break off the loop, because it is the only legal move in that column.


        :return: The list of move tuples (row id, column id)
        """
        starting_list = []

        for i in range(self.width):
            for j in range(self.height - 1, 0, -1):
                if self.board[i][j] == 0:
                    starting_list.append((j, i))
                    break

        return starting_list

    def is_horizontal_win(self, player: int) -> bool:

        """
        Goal:
            Check whether there are 4 connected discs for the given player horizontally

        Steps:
            1. Iterate over all rows. This is where the horizontal
            2. Iterate of all the elements in the row
            3. Find the first elementent that matches our player
            4. If it matches, counter increases.
            5. Check if counter has reached the value of 4.
            5. If next element is not our players, reset counter. Else increase.

        :param player: The player for which we check whether there is a horizontal win

        :return: True if the player has 4 horizontally connected discs else False
        """

        for i in range(self.height):
            horizontal_counter = 0
            for j in range(self.width):
                if self.board[i][j] == player:
                    horizontal_counter += 1
                    if horizontal_counter == 4:
                        return True
                else:
                    horizontal_counter = 0

        return False

    def is_vertical_win(self, player: int) -> bool:
        """
        Goal:
            Check whether there are 4 connected discs for the given player vertically

        Steps:


        :param player: The player for which we check whether there is a vertical win

        :return: True if the player has 4 vertically connected discs else False
        """


        self.print_board()

        for i in range(self.width):
            vertical_counter = 0
            for j in range(self.height):
                if self.board[j][i] == player:
                    vertical_counter += 1
                    if vertical_counter == 4:
                        return True
                else:
                    vertical_counter = 0

        return False

    def is_diagonal_win(self, player: int) -> bool:

        self.print_board()

        print([self.board[i][i] for i in range(len(self.board))])
        print([self.board[i][len(self.board)-1-i] for i in range(len(self.board))])

        """
        Check whether there are 4 connected discs for the given player diagonally

        :param player: The player for which we check whether there is a diagonal win

        :return: True if the player has 4 diagonal connected discs else False
        """

        raise NotImplementedError()

    def has_player_won(self, player: int) -> bool:
        """
        Check whether the given player has won

        :param player: The player for which we check whether there is a win

        :return: True if the player has won else False 
        """

        raise NotImplementedError()

    def get_game_status(self) -> int:
        """
        Returns the status of the game (inprogress, draw, win for blue, win for red)

        :return: one of the following:
                - IN_PROGRESS if the game is in progress
                - DRAW if the game ended in a draw
                - RED_WIN if red won
                - BLUE_WIN if blue won
        """

        raise NotImplementedError()

    def can_player_win(self, player: int) -> bool:
        """
        Recursive function that checks whether the given player (who is also to move) 
        can win from the current board position given by self.board.
        Refer to the assignment text for the exact winning criterion (not the default one!).

        :return: True if the player can win, False otherwise
        """

        raise NotImplementedError()

    def best_move_greedy(self, player: int) -> typing.Tuple[int, int]:
        """
        OPTIONAL. Design a greedy function to determine the best move to play. This
        algorithm involves enumerating all possible moves, and determining
        which of the moves seems good, without looking further ahead. A logical
        greedy approach would be to the following:
         - if we can win in one move, play that move
         - else, play our opponent's best move (the one maximizing the chain length of the opponent's color) 
        This way, the opponent can hopefully not win, and we win if we can in 1 move. It may be a good idea to formulate 
        new functions that are slight alterations of, e.g., is_horizontal_win, is_vertical_win, and is_diagonal_win.

        :return: The best move according to the function in the form (row_id, col_id)
        """

        raise NotImplementedError()
