def maximalSquareBruteForce(matrix):
    if not matrix or not matrix[0]:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    max_side = 0

    # 1. Loop through every possible top-left corner (i, j)
    for i in range(rows):
        print('i', matrix[i])
        for j in range(cols):

            # If the starting cell is '1', it's a potential square
            if matrix[i][j] != 0:
                # Minimum baseline side length for a single '1' is 1
                possible_side = 1
                is_valid_square = True

                # 2. Try expanding the square size (k)
                # The square cannot exceed the boundaries of the matrix
                while (i + possible_side < rows) and (j + possible_side < cols):

                    # Check the new row and column added by expanding to this size
                    # We check the row at index (i + possible_side)
                    for c in range(j, j + possible_side + 1):
                        print('i:', i + possible_side, 'j:', c, 'val:', matrix[i + possible_side][c])
                        if matrix[i + possible_side][c] == 0:
                            is_valid_square = False
                            break

                    # We check the column at index (j + possible_side)
                    for r in range(i, i + possible_side + 1):
                        print('i:', r, 'j:', j + possible_side, 'val:', matrix[r][j + possible_side])
                        if matrix[r][j + possible_side] == 0:
                            is_valid_square = False
                            break

                    # If we found a 0 anywhere in the new boundaries, stop expanding
                    if not is_valid_square:
                        break

                    # If all checked cells were 1, increment the valid side length
                    possible_side += 1

                # Update the overall maximum side length found so far
                max_side = max(max_side, possible_side)

    # Return the final area (side * side)
    return max_side * max_side


if __name__ == '__main__':
    matrix = [
        [2, 3, 4, 0],
        [5, 6, 7, 8],
        [0, 9, 1, 1],
        [0, 1, 1, 1]
    ]
    result = maximalSquareBruteForce(matrix=matrix)
    print(f'result: {result}')
