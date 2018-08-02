def cascade(matrix, i, j):
    cascade_right = matrix[i][j]
    cascade_down = matrix[i][j]
    for k in range(i, len(matrix[0])):
        cascade_down = max(cascade_down, matrix[k][j])
        matrix[k][j] = cascade_down
    for k in range(j, len(matrix[0])):
        cascade_right = max(cascade_right, matrix[i][k])
        matrix[i][k] = cascade_right
    return matrix


def highest_substr(str1, str2):
    matrix = [len(str1) * [0] for i in range(len(str1))]
    size = len(str1)
    for i in range(size):
        for j in range(size):
            # for col in range(size):
            #     for row in range(size):
                    # if row == i and col == j:
                    #     print("*" + str(matrix[row][col]) + "*", end="")
                    # else:
                    #     print(" " + str(matrix[row][col]) + " ", end="")
                # print()
            # print()
            # input()
            is_letter_used = matrix[i][j] != 0
            is_matched = str1[i] == str2[j]

            if i > 0:
                matrix[i][j] = max(matrix[i][j], matrix[i-1][j])

            if is_matched:
                if is_letter_used:
                    if i > 0 and j > 0 and matrix[i][j] == matrix[i-1][j-1]:
                        matrix[i][j] += 1
                        cascade(matrix, i, j)
                else:
                    matrix[i][j] += 1
                    cascade(matrix, i, j)

    return matrix[size-1][size-1]

# str1 = "shinchan"
# str2 = "noharaaa"
# str1 = "abbcd"
# str2 = "abcdw"
str1 = "abcdef"
str2 = "fbdamn"

print(highest_substr(str1, str2))
