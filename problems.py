# Muhammad Mahd Zeeshan
# 2023462 CS

from node import Node
import copy


class FifteensNode(Node):
    """Extends the Node class to solve the 15 puzzle."""

    def __init__(self, parent=None, g=0, board=None, input_str=None):
        # Initialize the board based on input_str or board
        if input_str:
            self.board = []
            for line in filter(None, input_str.splitlines()):
                self.board.append([int(n) for n in line.split()])
        else:
            self.board = board

        super(FifteensNode, self).__init__(
            parent, g)  # Call parent constructor

        # We can calculate f here, but do not set it directly
        # Store f value in a private variable
        self._f = self.evaluate_heuristic() + self.g

    @property
    def f(self):
        """Returns the f value, which is g + h."""
        return self._f

    @f.setter
    def f(self, value):
        """Setter for f, if you really need to set it somewhere."""
        self._f = value

    def generate_children(self):
        """Generates children by trying all 4 possible moves of the empty cell."""
        children = []
        # right, down, left, up: change in (row, col)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Find the empty tile (0) position
        empty_row, empty_col = next((r, c) for r in range(
            4) for c in range(4) if self.board[r][c] == 0)

        for dr, dc in directions:
            new_row, new_col = empty_row + dr, empty_col + dc
            
            # Check if the new position is within the 4x4 board bounds
            if 0 <= new_row < 4 and 0 <= new_col < 4:  
                # Create a new board state
                new_board = copy.deepcopy(self.board)
                
                # Swap the empty cell (0) with the adjacent cell
                new_board[empty_row][empty_col], new_board[new_row][new_col] = \
                    new_board[new_row][new_col], new_board[empty_row][empty_col]
                    
                # Create a child node (g is increased by 1 for each move)
                child_node = FifteensNode(
                    parent=self, g=self.g + 1, board=new_board)
                children.append(child_node)

        return children

    def is_goal(self):
        """Decides whether this search state is the final state of the puzzle."""
        # The goal state provided in the assignment description
        goal_state = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ]
        return self.board == goal_state

    def evaluate_heuristic(self):
        """Heuristic function h(n) that estimates the minimum number of moves 
        using the **Manhattan distance** (sum of city block distances)."""
        h = 0
        # Pre-calculate goal positions for quick lookup
        goal_positions = {n: (i, j) for i, row in enumerate([[1, 2, 3, 4], [5, 6, 7, 8],
                                                             [9, 10, 11, 12], [13, 14, 15, 0]]) for j, n in enumerate(row)}

        for i in range(4):
            for j in range(4):
                tile = self.board[i][j]
                if tile != 0:  # Skip the empty space (0)
                    goal_i, goal_j = goal_positions[tile]
                    # Manhattan distance: |current_row - goal_row| + |current_col - goal_col|
                    h += abs(goal_i - i) + abs(goal_j - j)

        return h

    def __lt__(self, other):
        return self.f < other.f  # Compare based on f value for the priority queue

    def _get_state(self):
        """Returns a hashable representation of this search state (tuple of board elements)."""
        return tuple(n for row in self.board for n in row)

    def __str__(self):
        """Returns the string representation of this node (formatted board)."""
        sb = []  # String builder
        for row in self.board:
            for i in row:
                sb.append(' ')
                sb.append('  ' if i == 0 else f'{i:2}')
            sb.append('\n')
        return ''.join(sb)


class SuperqueensNode(Node):
    """Extends the Node class to solve the Superqueens problem."""
    # NOTE: No changes were made here as per the assignment instruction:
    # "donot change or modify SuperqueensNode"
    # The methods are left as 'pass' or 'return 0' as in the provided skeleton.

    def __init__(self, parent=None, g=0, queen_positions=[], n=1):
        # NOTE: You shouldn't modify the constructor
        self.queen_positions = queen_positions
        self.n = n
        super(SuperqueensNode, self).__init__(parent, g)

    def generate_children(self):
        """Generates children by adding a new queen."""
        # TODO: add your code here
        pass

    def is_goal(self):
        """Decides whether all the queens are placed on the board."""
        # TODO: add your code here
        pass

    def evaluate_heuristic(self):
        """Heuristic function h(n) that estimates the minimum number of conflicts required to reach the final state."""
        # TODO: add your code here (optional)
        return 0

    def _get_state(self):
        """Returns an hashable representation of this search state."""
        # NOTE: You shouldn't modify this method.
        return tuple(self.queen_positions)

    def __str__(self):
        """Returns the string representation of this node."""
        # NOTE: You shouldn't modify this method.
        sb = [[' . '] * self.n for i in range(self.n)]  # String builder
        for i, j in self.queen_positions:
            sb[i][j] = ' Q '
        return '\n'.join([''.join(row) for row in sb])