def maximal_square_simplified(matrix):

    rows = len(matrix)
    cols = len(matrix[0])
    max_side_length = 0

    for x in range(rows):
        for y in range(cols):
            if matrix[x][y] == 0:
                continue

            # Calculate the maximum boundary limit for the current (x, y)
            max_limit = min(rows - x, cols - y)
            for size in range(max_side_length + 1, max_limit + 1):
                # The "Outer Shell": right wall (X-asis) then bottom floor (Y-asis)
                right_wall_ok = all(matrix[next_x][y + size - 1] for next_x in range(x, x + size))
                bottom_floor_ok = all(matrix[x + size - 1][next_y] for next_y in range(y, y + size))
                
                if not right_wall_ok or not bottom_floor_ok:
                    break

                max_side_length = size

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
