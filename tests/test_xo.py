import pytest

import xo


@pytest.mark.parametrize(
    "board,finished",
    [
        (
            # board
            [
                [" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "],
            ],
            # finished?
            "",
        ),
        (
            # board
            [
                ["X", "X", "O"],
                ["O", "X", "X"],
                ["X", "O", "O"],
            ],
            # finished?
            "stalemate",
        ),
        (
            # board
            [
                ["X", "X", "X"],
                [" ", " ", " "],
                [" ", " ", " "],
            ],
            # finished?
            "X",
        ),
        (
            # board
            [
                [" ", "O", "X"],
                [" ", "O", " "],
                [" ", "O", "O"],
            ],
            # finished?
            "O",
        ),
        (
            # board
            [
                ["X", "X", "O"],
                [" ", "X", " "],
                ["O", "O", "X"],
            ],
            # finished?
            "X",
        ),
        (
            # board
            [
                ["X", "X", "O"],
                [" ", "O", " "],
                ["O", "O", "X"],
            ],
            # finished?
            "O",
        ),
    ],
)
def test_finished(board, finished):
    assert xo.finished(board) == finished
