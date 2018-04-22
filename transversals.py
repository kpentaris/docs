#find transversals algorithm

def submatrix(matrix, removed_row):
    new_matrix = [row[1:] for row in matrix]
    return new_matrix[0:removed_row] + new_matrix[removed_row + 1:]

def find_transversals(matrix, existing):
    if len(matrix) is 0:
        existing.append(existing[-1][:-1])
        return False

    for row in range(len(matrix)):
        found_different = True
        while found_different:
            value = matrix[row][0]
            if value in existing[-1]:
                break
            else:
                existing[-1].append(value)
            found_different = find_transversals(submatrix(matrix, row), existing)
    if (len(existing[-1]) is 0):
        return existing[:-1]
    existing[-1].pop()
    return False
    
find_transversals(latin_square, [[]])
