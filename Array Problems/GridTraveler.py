# m,n ---Dimension of the gridTravler
def grid_traveller(m, n):
    memo = {"1,1": 1}

    def helper(m, n):
        key = f"{m},{n}"
        if m == 0 or n == 0:
            return 0
        if key in memo:
            return memo[key]
        if key in memo:
            return memo[key]
        memo[key] = helper(m - 1, n) + helper(m, n - 1)
        return memo[key]

    return helper(m, n)


print(grid_traveller(50,10))