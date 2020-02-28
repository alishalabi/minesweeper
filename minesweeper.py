"""
Design a game of minesweeper.

Step 1 - Create Adjacency Array: You should have a 2d array of values.
Inserted will be several "mines" - represented by x's. Each cell (that is
not a mine) should have a value of how many mines are adjacent to it.

Ex:
[[None, None, x],
[None, None, None],
[None, None, x]]

Should yield:
[[0, 1, x],
[0, 2, 2],
[0, 1, x]]

Step 2 - Create Obfuscated "Shown" Array: Allow users to add flags and reveal
obfuscated cells on an obfuscated gameboard. Allow win and lose conditions

"""

from pprint import pprint
import random


class Minesweeper:
    def __init__(self, width, height):
        """
        Instantiate all class properties
        """
        self.width = width  # Total width of 2d array
        self.height = height  # Total height of 2d array
        self.number_of_mines = 0  # Total number of mines
        self.number_of_flags = 0  # Total number of flags
        self.secret_gameboard = [
            [0 for i in range(width)] for j in range(height)]
        self.shown_gameboard = [
            ["HIDDEN" for i in range(width)] for j in range(height)]
        self.all_directions = [
            (-1, 1),
            (-1, 0),
            (-1, -1),
            (0, -1),
            (1, -1),
            (1, 0),
            (1, 1),
            (0, 1)
        ]
        self.all_flags = 0
        self.all_shown = 0

    def add_mine(self, row_index, col_index):
        """
        Add a single mine at a specific, valid location
        """
        if self._is_valid(row_index, col_index):
            self.secret_gameboard[row_index][col_index] = "MINE!"
            self.number_of_mines += 1

    def add_random_mines(self, num_mines):
        """
        Add a random number of mines to the secret gameboard
        Will use recursion
        """
        # Exit: have placed all mines
        if num_mines == 0:
            return
        # Get random x and y
        random_x = random.randrange(0, self.width)
        random_y = random.randrange(0, self.height)
        # If cell is already a mine, call function again without decreasing mines
        if self.secret_gameboard[random_x][random_y] == "MINE!":
            return self.add_random_mines(num_mines)
        else:
            self.secret_gameboard[random_x][random_y] = "MINE!"
            return self.add_random_mines(num_mines - 1)

    def generate_all_adjacency(self):
        """
        Generate adjacency board for each cell in secret gameboard
        """
        # Iterate through each cell
        for i in range(len(self.secret_gameboard)):
            for j in range(len(self.secret_gameboard[i])):
                # If cell is itself a mine, do nothing
                if self.secret_gameboard[i][j] != "MINE!":

                    adjacenct_count = 0
                    valid_neighbors = self.get_valid_neighbors(i, j)
                    # print(f"Valid neighbors: {valid_neighbors}")
                    for x, y in valid_neighbors:
                        # print(f"x: {x}, y: {y}")
                        # print(f"secret_gameboard at {x}, {y}: {self.secret_gameboard[x][y]}")
                        if self.secret_gameboard[x][y] == "MINE!":
                            adjacenct_count += 1
                            # print(f"Adjacency count: {adjacenct_count}")
                    self.secret_gameboard[i][j] = adjacenct_count

    def _is_valid(self, row_position, col_position):
        """
        Determine if a position is valid
        Internal helper function
        """
        # Check if x is in position
        if 0 <= row_position <= self.width - 1 and 0 <= col_position <= self.height - 1:
            return True
        else:
            return False

    def get_valid_neighbors(self, row_index, col_index):
        """
        Return array of all valid neighbors for a given cell
        """
        all_neighbors = []
        # Iterate through each direction
        for row_dir, col_dir in self.all_directions:
            new_row_position = row_index + row_dir
            new_col_position = col_index + col_dir

            # Check if valid position
            if self._is_valid(new_row_position, new_col_position):
                # Append to neighbors array
                all_neighbors.append((new_row_position, new_col_position))

        return all_neighbors

    def add_flag(self, row_index, col_index):
        """
        Place a flag in any valid cell on shown gameboard
        """
        if self._is_valid(row_index, col_index) and self.shown_gameboard[row_index][col_index] == "HIDDEN":
            self.shown_gameboard[row_index][col_index] = "FLAG"
            self.number_of_flags += 1
            print(f"Flag added at ({row_index}, {col_index})")
        else:
            print(
                f"({row_index}, {col_index}) not a valid cell to add flag. Please enter valid x and y coordinates")

    def remove_flag(self, row_index, col_index):
        """
        Remove a flag from a cell, re-obfuscate
        """
        if self._is_valid(row_index, col_index) and self.shown_gameboard[row_index][col_index] == "FLAG":
            self.shown_gameboard[row_index][col_index] = "HIDDEN"
            self.number_of_flags -= 1
        else:
            print(
                f"({row_index}, {col_index}) not a valid cell to remove flag. Please enter valid x and y coordinates")

    def reveal_hidden_cell(self, row_index, col_index):
        """
        Reveals cell on obfuscated gameboard.
        If invalid: do nothing
        If cell is flagged: nothing will happen (prompt to remove flag)
        If cell is mine: gameover
        If not flagged, not mine: update cell value to adjacency count
        """
        if self._is_valid(row_index, col_index) == False:
            print(f"({row_index},{col_index}) not on board, please enter valid cell")
            return
        if self.shown_gameboard[row_index][col_index] == "FLAG":
            print(f"({row_index},{col_index}) is flagged, please remove flag or try another cell")
            return
        if self.secret_gameboard[row_index][col_index] == "MINE!":
            print("You hit a bomb! Gameover")
            # TODO: Create method to end game
            return
        else:
            self.shown_gameboard[row_index][col_index] = self.secret_gameboard[row_index][col_index]


new_game = Minesweeper(5, 5)
# new_game.add_random_mines(5)
new_game.add_mine(0, 0)
new_game.add_mine(0, 1)
# new_game.add_mine(1, 2)
# new_game.add_mine(3, 4)
print("Fresh secret gameboard:")
pprint(new_game.secret_gameboard)
new_game.generate_all_adjacency()
print("Secret gameboard after adjacency:")
pprint(new_game.secret_gameboard)
print("Initial shown gameboard:")
pprint(new_game.shown_gameboard)

new_game.add_flag(2, 2)
new_game.add_flag(1, 1)
print("Shown gameboard after adding flags:")
pprint(new_game.shown_gameboard)
#
new_game.remove_flag(2, 2)
print("Shown gameboard after removing flag:")
pprint(new_game.shown_gameboard)
# new_game.remove_flag(50, 50)

new_game.reveal_hidden_cell(4, 4)
print("Shown gameboard after revealing non-mined cell:")
pprint(new_game.shown_gameboard)

print("Trying to reveal flagged cell:")
new_game.reveal_hidden_cell(1, 1)
pprint(new_game.shown_gameboard)

print("Revealing mined cell:")
new_game.reveal_hidden_cell(0, 0)
