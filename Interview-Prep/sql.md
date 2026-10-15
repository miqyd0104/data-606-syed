[sql.md](https://github.com/user-attachments/files/33501690/sql.md)
# SQL

### 1. What is SQL and what is it used for?

“SQL stands for Structured Query Language. We use it to work with data in relational databases—retrieving records, adding or updating them, and creating structures like tables.

For example, an online shop could use SQL to find a customer's orders or calculate monthly sales. In data engineering, we also use it to clean, combine and prepare data for reporting.”

### 2. What is the difference between a database and a table?

“A database holds and organises data, while a table is one structure inside it. A table stores records in rows, with columns describing each record.

For example, a shop's database could contain separate tables for customers, products and orders. Those tables can be linked, so we can find out which customer placed each order.”

### 3. What is a primary key?

“A primary key uniquely identifies each row in a table. It can't contain duplicate or null values, and it can consist of one column or a combination of columns.

For example, two customers could have the same name, but their customer IDs would be different. That lets us identify the right person without relying on details that might repeat or change.”

### 4. What is a foreign key?

“A foreign key links records by referencing a primary or other unique key in a related table.

For example, an order could contain a customer ID that references the customers table. The database can then prevent an order from being assigned to a customer who doesn't exist.

That helps keep relationships between records valid.”

### 5. What is the purpose of SELECT?

“`SELECT` tells the database which columns or calculated values we want to retrieve. We can combine it with other clauses to filter, group and sort the results.

For example, I could select customer names and email addresses rather than return every column. That makes the output more relevant and avoids retrieving information I don't need.”

### 6. What is the difference between WHERE and HAVING?

“`WHERE` filters individual rows before grouping, while `HAVING` filters the groups after aggregation.

For example, I could use `WHERE` to select orders from this year, then group them by customer and use `HAVING` to keep only customers who spent over £1,000.

They're useful at different stages: one filters the original records, and the other filters the calculated group results.”

### 7. What is the difference between COUNT(*) and COUNT(column_name)?

“`COUNT(*)` counts all rows in the result or group. `COUNT(column_name)` counts only the rows where that column isn't null.

For example, if I have ten customers but only eight have an email address, `COUNT(*)` returns ten and `COUNT(Email)` returns eight.

So I'd choose based on whether I'm counting records or populated values.”

### 8. What is a NULL value?

“`NULL` means a value is missing, unknown or not applicable. It isn't the same as zero or an empty string.

For example, an order might have a null delivery date because it hasn't been delivered yet. I'd check for that using `IS NULL`, rather than `= NULL`.

Understanding the meaning matters before deciding how to handle it.”

### 9. How do you sort data in SQL?

“We use `ORDER BY`. `ASC` sorts in ascending order and is normally the default, while `DESC` sorts in descending order.

For example, I could sort products by price from highest to lowest. I can also sort by several columns, such as order date and then order ID.

Without `ORDER BY`, I shouldn't assume the rows will come back in a particular order.”

### 10. What are the different types of joins?

“Joins bring related data together. The main types are:

- **INNER JOIN:** returns matching rows.
- **LEFT JOIN:** keeps every left-table row, with matching right-table data where available.
- **RIGHT JOIN:** does the reverse.
- **FULL OUTER JOIN:** keeps matched and unmatched rows from both sides.
- **CROSS JOIN:** returns every possible combination.

A self join means joining a table to itself—for example, connecting employees to their managers. Support for particular join syntax varies between databases.”

### 11. What is the difference between INNER JOIN and LEFT JOIN?

“An inner join returns only rows that match on both sides. A left join keeps every row from the left table, even when there's no match on the right.

For example, joining customers to orders with an inner join shows customers who have orders. A left join also includes customers who haven't ordered, with nulls for the order details.

That's useful when looking for missing relationships.”

### 12. What is the difference between UNION and UNION ALL?

“Both combine the rows returned by separate queries. `UNION` removes duplicate result rows, while `UNION ALL` keeps them.

For example, I could combine customer lists from two sources. If I need every row preserved, I'd use `UNION ALL`.

`UNION ALL` usually requires less work because it doesn't remove duplicates. The queries also need compatible columns in the same positions.”

### 13. What is normalisation, and why is it important?

“Normalisation organises relational data into appropriate tables to reduce unnecessary duplication and avoid inconsistent changes.

For example, we could store a customer's current contact details once and link their orders using a customer ID.

That means we can update the details in one place rather than risk leaving conflicting copies across several records.”

### 14. How would you find duplicate records in a table?

“First, I'd decide what makes a record a duplicate. Then I'd group by those fields and use `HAVING COUNT(*) > 1`.

For example, this finds email values that appear more than once:”

```sql
SELECT Email, COUNT(*) AS Occurrences
FROM Customers
WHERE Email IS NOT NULL
GROUP BY Email
HAVING COUNT(*) > 1;
```

“I'd investigate the results before deleting anything, because sharing an email address doesn't automatically mean two customer records are duplicates.”

### 15. How would you return the top N rows from a table?

“I'd use the row-limiting syntax for the database and an `ORDER BY` that defines what ‘top’ means.

For example, in MySQL, this returns the five highest-priced products:”

```sql
SELECT ProductID, ProductName, UnitPrice
FROM Products
ORDER BY UnitPrice DESC, ProductID
LIMIT 5;
```

“SQL Server commonly uses `TOP`. The extra product ID makes the ordering predictable when prices are equal.”

### 16. How do aggregate functions work?

“Aggregate functions summarise multiple rows into a result. Examples include `SUM`, `AVG`, `COUNT`, `MIN` and `MAX`.

For example, I could group orders by customer and calculate each customer's total spending using `SUM`.

Most common aggregates ignore null inputs, while `COUNT(*)` counts rows. That matters because missing values can affect how we interpret the result.”

### 17. What is the difference between CHAR and VARCHAR?

“`CHAR` is intended for fixed-length text, while `VARCHAR` stores variable-length text up to a defined limit.

For example, `CHAR` could suit a consistently sized code, while `VARCHAR` suits customer names because their lengths vary.

`CHAR` generally involves padding shorter values, although storage and trailing-space behaviour depend on the database.”

### 18. What is an index?

“An index is an additional structure that helps the database locate data more efficiently, instead of checking every row.

For example, an index on a frequently searched customer ID can speed up lookups and joins.

The trade-off is that indexes take storage and need maintaining when data changes. I'd index based on the queries we actually run rather than add one to every column.”

### 19. What is the difference between a clustered and nonclustered index?

“A clustered index determines how the table's rows are organised at the storage level. A nonclustered index is a separate structure containing indexed values and references to the corresponding rows.

There can only be one clustered organisation, but there can be several nonclustered indexes.

For example, a table might be clustered by customer ID and have a nonclustered index on email for searches. The implementation varies by database; MySQL's InnoDB normally clusters data by the primary key.”

### 20. What is a view, and when would you use one?

“A view is a named query that we can use much like a table. A regular view normally stores the query definition rather than a separate copy of its results.

For example, I could create a view that joins customers and orders, so report writers don't repeat the same join.

It can simplify access and expose selected columns, although access restrictions still need appropriate permissions.”

### 21. What is the difference between a subquery and a CTE?

“A subquery is a query nested inside another statement. A CTE, or Common Table Expression, defines a named query using `WITH`, which the following statement can reference.

For example, I could use a CTE to calculate customer totals, then filter those totals in the main query.

Both can help break down a problem. CTEs are often easier to follow when there are several steps, but they aren't automatically faster.”

### 22. What are window functions?

“Window functions calculate across related rows while keeping the individual rows in the result.

For example, I could show every order alongside that customer's total spending, or rank products by sales within each category.

The `OVER` clause defines the rows used for the calculation. Unlike `GROUP BY`, a window function doesn't collapse those rows into one summary row, which is useful when we need detail and a comparison together.”

---

[Back to Interview Prep](README.md)
