
# the sequences
SEQ1 = "-GAATTCAGTTA"
SEQ2 = "-GGATCGA"

# the length of these sequences is pretty

# widely used
SEQ1_N1 = len(SEQ1)
SEQ2_N1 = len(SEQ2)

# scoring scheme
MATCH = 2 
MISMATCH = -1
GAP = -1

# some traceback constants
DIAGONAL = 1
DOWN = 2
RIGHT = 3

def main():
    # build the matrix
    matrix = []
    traceback = []

    for i in range(SEQ1_N1):
        matrix.append([])
        traceback.append([])

    # initialize the first column to zeroes
    for i in range(SEQ1_N1):
        matrix[i].append(0)
        traceback[i].append(0)

    # initialize the first row to zero
    for i in range(1, SEQ2_N1):
        matrix[0].append(0)
        traceback[0].append(0)


    # loop through each of the unfilled spaces
    # and use the score function to give the correct value
    for i in range(1, SEQ1_N1):
        for j in range(1, SEQ2_N1):
            matrix[i].append(score(i,j,matrix, traceback))

    for m in matrix:
        print m

    print "-----------------"
    for t in traceback:
        print t

    traceback_function(matrix, traceback)

# calculate the score of cell i, j using the formula
# Si,j = MAXIMUM[
# Si-1, j-1 + s(ai,bj) (match/mismatch in the diagonal), 
# Si,j-1 + w (gap in sequence #1), 
# Si-1,j + w (gap in sequence #2), 
# 0
# ]
def score(i, j, matrix, traceback):

    if SEQ1[i] == SEQ2[j]:
        match_score = MATCH
    else:
        match_score = MISMATCH


    diagonal = matrix[i-1][j-1] + match_score
    right = matrix[i][j-1] + GAP
    down = matrix[i-1][j] + GAP

    # store the tracebacks in a matrix
    #    1 - means we came here diagonally
    #    2 - means we came here from above
    #    3 - means we came here from the right
    if max(diagonal, down, right) == diagonal:
        traceback[i].append(DIAGONAL)
    elif max(diagonal, down, right) == down:
        traceback[i].append(DOWN)
    elif max(diagonal, down, right) == right:
        traceback[i].append(RIGHT)

    return max(diagonal, down, right, 0)


def traceback_function(matrix, traceback):
    solved_seq1 = ""
    solved_seq2 = ""

    max_i = max_j = cur_max = 0

    # first we need to find the max element in the matrix
    for i in range(SEQ1_N1):
        for j in range(SEQ2_N1):
            if matrix[i][j] > cur_max:
                max_i = i
                max_j = j
                cur_max = matrix[i][j]

    current_cell = traceback[max_i][max_j]
    cur_i = max_i
    cur_j = max_j

    while (current_cell != 0):

        if current_cell == DIAGONAL:
            solved_seq1 += SEQ1[cur_i]
            solved_seq2 += SEQ2[cur_j]
            cur_i = cur_i - 1
            cur_j = cur_j - 1
            current_cell = traceback[cur_i][cur_j]

        elif current_cell == DOWN:
            solved_seq1 += SEQ1[cur_i]
            solved_seq2 += "-"
            cur_i = cur_i - 1

            current_cell = traceback[cur_i][cur_j]
        elif current_cell == RIGHT:
            solved_seq1 += "-"
            solved_seq2 += SEQ2[cur_j]
            cur_j = cur_j - 1
            current_cell = traceback[cur_i][cur_j]


    print solved_seq2[::-1]
    print solved_seq1[::-1]

if __name__ == "__main__":
    main()
