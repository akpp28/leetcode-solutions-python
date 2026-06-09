def maximal_square_simplified(matrix):
    """
    width /wɪdθ/
    height /haɪt/
    """
    rows = len(matrix)
    cols = len(matrix[0])
    # max width and height
    max_side_length = 0

    for x in range(rows):
        print(matrix[x])
        for y in range(cols):
            # print(matrix[x][y])
            if matrix[x][y] != 0:
                max_possible_side_length = 1
                is_valid_square = True
                # Try expanding the square size
                # The square cannot exceed the boundaries of the matrix

                # Expand x asix
                for next_x in range(max_side_length, max_side_length + 1):
                    print('next_x', next_x, matrix[next_x][y])
                    if matrix[next_x][y] == 0:
                        is_valid_square = False
                        break

                # Expand y asix
                for next_y in range(max_side_length, max_side_length + 1):
                    print('next_y', next_y, matrix[x][next_y])
                    if matrix[x][next_y] == 0:
                        is_valid_square = False
                        break

                # If we found a 0 anywhere in the new boundaries, stop expanding
                if not is_valid_square:
                    break

                max_possible_side_length += 1

                max_side_length = max(max_side_length, max_possible_side_length)

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
