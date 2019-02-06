"""Module for testing Tree class"""
import unittest


class Node:
    """Class to maintain example node"""

    def __init__(self, board):
        self.board = board
        self.kids = []

    def __str__(self):
        return '.'.join(str(i) for i in self.board.fields.flatten())

    def set_kids(self, kids):
        """
        Set given list as value for attribute kids
        :param kids: list of kids
        :return:
        """
        self.kids = kids


class Tree:
    """Class to maintain example tree"""

    def __init__(self, board):
        self.root = Node(board)

    def get_next_move(self):
        """ Get next move from predictions """
        max_length_path = self.get_max_length_path()
        return max_length_path[0]

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
            path[path_len] = root.board
        else:
            path.append(root.board)

        path_len += 1

        if not root.kids:
            paths.append(path[:path_len])
        else:
            for i in root.kids:
                self.print_paths(i, path, path_len, paths)
        return paths


class PlayerTest(unittest.TestCase):
    """Player Class Unit Test Class"""

    def setUp(self):
        self.tree = Tree(3)
        self.tree.root.set_kids([Node(1), Node(2)])
        self.tree.root.kids[0].set_kids([Node(4), Node(5)])
        self.tree.root.kids[0].kids[1].set_kids([Node(6)])

    def test_print_paths(self):
        """Return True if all paths are calculated properly, False otherwise. """
        paths = self.tree.find_all_paths()
        self.assertEqual(paths, [[3, 1, 4], [3, 1, 5, 6], [3, 2]])

    def test_get_max_length_path(self):
        """Return True if good longest path is returned, False otherwise"""
        max_length_path = self.tree.get_max_length_path()
        self.assertEqual(max_length_path, [3, 1, 5, 6])

    def test_get_next_move(self):
        """ Return True if proper element from path is returned, False otherwise."""
        next_move = self.tree.get_next_move()
        self.assertEqual(next_move, 3)
