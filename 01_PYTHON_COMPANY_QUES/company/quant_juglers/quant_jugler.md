Narender Daravathu
16:13
write a program to examine whether the pairs and the orders of “{“, “}”, “(“, “)”, “[“, “]” are correct in the given expression.
Input: exp = “[()]{}{[()()]()}”
Balanced
Narender Daravathu
16:31

Product table
+-----------+-------------+-------------+-------+
| ProductID | ProductName | Category    | Price |
+-----------+-------------+-------------+-------+
| 1         | Laptop      | Electronics | 800   |
| 2         | Smartphone  | Electronics | 400   |
| 3         | T-shirt     | Apparel     | 20    |
| 4         | Headphones  | Electronics | 50    |
| 5         | Jeans       | Apparel     | 45    |
+-----------+-------------+-------------+-------+
Order table -

+---------+--------------+-----------+----------+------------+
| OrderID | CustomerName | ProductID | Quantity | OrderDate  |
+---------+--------------+-----------+----------+------------+
| 1       | Alice        | 1         | 2        | 2023-01-10 |
| 2       | Bob          | 3         | 5        | 2023-02-15 |
| 3       | Alice        | 2         | 1        | 2023-03-20 |
| 4       | Carol        | 5         | 3        | 2023-04-05 |
| 5       | Bob          | 1         | 1
Interview Meet _Danish khan@Loyalty Juggernaut India Pvt. Ltd.

Alice-1600



To achieve the output where we calculate the total amount spent by the customer "Alice," you can write a SQL query that:

1. **Joins** the `Order` table with the `Product` table using the `ProductID`.
2. **Filters** for the specific customer ("Alice").
3. **Calculates** the total cost by multiplying the `Quantity` by the `Price` for each order and then summing it up.

Here is the SQL query to achieve that:

```sql
SELECT 
    CustomerName, 
    SUM(Quantity * Price) AS TotalAmountSpent
FROM 
    `Order`
JOIN 
    Product 
ON 
    `Order`.ProductID = Product.ProductID
WHERE 
    CustomerName = 'Alice'
GROUP BY 
    CustomerName;
```

### Explanation:

- **JOIN**: We join the `Order` table with the `Product` table on the `ProductID` column to get the price of each product.
- **WHERE**: We filter the results to include only the orders placed by "Alice."
- **SUM**: We calculate the total amount spent by summing up the product of `Quantity` and `Price` for each order.
- **GROUP BY**: Since we are calculating the total amount spent by "Alice," we group by the `CustomerName`.

### Result:

For the provided data, the output will be:

```
+--------------+------------------+
| CustomerName | TotalAmountSpent |
+--------------+------------------+
| Alice        | 1600             |
+--------------+------------------+
```

This query correctly calculates that Alice spent a total of $1600 (2 Laptops × $800).







--------------Talnet101-----------




