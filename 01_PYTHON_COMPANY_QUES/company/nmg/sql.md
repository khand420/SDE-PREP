Let's correct the SQL queries you provided:

### 6) Find the department with the highest average salary

**Original Query**:
```sql
select AVG(salary) as AVERAGE SALARY
from employees
LEFT JOIN departments
 ON employees.id = departments.id 
order by salary desc limit 1;
```

**Corrected Query**:
You should group by department and then order by the average salary.

```sql
SELECT departments.name, AVG(employees.salary) AS average_salary
FROM employees
JOIN departments ON employees.department_id = departments.id
GROUP BY departments.name
ORDER BY average_salary DESC
LIMIT 1;
```

### 7) Find departments with more than 5 employees and average salary greater than $50,000

**Original Query**:
```sql
select AVG(salary), departments
from employees
group by departments
having salary > 50000 limit 5;
```

**Corrected Query**:
You need to apply the conditions in the `HAVING` clause correctly and ensure you are grouping by the department.

```sql
SELECT departments.name, COUNT(employees.id) AS employee_count, AVG(employees.salary) AS average_salary
FROM employees
JOIN departments ON employees.department_id = departments.id
GROUP BY departments.name
HAVING employee_count > 5 AND average_salary > 50000;
```

### 8) Find all customers who have never placed an order

**Original Query**:
```sql
select order_id, customer_id, name, order_date
from customer
RIGHT JOIN orders
ON customer_id = customer_id
where order_id = null;
```

**Corrected Query**:
You should use a `LEFT JOIN` to find customers without orders and check for `NULL` in the `order_id`.

```sql
SELECT customers.customer_id, customers.name
FROM customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id
WHERE orders.order_id IS NULL;
```

### Summary of Corrections:
1. **Query 6**: Properly grouped by department and ordered by average salary.
2. **Query 7**: Correctly counted employees and applied conditions in the `HAVING` clause.
3. **Query 8**: Used `LEFT JOIN` and checked for `NULL` in `order_id` to find customers without orders.

Feel free to ask if you need further assistance!