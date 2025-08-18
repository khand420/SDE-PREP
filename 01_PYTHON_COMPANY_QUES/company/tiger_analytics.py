# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# print("Try programiz.pro")


# out = 7,6,1
# o
def findLeaders(lst):
    new_lst = []
    n = len(lst)
    
    # Start from the last element, which is always a leader
    max_from_right = lst[n - 1]
    new_lst.append(max_from_right)

    # Traverse the list from second last to the first element
    for i in range(n - 2, -1, -1):
        if lst[i] > max_from_right:
            max_from_right = lst[i]
            new_lst.append(max_from_right)

    # Since we collected leaders in reverse order, reverse the list before returning
    return new_lst[::-1]

# lst = [1, 2, 7, 5, 6, 1]
lst =  [2,7,5,8,1]
print(findLeaders(lst))  # Output: [7, 6, 1]



# # lst =  [1,2,7,5,6,1]
# lst =  [2,7,5,8,1]

# print(findLeaders(lst))

# Employee

#  dep, name, salary 

# select dep, max(salary) from employee
# group by dep ;


# select name, dep, max(salary) from employee
# group by dep  ;


# name, dep, salary
# a1, d1, 1000
# a2, d1, 2000
# a3, d2, 3000
# a4, d2, 4000


# # data = Employee.objects.all().aggregate(MAX('salary'))

# from django.db.models import Max
# from django.db.models import F

# result = (Employee.objects
#     .values('dep')
#     .annotate(max_salary=Max('salary'))
#     .annotate(employee_ids=ArrayAgg('id'))  # Collecting IDs
#     .annotate(employee_names=ArrayAgg('name'))  # Collecting names
# )

# This will give you a queryset with each department, its max salary, and lists of employee IDs and names.




# second_last_salary = Employee.objects.order_by('-salary')[1]
# print(second_last_salary.salary)  # This will print the second last salary

# n = 5  # Replace with the desired number of top salaries
# top_salaries = Employee.objects.order_by('-salary')[:n]
# for employee in top_salaries:
#     print(employee.salary)  # This will print the top n salaries




# from django.db.models import Max

# # Step 1: Find the maximum salary
# max_salary = Employee.objects.aggregate(Max('salary'))['salary__max']

# # Step 2: Retrieve all fields for employees with the maximum salary
# employees_with_max_salary = Employee.objects.filter(salary=max_salary)

# # Print the results
# for employee in employees_with_max_salary:
#     print(employee.id, employee.name, employee.dep, employee.salary)  # Adjust fields as necessary
