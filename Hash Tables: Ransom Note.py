from collections import Counter


def checkMagazine(magazine, note):
    if Counter(note) - Counter(magazine) == {}:
        return 'Yes'
    else:
        return 'No'


m, n = map(int, input().split())
magazine = list(input().split())
note = list(input().split())
print(checkMagazine(magazine, note))
