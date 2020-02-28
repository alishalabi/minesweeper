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

"""

from pprint import pprint


class Minesweeper:
    def __init__(self, width, height):
        """
        Instantiate all class properties
        """
        self.width = width  # Total width of 2d array
        self.height = height  # Total height of 2d array
        self.number_of_mines = 0  # Total number of mines
        self.gameboard = [[None for i in range(width)] for j in range(height)]
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

    # Add a mine in any valid cell
    def add_mine(self, row_index, col_index):
        if self._is_valid(row_index, col_index):
            self.gameboard[row_index][col_index] = "X"

    # Add a random mine
    def add_random_mines(self, num_mines):
        pass

    def generate_all_adjacency(self):
        # Iterate through each cell
        for i in range(len(self.gameboard)):
            for j in range(len(self.gameboard[i])):
                # If cell is itself a mine, do nothing
                if self.gameboard[i][j] == "X":
                    pass
                adjacenct_count = 0
                valid_neighbors = self.get_valid_neighbors(i, j)
                # print(f"Valid neighbors: {valid_neighbors}")
                for x, y in valid_neighbors:
                    print(f"x: {x}, y: {y}")
                    if self.gameboard[x][y] == "X":
                        adjacenct_count += 1
                        # print(f"Adjacency count: {adjacenct_count}")
                self.gameboard[i][j] = adjacenct_count

    # Helper function: is valid position
    def _is_valid(self, row_position, col_position):
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


new_game = Minesweeper(5, 5)
new_game.add_mine(0, 0)
new_game.add_mine(0, 1)
new_game.add_mine(1, 2)
new_game.add_mine(3, 4)
print("Fresh gameboard:")
pprint(new_game.gameboard)
# print(f"Valid neighbors for (1, 1): {new_game.get_valid_neighbors(1, 1)}")
new_game.generate_all_adjacency()
print("Gameboard after adjacency")
pprint(new_game.gameboard)
