# SQL

## `WHERE` vs. `HAVING`
- Both are filter methods.
- `WHERE` filters at the record level
    Example of filtering customers who have never ordered anything (no entry in the Orders table):
    ```sql
    SELECT Customers.name as Customers
    FROM Customers
    LEFT JOIN Orders ON Customers.id=Orders.customerId
    WHERE Orders.id is null
    ```

- `HAVING` filters at the group of records level
    Example of finding unique emails that are duplicated throughout the table:
    ```sql
    SELECT email
    FROM person
    GROUP BY email
    HAVING COUNT(email) > 1
    ```

## Other Functions

### Datediff
Example of rising temperature from previous day:
```sql
SELECT a.id
FROM Weather a
WHERE a.temperature > (
    SELECT temperature
    FROM Weather
    WHERE DATEDIFF(a.recordDate,recordDate) = 1
)
```

### Not Equal
Example where salary is not equal to the max salary (second highest salary):
```sql
SELECT MAX(salary) AS SecondHighestSalary  
FROM employee 
WHERE salary <> (
    SELECT MAX(salary) 
    FROM employee
);
```
