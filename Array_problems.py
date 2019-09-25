import math

def matrix_in_spiral_order_one(M):
    def matrix_layer_in_clockwise(offset):
        if offset == len(M) - offset - 1:
            # square has odd dimensions
            spiral_ordering.append(M[offset][offset])
            return
        spiral_ordering.extend(M[offset][offset:-1 - offset])
        spiral_ordering.extend(list(zip(*M))[-1 - offset][offset:-1 - offset])
        spiral_ordering.extend(M[-1 - offset][-1 - offset:offset:-1])
        spiral_ordering.extend(list(zip(*M))[offset][-1 - offset:offset:-1])

    spiral_ordering = []

    for offset in range(len(M)+1//2):
        matrix_layer_in_clockwise(offset)

    return spiral_ordering



def plus_one(A):
    A[-1] += 1

    for i in reversed(range(1,len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1

    if A[0] == 10:
        A[0] = 1

        # Holy shit!
        A.append(0)

    return A



def is_valid_sudoku(partial_assignment):


    def has_duplicate(block):
        block = list(filter(lambda x: x != 0, block))
        return len(block) != len(set(block))

    n = len(partial_assignment)

    if any(
        has_duplicate([partial_assignment[i][j] for j in range(n)])
        or
        has_duplicate([partial_assignment[j][i] for j in range(n)])
        for i in range(n)):
        return False

    region_size = int(math.sqrt(n))
    return all(not has_duplicate([partial_assignment[a][b]
                                  for a in range(region_size * I,
                                                 region_size * (I + 1))
                                  for b in range(region_size * J, region_size * (J+1))
                                  ]) for I in range(region_size) for J in range(region_size))
