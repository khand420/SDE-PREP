import pandas as pd

# Read CSV with appropriate delimiter
# df = pd.read_csv(r'C:\Users\13\Desktop\python\DSA\python interview\company\nmg\data.csv', delim_whitespace=True) on_bad_lines='skip error_bad_lines=False
try:
    # Adjust the delimiter as necessary
    df = pd.read_csv(r'C:\Users\13\Desktop\python\DSA\python interview\company\nmg\data.csv',on_bad_lines='skip')
    # print(df)
except Exception as e:
    print(f"Error reading the CSV: {e}")

# Print column names to inspect
print("Columns in DataFrame:", df.columns)

# Strip whitespace from column names
# df.columns = df.columns.str.strip()

# Check the DataFrame
# print(df.head())

# # Find students with Math as a subject
students_with_math = df[df['Name'].str.contains('Alice Brown')]
print(students_with_math)


# # b) Find out the students which have hindi as a subject
# student_with_hindi = df[df["Subjects"].str.contains("Hindi")] 
# students_with_hindi = df[df["Subjects"].apply(lambda x: "Hindi" in x )]
# print(students_with_hindi)

# # c) Find out the number of students whoever have a computer science as a subject
student_with_cs = df[df["Subjects"].str.contains("Computer Science")]  
# print(student_with_cs)



# 2. dates are in array format

# dates = ['2012-12-31 08:45', '2019-1-1 12:30', '2008-02-2 10:30',

# '2010-1-1 09:25', '2019-12-31 00:00']

# a) Process the above data using pandas and get day from date in pandas

# Output should be in below format

# Day1 Monday

# Day2 Tuesday

# Day3 Thursday




# Data Structure Questions

# 3. Generate Longest Consequtive Sequence

# Input: arr[] = {1, 9, 3, 10, 4, 20, 2}

# output is :[2, 3, 4, 5]

# Terminology:

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.

def Longest_consc_seq(arr):
    num_set = set(arr)
    longest_streak_arr = []
    longest_streak = 0

    for num in num_set:
        if not num-1 in num_set:
            current_streak = 0
            current_streak_arr = []

            while num+current_streak in num_set:
                current_streak_arr.append(num+current_streak)
                current_streak += 1

            if current_streak > longest_streak:
                longest_streak  = current_streak
                longest_streak_arr = current_streak_arr 

    return  longest_streak_arr, longest_streak          





arr = [1, 9, 3, 10, 4, 20, 2]
print(Longest_consc_seq(arr))






# 4. Valid Anargam

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true

# Example 2:

# Input: s = "jar", t = "jam"

# Output: false


def check_anagram(s, t):
    return sorted(s) == sorted(s) 

s = "racecar"
t = "carrace"

print(check_anagram(s, t))







# 5.Longest Substring Without Duplicates

# Given a string s, find the length of the longest substring without duplicate characters.

# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: s = "zxyzxyz"

# Output: 3

# Explanation: The string "xyz" is the longest without duplicate characters.

# Example 2:

# Input: s = "xxxx"

# Output: 1



def long_substr(s):
    sets = set()
    left = max_len = 0

    for right in range(len(s)):

        while s[right] in sets:
            sets.remove(s[left])
            left+=1
        sets.add(s[right])    
        max_len  = max(max_len, right- left + 1)

    return max_len    

   
s = "zxyzxyz"
print(long_substr(s))    


# MySql Questions

# 6)You have a departments and an employees table. Write a query to find the department with the highest average salary.

# Solution-
# select AVG(salary) as AVERAGE SALARY
# from employees
# LEFT JOIN departments
#  ON employees.id = departments.id 
# order by salary desc limit 1;

 


# 7)Write a query to find departments that have more than 5 employees and whose average salary is greater than $50,000.

# Solution-
# select AVG(salary) , departments
# from employees
# group by departments
# having salary > 50000 limit 5;


# 8.# Write a query to find all customers who have never placed an order. You have a customers table and an orders table.

# Customer Table

# customer_id name

# 1 Alice

# 2 Bob

# 3 Charlie

# 4 David

# 5 Emma

# orders Table:

# order_id customer_id order_date

# 101 1 2024-01-15

# 102 1 2024-02-10

# order_id customer_id order_date

# 103 3 2024-03-12

# 104 4 2024-04-05

# Solution-
# select order_id, customer_id, name,  order_date
# from customer
# RIGHT JOIN orders
# ON customer_id = customer_id
# where order_id = null;



