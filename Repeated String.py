def repeated_string(s, n):
    return n // len(s) * s.count('a') + s[0: n % len(s)].count('a')


s = input()
n = int(input())
print(repeated_string(s, n))
