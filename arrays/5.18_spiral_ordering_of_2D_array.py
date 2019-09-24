

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












if __name__ == "__main__":
    matrix_1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    matrix_2 = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
    ]

    matrix_3 = [
        [1,2,3],
        [4,5,6],
        [7, 8, 9],
        [10,11,12]
    ]


    matrix_in_spiral_order_one(matrix_1)