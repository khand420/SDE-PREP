
def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    # if s == reversed(s):
    #     return true
    # else:
    #     return false

    s = s.lower()
    original = ""
    reverse = ""

    for i in s:
        if i.isalnum():
            original += i
            reverse = i+reverse
    # print(original, reverse)
    # revere = original[::-1]
    # print(revere)
    return original == original

s = "A man, a plan, a canal: Panama"
# "race a car"
print(isPalindrome(s))