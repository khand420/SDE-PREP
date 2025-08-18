

# Write a function to reverse a string.

def reverse_string(s):
    return s[::-1]


# Write a function to return the n-th number in the Fibonacci sequence.


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Write a function to check if a given string is a palindrome.



def is_palindrome(s):
    return s == s[::-1]


# Find the Largest Element in an Array:
# Write a function to find the largest element in a given list.


def find_largest(arr):
    if not arr:
        return None
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    return largest


# Count Vowels in a String:
# Write a function to count the number of vowels in a given string.

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


# Find the Second Largest Element in an Array:
# Write a function to find the second largest element in a given list.



def find_second_largest(arr):
    if len(arr) < 2:
        return None
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    return second

find_second_largest([3,4,5,7,8,2])

# Find Duplicates in an Array:
# Write a function to find all the duplicates in a list.
# python
# Copy code


def find_duplicates(arr):
    from collections import Counter
    counter = Counter(arr)
    return [item for item, count in counter.items() if count > 1]



# Merge Two Sorted Lists:
# Write a function to merge two sorted lists into a single sorted list.



def merge_sorted_lists(list1, list2):
    merged_list = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list


# Write a function to check if two strings are anagrams of each other.


def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)


# Write a function to find the longest common prefix string amongst an array of strings.

def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while s[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix