def array_left_rotation(a, k):
    result = a[k:] + a[:k]
    return result


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
print(*array_left_rotation(a, k))
