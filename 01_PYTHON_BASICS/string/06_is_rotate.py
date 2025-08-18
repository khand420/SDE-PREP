
def is_rotation(s1, s2):
    return len(s1) == len(s2) and s1 in s2 + s2



s1 = "abcde"
s2 = "cdeab"
print(is_rotation(s1, s2))  # Output: True