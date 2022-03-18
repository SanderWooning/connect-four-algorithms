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

        Color ANSI escape sequences to give terminal-text color for better readability
        """
        print("")
        for row in range(self.height):
            for column in range(self.width):

                print("|", end="")

                if self.board[row][column] == 0:
                    print('\033[0m' + "    " + '\033[0m', end="")

                if self.board[row][column] == 1:
                    print('\33[41m' + "REDD" + '\033[0m', end="")

                if self.board[row][column] == 2:
                    print('\33[44m' + "BLUE" + '\033[0m', end="")

                if column == (self.width - 1):
                    print("|")

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

    def get_available_moves(self) -> typing.List[typing.Tuple[int, int]]:
        """
        Goal:
            Return a list with all possible moves in tuples.
        Steps:
            1. Initiate an empty list where to put the ID's into
            2. Start a loop over all the columns by utilising the width of the board.
            3. Start a reverse loop (from self.heigth - 1 to 0) over the height of the column.
            4. Find the first zero in the column
            5. Append the list with tuple(row id, column id)
            6. Then break off the loop, because a column only has it is the only legal move in that column.
        :return: The list of move tuples (row id, column id)
        """
        starting_list = []

        for column in range(self.width):
            for row in range(self.height - 1, -1, -1):
                if self.board[row][column] == 0:
                    starting_list.append((row, column))
                    break
            else:
                continue

        return starting_list

    def is_horizontal_win(self, player: int) -> bool:

        """
        Goal:
            Check whether there are 4 connected discs for the given player horizontally
        Steps:
            1. Iterate over all rows. This is where the horizontal
            2. Iterate of all the elements in the row - 3.
            3. Check if position until position + 4 all equals player. If True, return True.
            4. Else return False
        :param player: The player for which we check whether there is a horizontal win
        :return: True if the player has 4 horizontally connected discs else False
        """

        for row in range(self.height):
            for column in range(0, self.width - 3):
                if self.board[row][column] == player \
                        and self.board[row][column + 1] == player \
                        and self.board[row][column + 2] == player \
                        and self.board[row][column + 3] == player:
                    return True

        else:
            return False

    def is_vertical_win(self, player: int) -> bool:
        """
        Goal:
            Check whether there are 4 connected discs for the given player vertically
        Steps:
            1. Iterate over all rows. This is where the horizontal
            2. Iterate of all the elements in the row - 3.
            3. Check if position until position + 4 all equals player. If True, return True.
            4. Else return False
        :param player: The player for which we check whether there is a vertical win
        :return: True if the player has 4 vertically connected discs else False
        """

        for column in range(self.width):
            for row in range(0, self.height - 3):
                if self.board[row][column] == player \
                        and self.board[row + 1][column] == player \
                        and self.board[row + 2][column] == player \
                        and self.board[row + 3][column] == player:
                    return True

        return False

    def check_diag_win(self, array, player):
        """
        ** Self implemented function **
        Goal:
            Check if the given array has 4 connected for the given player diagonally
        Steps:
            1. Iterate over all rows which could form a diagonal of length 4.
            2. Iterate over all columns which could form a diagonal of length 4.
            3. Check if four connected discs are in the formed diagonal.
        :param player: The player for which we check whether there is a diagonal win
        :return: True if the player has 4 diagonal connected discs else False
        """

        for row in range(self.height - 3):
            for column in range(self.width - 3):
                if array[row][column] == player \
                        and array[row + 1][column + 1] == player \
                        and array[row + 2][column + 2] == player \
                        and array[row + 3][column + 3] == player:
                    return True

        return False

    def is_diagonal_win(self, player: int) -> bool:

        """
        Goal:
            "Check whether there are 4 connected discs for the given player diagonally"

        Steps:
            1. Call fuction check_diag_win() with normal board and vertically mirrored board.

        Additional info:
            "Function is split up into two partitions because unsure if we able to alter input parameters of functions"


        :param player: The player for which we check whether there is a diagonal win

        :return: True if the normal or vertically mirrored board are contain four connected discs.
        """

        if self.check_diag_win(array=self.board, player=player) \
                or self.check_diag_win(array=np.fliplr(self.board),
                                       player=player):  # Mirror Matrix vertically with np.fliplr
            return True
        else:
            return False

    def has_player_won(self, player: int) -> bool:

        """
        Check whether the given player has won

        Steps:
            1. Call all winning function once with the given player parameter. Return true if any are true.

        :param player: The player for which we check whether there is a win

        :return: True if the player has won else False
        """

        if self.is_vertical_win(player=player) \
                or self.is_horizontal_win(player=player) \
                or self.is_diagonal_win(player=player):
            return True
        else:
            return False

    def get_game_status(self) -> int:

        """
            Returns the status of the game (inprogress, draw, win for blue, win for red)

            Steps:
                1. Check if player red has won with has_player_won function
                2. Check if player blue has won with has_player_won function
                3. Check if there are no legal moves, which implies a draw
                4. Else return in progress.

            :return: one of the following:
                    - IN_PROGRESS if the game is in progress
                    - DRAW if the game ended in a draw
                    - RED_WIN if red won
                    - BLUE_WIN if blue won
            """

        if self.has_player_won(RED):
            return RED_WIN
        if self.has_player_won(BLUE):
            return BLUE_WIN
        if len(self.get_available_moves()) == 0:
            return DRAW
        else:
            return IN_PROGRESS

    def invert_player(self, player):

        """
        Invertion function put outside of the can_player_win function to not interfere with player parameter"
        """

        if player == RED:
            return BLUE
        if player == BLUE:
            return RED

    def can_player_win(self, player: int) -> bool:
        """
        Recursive function that checks whether the given player (who is also to move)
        can win from the current board position given by self.board.
        Refer to the assignment text for the exact winning criterion (not the default one!).

        Steps:
            1. Check if player has won
            2. Check if the game is a draw. If a draw occurs, red has won.
            3. Get all available moves of the current board
            4. Loop over all available moves
            5. Play the available moves.
            6. Check if other player can not win with next move.
            7. Undo move

        :return: True if the player can win, False otherwise
        """

        if self.has_player_won(player=player):
            return True
        if self.get_game_status() == DRAW:
            if player == RED:
                return True
            if player == BLUE:
                return False
        else:
            for move in self.get_available_moves():

                self.place_disc(row_idx=move[0], col_idx=move[1], player=player)

                if not self.can_player_win(self.invert_player(player)):
                    self.place_disc(row_idx=move[0], col_idx=move[1], player=0)
                    return True

                self.place_disc(row_idx=move[0], col_idx=move[1], player=0)

        return False

    def max_horizontal_length(self, player: int, return_moves: bool):

        """"
        A function for the greedy search algorithm
        A nested for-loop which checks the longest line of HORIZONTALLY connected discs for the given player

        Steps:
            1. Iterate over all rows
            2. Iterate over all items within that row.
            3. Every time a piece is encountered which is equal to player, increment our counting length.
            4. If counting length has increased in comparison to our starting value (starting_len), reset the moves.
            5. Create possible moves, which are one LEFT and one RIGHT our sequence of piece which are equal to player.
            6. Check if created move is a valid move, if so, append to returning_moves.
            7. Return the length of the longest chain. Or if return_moves is true, return the move which blocks
            the longest chain.


        :param: player: The player for which we check the maximal length.
        :param: return_moves: A boolean value. If yes, function returns the moves.

        :return: Returns the length of the longest horizontal connect or if return_moves, it returns the moves
        """

        starting_len = 0
        returning_moves = []
        avail_moves = self.get_available_moves()

        for row in range(self.height):
            counting_len = 0
            for column in range(self.width):
                if self.board[row][column] == player:
                    counting_len += 1

                    # Override the returning_moves if the move is longer then the previous sequence
                    if counting_len > starting_len:
                        returning_moves = []
                        starting_len = counting_len

                    # Append returning_moves if move is as long as the previous sequence
                    if counting_len == starting_len:
                        move_1 = (row, column + 1)
                        move_2 = (row, column - starting_len)
                        if move_1 in avail_moves:
                            returning_moves.append(move_1)
                        if move_2 in avail_moves:
                            returning_moves.append(move_2)

                else:
                    counting_len = 0

        if return_moves:
            return returning_moves

        else:
            return starting_len

    def max_vertical_length(self, player: int, return_moves: bool):

        """"
        A function for the greedy search algorithm
        A nested for-loop which checks the longest line of VERTICALLY connected discs for the given player

        Steps:
            1. Iterate over all columns
            2. Iterate over all items within that column.
            3. Every time a piece is encountered which is equal to player, increment our counting length.
            4. If counting length has increased in comparison to our starting value (starting_len), reset the moves.
            5. Create possible moves, which are one above and one below our sequence of piece which are equal to player.
            6. Check if created move is a valid move, if so, append to returning_moves.
            7. Return the length of the longest chain. Or if return_moves is true, return the move which blocks
            the longest chain.

        :param: player: The player for which we check the maximal length.
        :param: return_moves: A boolean value. If yes, function returns the moves.

        :return: Returns the length of the longest horizontal connect or if return_moves is true, it returns the moves.
        """

        starting_len = 0
        returning_moves = []
        avail_moves = self.get_available_moves()

        for column in range(self.width):
            counting_len = 0
            for row in range(self.height):
                if self.board[row][column] == player:
                    counting_len += 1

                    # Override the returning_moves if the move is longer then the previous sequence
                    if counting_len > starting_len:
                        returning_moves = []
                        starting_len = counting_len

                    # Append returning_moves if move is as long as the previous sequence
                    if counting_len == starting_len:
                        move_1 = (row + 1, column)
                        move_2 = (row - starting_len, column)
                        if move_1 in avail_moves:
                            returning_moves.append(move_1)
                        if move_2 in avail_moves:
                            returning_moves.append(move_2)
                else:
                    counting_len = 0

        if return_moves:
            return returning_moves

        else:
            return starting_len

    def max_diagnonal_length(self, player: int, flip_array: bool, return_moves: bool):

        """"
        A function for the greedy search algorithm
        A nested for-loop which checks the longest line of the DIAGONAL and the ANTI-DIAGONAL for connected discs
        for the given player

        Steps:
            1. Iterate over the bottom row.
            2. Iterate over all elements in the bottom row.
            3. Iterate the possible length of the diagonal, which is based on the width of the board and
            it's current index.
            4.

        :param: player: The player for which we check the maximal length.
        :param: array: The board array. Given so we can input a flipped board.
        :param: return_moves: A boolean value. If yes, function returns the moves.

        :return: Returns the length of the longest horizontal connect or if return_moves, it returns the moves
        """

        starting_len = 0
        diagonal_returning_moves = []
        avail_moves = self.get_available_moves()


        #Flip the board for checking the anti-diagonal.
        if flip_array:
            self.board = np.fliplr(self.board)



        for row in range(self.height - 3):
            counting_len = 0
            for column in range(self.width):
                for index in range(self.width - column):
                    if self.board[row + index][column + index] == player:
                        print()
                        counting_len += 1

                        if counting_len > starting_len:
                            diagonal_returning_moves = []
                            starting_len = counting_len

                        # If the counting-sequence is as long or longer then the starting-sequence
                        # Build two tupples which are the moves one at the bottom of the diagonal and one on the top.
                        if counting_len == starting_len:
                            move_1 = (index + 1, index + 1)
                            move_2 = (index - starting_len, index - starting_len)

                            # If the array is flipped, the move needs to be flipped.
                            # This is done by subtracting it from the width of the board
                            if flip_array:
                                move_1 = (move_1[0], (self.width - 1 - move_1[1]))
                                move_2 = (move_2[0], (self.width - 1 - move_2[1]))

                            # Check if the moves are valid moves. If so, add them to the storage.
                            if move_1 in avail_moves:
                                diagonal_returning_moves.append(move_1)
                            if move_2 in avail_moves:
                                diagonal_returning_moves.append(move_2)

                    else:
                        counting_len = 0

        # Unflip the board.
        if flip_array:
            self.board = np.fliplr(self.board)

        if return_moves:
            return diagonal_returning_moves

        else:
            return starting_len

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

        Steps:
            1. Check if any of the legal moves are winning moves.
            2. Call multiple length checking functions to get the max length of the board for the inverted played.
            3. Check which of the function is the longest and call it's given moves.
            4. If any of the moves are in the legal moves, return
            5. Else go to the next moves and functions.

        :return: The best move according to the function in the form (row_id, col_id)
        """

        # Check for winning-cases for player
        for move in self.get_available_moves():
            self.place_disc(row_idx=move[0], col_idx=move[1], player=player)
            if self.has_player_won(player=player):
                self.place_disc(row_idx=move[0], col_idx=move[1], player=0)
                return move
            else:
                self.place_disc(row_idx=move[0], col_idx=move[1], player=0)

        # Get all maximal lengths of the other player of the horizontal, vertical, diagonal and anti-diagonal sequences.
        horizontal_max = self.max_horizontal_length(self.invert_player(player), return_moves=False)
        vertical_max = self.max_vertical_length(self.invert_player(player), return_moves=False)
        diagonal_max = self.max_diagnonal_length(self.invert_player(player), flip_array=False, return_moves=False)
        a_diagonal_max = self.max_diagnonal_length(self.invert_player(player), flip_array=True, return_moves=False)

        # Get all available blocking the longest sequence of the other player.
        horizontal_moves = self.max_horizontal_length(self.invert_player(player), return_moves=True)
        vertical_moves = self.max_vertical_length(self.invert_player(player), return_moves=True)
        diagonal_moves = self.max_diagnonal_length(self.invert_player(player), flip_array=False, return_moves=True)
        a_diagonal_moves = self.max_diagnonal_length(self.invert_player(player), flip_array=True, return_moves=True)

        # Get the longest length
        max_length_opponent = max(horizontal_max, vertical_max, diagonal_max, a_diagonal_max)


        # Check which function gives the longest length for the opponent.
        # Then it returns the first move which is in available moves.
        for max_length_loop in range(max_length_opponent, 0, -1):
            if horizontal_max == max_length_loop and len(horizontal_moves) > 0:
                return horizontal_moves[0]

            if vertical_max == max_length_loop and len(vertical_moves) > 0:
                return vertical_moves[0]

            if diagonal_max == max_length_loop and len(diagonal_moves) > 0:
                return diagonal_moves[0]

            if a_diagonal_max == max_length_loop and len(a_diagonal_moves) > 0:
                return a_diagonal_moves[0]
