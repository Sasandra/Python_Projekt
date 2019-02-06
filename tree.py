"""Module with classes to maintain board's predictions"""
import numpy as np


class Node:
    """Class to maintain board's state"""

    def __init__(self, board, my_id, move):
        self.board = board
        self.my_id = my_id
        self.opponent_id = 1 - my_id
        self.kids = []
        self.move_from_parent = move

    def __str__(self):
        return '.'.join(str(i) for i in self.board.fields.flatten())

    def generate_kids(self):
        """ Generate all possible boards from actual one"""
        my_legal_moves = self.board.get_legal_moves(self.my_id)
        original_row, original_col = np.where(self.board.fields == str(self.my_id))

        for (row, col), direction in my_legal_moves:
            self.board.fields[original_row[0], original_col[0]] = 'x'
            self.board.fields[row, col] = str(self.my_id)

            opponent_legal_moves = self.board.get_legal_moves(self.opponent_id)
            original_op_row, original_op_col = np.where(self.board.fields == str(self.opponent_id))

            if opponent_legal_moves:
                for (op_row, op_col), _ in opponent_legal_moves:
                    self.board.fields[original_op_row[0], original_op_col[0]] = 'x'
                    self.board.fields[op_row, op_col] = str(self.opponent_id)
                    self.kids.append(Node(self.board, self.my_id, ((row, col), direction)))

            else:
                self.kids.append(Node(self.board, self.my_id, ((row, col), direction)))


class Tree:
    """Class to maintain board's predictions"""

    def __init__(self, board, my_id):
        self.root = Node(board, my_id, ((0, 0), 'None'))
        self.generate_tree()

    def generate_tree(self):
        """Generate tree with height 3"""
        self.root.generate_kids()
        for i in self.root.kids:
            i.generate_kids()
            for j in i.kids:
                j.generate_kids()

    def get_next_move(self):
        """ Get next move from predictions """
        max_length_path = self.get_max_length_path()
        if len(max_length_path) > 2:
            return max_length_path[1].move_from_parent

        return None

    def get_max_length_path(self):
        """Return longest path from root to leaf"""
        paths = self.find_all_paths()
        return max(paths, key=len)

    def find_all_paths(self):
        """Return all paths from root to leaves"""
        path = []
        paths = []
        return self.print_paths(self.root, path, 0, paths)

    def print_paths(self, root, path, path_len, paths):
        """ Recursive function finding all paths from root to leaves
        :param root: actual Node
        :param path: path at given Node
        :param path_len: path's length at given Node
        :param paths: list of all found paths
        """
        if root is None:
            return paths

        if len(path) > path_len:
            path[path_len] = root
        else:
            path.append(root)

        path_len += 1

        if not root.kids:
            paths.append(path[:path_len])
        else:
            for i in root.kids:
                self.print_paths(i, path, path_len, paths)

        return paths
