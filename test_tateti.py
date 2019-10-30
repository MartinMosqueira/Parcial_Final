import unittest
from parameterized import parameterized
from tateti import TaTeTi

class TaTeTiTest(unittest.TestCase):

    def test_initilization(self):
        tateti = TaTeTi()
        first = [' ' for _ in range(9)]
        self.assertEqual(tateti.board, first)

    @parameterized.expand([
        ([['x', 'o', 'x', 'o', 'x', 'o', 'x', 'o', 'x']]),
        ([['o', 'x', 'o', 'x', 'o', 'x', 'o', 'x', 'o']]),
        ([['x', 'x', 'o', 'o', 'x', 'x', 'o', 'o', 'x']]),
        ([['o', 'o', 'x', 'x', 'o', 'o', 'x', 'x', 'o']]),
        ([['o', 'x', 'x', 'o', 'o', 'x', 'x', 'o', 'o']]),
        ([['x', 'o', 'o', 'x', 'x', 'o', 'o', 'x', 'x']])
    ])
    def test_full(self, board):
        tateti = TaTeTi(board)
        self.assertTrue(tateti.full())

    @parameterized.expand([
        ([['x', 'o', 'x', 'o', ' ', 'o', 'x', 'o', 'x']]),
        ([['o', 'x', 'o', ' ', 'o', ' ', 'o', 'x', 'o']]),
        ([['x', 'x', 'o', ' ', 'x', 'x', ' ', ' ', 'x']]),
        ([['o', ' ', 'x', ' ', 'o', ' ', 'x', ' ', 'o']]),
        ([[' ', ' ', 'x', ' ', 'o', 'x', ' ', 'o', ' ']]),
        ([['x', ' ', ' ', 'x', ' ', ' ', 'o', ' ', ' ']])
    ])
    def test_not_full(self, board):
        tateti = TaTeTi(board)
        self.assertFalse(tateti.full())

    @parameterized.expand([
        ([['x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ']]),
        ([['o', 'o', 'o', ' ', ' ', ' ', ' ', ' ', ' ']]),
        ([[' ', ' ', ' ', 'x', 'x', 'x', ' ', ' ', ' ']]),
        ([[' ', ' ', ' ', 'o', 'o', 'o', ' ', ' ', ' ']]),
        ([[' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x']]),
        ([[' ', ' ', ' ', ' ', ' ', ' ', 'o', 'o', 'o']]),
        ([['x', ' ', ' ', 'x', ' ', ' ', 'x', ' ', ' ']]),
        ([['o', ' ', ' ', 'o', ' ', ' ', 'o', ' ', ' ']]),
        ([[' ', 'x', ' ', ' ', 'x', ' ', ' ', 'x', ' ']]),
        ([[' ', 'o', ' ', ' ', 'o', ' ', ' ', 'o', ' ']]),
        ([[' ', ' ', 'x', ' ', ' ', 'x', ' ', ' ', 'x']]),
        ([[' ', ' ', 'o', ' ', ' ', 'o', ' ', ' ', 'o']]),
        ([['x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x']]),
        ([[' ', ' ', 'x', ' ', 'x', ' ', 'x', ' ', ' ']]),
        ([['o', ' ', ' ', ' ', 'o', ' ', ' ', ' ', 'o']]),
        ([[' ', ' ', 'o', ' ', 'o', ' ', 'o', ' ', ' ']])
    ])
    def test_win(self, board):
        tateti = TaTeTi(board)
        self.assertTrue(tateti.win())


if __name__ == '__main__':
    unittest.main()