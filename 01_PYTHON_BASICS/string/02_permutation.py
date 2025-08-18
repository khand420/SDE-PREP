from itertools import permutations, combinations


def string_permutations(s):
    # print(list(combinations(s, 3)))
    print(list(permutations(s)))
    return [''.join(p) for p in permutations(s)]




s = "abc"
print(string_permutations(s))