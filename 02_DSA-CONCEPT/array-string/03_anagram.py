from collections import Counter

# Function to check if two strings are anagrams
def are_anagrams(s1, s2):
    # Sort both strings and compare
    # return sorted(s1) == sorted(s2)
    # return Counter(s1) == Counter(s2)

    # print(Counter(s1), Counter(s2))
    s1_freq = s2_freq = {}

    for i in s1:
        s1_freq[i] = s1_freq.get(i, 0)+1
    for j in s2:
        s2_freq[j] = s2_freq.get(j, 0)+1   

    print(s1_freq, s2_freq) 

    return s1_freq == s2_freq    



# Test cases
if __name__ == "__main__":
    str1 = "listen"
    str2 = "silent"

    if are_anagrams(str1, str2):
        print("True")
    else:
        print("False")

    str1 = "gram"
    str2 = "arm"

    if are_anagrams(str1, str2):
        print("True")
    else:
        print("False")