import pytest

from google_maximal_square_simplified import maximal_square_simplified

CASES = [
    pytest.param(
        [
            [2, 3, 4, 0],
            [5, 6, 7, 8],
            [0, 9, 1, 2],
            [0, 3, 4, 5]
        ],
        9,
        id='example_from_problem',
    ),
    pytest.param(
        [
            [1, 0, 1, 0, 0],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0]
        ],
        4,
        id='leetcode_classic_case',
    ),
    pytest.param([[0]], 0, id='single_cell_zero'),
    pytest.param([[1]], 1, id='single_cell_one'),
    pytest.param([[0, 0], [0, 0]], 0, id='all_zeros'),
    pytest.param([[1, 1], [1, 1]], 4, id='all_ones_square'),
    pytest.param([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 9, id='all_ones_3x3'),
    pytest.param([[1, 1, 0, 1, 1]], 1, id='single_row'),
    pytest.param([[1], [1], [0], [1]], 1, id='single_column'),
    pytest.param(
        [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ],
        1,
        id='checkerboard_no_square_larger_than_one',
    ),
    pytest.param(
        [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 0]
        ],
        9,
        id='3x3_square_in_top_left',
    ),
]


@pytest.mark.parametrize('matrix, expected', CASES)
def test_maximal_square_simplified(matrix, expected):
    assert maximal_square_simplified(matrix) == expected
