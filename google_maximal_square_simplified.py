def maximal_square_simplified(matrix):
    """
    width /wɪdθ/
    height /haɪt/


    """
    rows = len(matrix)
    cols = len(matrix[0])
    max_side_length = 0

    for x in range(rows):
        for y in range(cols):
            if matrix[x][y] != 0:

                is_valid = True

                # Calculate the maximum boundary limit for the current (x, y)
                # The Goal: Checking the "Outer Shell"
                max_limit = min(rows - x, cols - y)
                for size in range(1, max_limit + 1):

                    # 1. TOP-TO-BOTTOM FIRST (X-axis)
                    # We scan down the right wall, starting from the higher rows
                    for next_x in range(x, x + size):
                        if matrix[next_x][y + size - 1] == 0:
                            is_valid = False
                            break

                    # 2. LEFT-TO-RIGHT SECOND (Y-axis)
                    # Only after checking the top parts do we check the very bottom floor
                    for next_y in range(y, y + size):
                        if matrix[x + size - 1][next_y] == 0:
                            is_valid = False
                            break

                    # If we found a 0 anywhere in the new boundaries, stop expanding
                    if not is_valid:
                        break

                    max_side_length = max(max_side_length, size)

    # Return the final area (side * side)
    return max_side_length * max_side_length


if __name__ == '__main__':
    result = maximal_square_simplified(matrix=[
        [2, 3, 4, 0],
        [5, 6, 7, 8],
        [0, 9, 1, 2],
        [0, 3, 4, 5]
    ])
    print(f'result: {result}')
