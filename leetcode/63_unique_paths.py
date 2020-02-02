def num_paths(n, m):

    def num_paths_rec(i=0, j=0):
        if i == n - 1 and j == m - 1:
            return 1

        if i == n or j == m:
            return 0

        return num_paths_rec(i+1, j) + num_paths_rec(i, j+1)

    return num_paths_rec()

print(num_paths(3, 3))

def num_paths_memo(n, m):

    memo = {}
    def num_paths_rec(i=0, j=0):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == n - 1 and j == m - 1:
            return 1

        if i == n or j == m:
            return 0

        memo[(i, j)] = num_paths_rec(i+1, j) + num_paths_rec(i, j+1)

        return memo[(i, j)]

    return num_paths_rec()

print(num_paths_memo(3, 3))
