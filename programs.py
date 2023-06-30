def max_profit(prices):
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price

    return max_profit

prices = [7,6,4,3,1]
max_profit = max_profit(prices)
print(max_profit)

def rotate(matrix):
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]

    return matrix

matrix =[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotated_matrix = rotate(matrix)
print(rotated_matrix)

def longestIncreasingPath(matrix):
    if not matrix:
        return 0

    n = len(matrix)
    m = len(matrix[0])
    cache = [[0 for _ in range(m)] for _ in range(n)]
    max_length = 0

    def dfs(i, j):
        if cache[i][j] != 0:
            return cache[i][j]

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_path = 1

        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < n and 0 <= y < m and matrix[x][y] > matrix[i][j]:
                max_path = max(max_path, 1 + dfs(x, y))

        cache[i][j] = max_path
        return max_path

    for i in range(n):
        for j in range(m):
            max_length = max(max_length, dfs(i, j))

    return max_length

matrix =[[1]]
max_length = longestIncreasingPath(matrix)
print(max_length)