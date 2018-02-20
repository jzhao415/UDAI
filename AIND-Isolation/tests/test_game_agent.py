"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
from game_agent import (MinimaxPlayer, AlphaBetaPlayer, CustomPlayer, custom_score,
                        custom_score_2, custom_score_3)

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2, 9, 9)
        self.board0 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 42, 22]
        self.board1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 66, 58]
    def test_example(self):
        rootNode = self.game
        rootNode._board_state = self.board1
        player = CustomPlayer(score_fn=custom_score)
        player.time_left = lambda: 10
        print(rootNode.active_player)
        print(rootNode.to_string())
        print(rootNode.get_legal_moves())
        move = player.alphabeta(rootNode, 2)[1]

        print("Your code chose: {}".format(move))

    def test_example2(self):
        rootNode = self.game
        rootNode._board_state = self.board1
        player = AlphaBetaPlayer(score_fn=custom_score)
        player.time_left = lambda: 10
        print(rootNode.active_player)
        print(rootNode.to_string())
        print(rootNode.get_legal_moves())
        move = player.alphabeta(rootNode, 2)

        print("Your code chose: {}".format(move))


if __name__ == '__main__':
    unittest.main()
