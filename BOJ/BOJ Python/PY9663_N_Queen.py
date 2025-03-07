def check(x):
    for i in range(x):
        if row[i] == row[x] or abs(row[x] - row[i]) == x-i:
            return False
    return True


def dfs(x):
    global count
    if x == n:
        count += 1
    else:
        for i in range(n):
            row[x] = i
            if check(x):
                dfs(x+1)


n = int(input())

row = [0] * n
count = 0
dfs(0)

print(count)
