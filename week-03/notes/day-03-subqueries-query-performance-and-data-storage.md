# Day 3 — Subqueries, query performance and data storage

7 October 2026

[← Week 3](../README.md) · [Previous notes: Database design and stored procedures](day-02-database-design-and-stored-procedures.md)

Today brought together more SQL querying techniques: filtering, grouped results, subqueries, views and copying query results into a table. We also looked at why similar queries can perform differently, how indexes help, and how operational databases fit into a wider data pipeline.

## Interview practice and the morning recap

I identified Microsoft SQL Server as the database management system we have been using, and answered a question about entity relationship diagrams. The feedback on my ERD answer was to give enough context for someone who has not seen our training work.

Rather than referring to “the course table” without explaining it, describe the problem, what the tables represent and how the diagram communicates their relationships. Mentioning the keys, column types and relationship notation helps show understanding. Any example of my own work needs to be something I can explain properly.

The wider advice was to define the concept first, then support the answer with an example. If a term does not come to mind, explain the relevant ideas I do understand and work through the question rather than guessing confidently.

### Database, DBMS and SSMS

| Term | Meaning |
| --- | --- |
| Database | An organised collection of data. Relational tables are one way of organising it, not the only way. |
| DBMS | Software that manages data storage, access, queries and changes. |
| RDBMS | A database management system based on the relational model, such as SQL Server, PostgreSQL or MySQL. |
| SSMS | SQL Server Management Studio: a client application used to connect to and manage SQL Server. |
| T-SQL | SQL Server's SQL dialect, including its additional statements and functions. |

SQL Server does not automatically add an identity column to every table. A table's columns and constraints come from its definition; `IDENTITY` must be specified when required.

## Database design review

The review of the training-database exercise showed that there can be more than one valid design for the same requirements. The important thing is that the ERD matches the database actually built.

A **course** can describe a type of training, while a **course instance** describes a particular delivery of it. One course might have no current instances or several instances. Each instance refers back to its course.

### Junction tables

A junction table represents a many-to-many relationship using two one-to-many relationships. For example:

```text
Trainers(TrainerID, TrainerName)
CourseInstances(CourseInstanceID, CourseID, StartDate)
CourseInstanceTrainers(CourseInstanceID, TrainerID)
```

A trainer can teach multiple instances, and an instance can have multiple trainers. Each row in `CourseInstanceTrainers` records one assignment. The two IDs can form a composite primary key, with each also being a foreign key.

The junction table does contain data: the relationship itself. It can also contain attributes of that relationship, such as an assigned role or the date the assignment began.

Other points from the review:

- Crow's-foot symbols show cardinality; a circle indicates that zero related rows are allowed.
- `UQ` on a diagram denotes a unique constraint, such as preventing duplicate email addresses.
- Rules such as an end date being after a start date need to be reflected in constraints where appropriate.
- A diagram looking tidy is not enough to prove its normal form. Check the keys and dependencies.

## IN, BETWEEN and LIKE

These answer different kinds of filtering questions.

### IN: match one of several values

```sql
SELECT CustomerID, CompanyName, Region
FROM dbo.Customers
WHERE Region IN (N'WA', N'SP');
```

`IN` checks membership in a set of values. For this example it expresses the same condition as `Region = N'WA' OR Region = N'SP'`.

### BETWEEN: include both endpoints

```sql
SELECT TerritoryID, TerritoryDescription
FROM dbo.Territories
WHERE TerritoryID BETWEEN N'06800' AND N'09999';
```

`BETWEEN` includes the lower and upper bounds. I shared the documentation during the discussion so we could check that behaviour.

Northwind territory IDs are text identifiers. Quoting them preserves leading zeroes and compares text values. This example uses consistently formatted five-digit IDs; text ordering should not be assumed to behave like numeric ordering for arbitrary strings of different lengths.

### LIKE: match a pattern

```sql
SELECT ProductID, ProductName
FROM dbo.Products
WHERE ProductName LIKE N'Ch%';
```

| Pattern | Meaning |
| --- | --- |
| `N'Dan%'` | Starts with `Dan`, followed by zero or more characters. |
| `N'M_D%'` | `M`, one character, `D`, then any remaining characters. |
| `N'M[N-Z]%'` | `M`, one character from the specified range, then any remaining characters. |
| `N'[^A]%'` | Starts with a character outside the specified set. |

Square brackets match **one character** from a set or range. A pattern such as `[06800-09999]` is not a way to test whether a whole identifier lies between two numbers. Use a comparison such as `BETWEEN` for that question.

Case sensitivity and the interpretation of character ranges depend on the collation. `%` and `_` are wildcard symbols in a `LIKE` pattern; their meaning depends on that context. See [Microsoft's LIKE documentation](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/like-transact-sql).

Built-in syntax makes the intention easier to read. That does not mean `IN` is automatically faster than equivalent `OR` conditions, or `BETWEEN` faster than equivalent comparisons: the optimiser may produce the same plan.

## Aggregates and HAVING

To compare the average reorder level across product categories:

```sql
SELECT
    CategoryID,
    AVG(CAST(ReorderLevel AS DECIMAL(10, 2))) AS AverageReorderLevel
FROM dbo.Products
GROUP BY CategoryID
ORDER BY AverageReorderLevel DESC, CategoryID;
```

Casting before `AVG` preserves a fractional average. SQL Server returns an integer type for `AVG` over `SMALLINT` or `INT`, which can lose the fractional part. `AVG` also ignores null values rather than treating them as zero. See [Microsoft's AVG return types](https://learn.microsoft.com/en-us/sql/t-sql/functions/avg-transact-sql).

To keep suppliers whose products have average units on order above five:

```sql
SELECT
    SupplierID,
    SUM(UnitsOnOrder) AS TotalUnitsOnOrder,
    AVG(CAST(UnitsOnOrder AS DECIMAL(10, 2))) AS AverageUnitsOnOrder
FROM dbo.Products
GROUP BY SupplierID
HAVING AVG(CAST(UnitsOnOrder AS DECIMAL(10, 2))) > 5
ORDER BY AverageUnitsOnOrder DESC;
```

`WHERE` filters individual rows before grouping. `HAVING` filters the grouped results. The relevant logical order is:

```text
FROM / JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY
```

The alias `AverageUnitsOnOrder` is introduced by `SELECT`, so it cannot be used in `HAVING` at the same query level. Repeat the aggregate expression there. `ORDER BY` can use the alias.

This is the logical order for understanding the query; the physical execution plan can organise the work differently.

## Subqueries

A subquery is a query nested inside another statement. We looked at examples in `WHERE`, `SELECT` and `FROM`. Its result might be a single value, a set of values or a table-shaped result, depending on where it is used.

### WHERE: order lines for discontinued products

```sql
SELECT OrderID, ProductID, UnitPrice, Quantity, Discount
FROM dbo.[Order Details]
WHERE ProductID IN (
    SELECT ProductID
    FROM dbo.Products
    WHERE Discontinued = 1
);
```

The inner query identifies discontinued products. The outer query returns order lines containing those products. This gives historical order lines for products currently marked discontinued; it does not show whether they were discontinued at the time of each order.

### Customers with no orders

The lesson used `NOT IN` to exclude customer IDs found in `Orders`. Null values need care, so this version excludes them from the subquery:

```sql
SELECT c.CustomerID, c.CompanyName
FROM dbo.Customers AS c
WHERE c.CustomerID NOT IN (
    SELECT o.CustomerID
    FROM dbo.Orders AS o
    WHERE o.CustomerID IS NOT NULL
);
```

If the inner result contains a null, a nonmatching `NOT IN` comparison can become unknown instead of true, unexpectedly removing rows. See [Microsoft's IN and NOT IN guidance](https://learn.microsoft.com/en-us/sql/t-sql/language-elements/in-transact-sql).

An alternative expresses the absence of a matching order directly:

```sql
SELECT c.CustomerID, c.CompanyName
FROM dbo.Customers AS c
WHERE NOT EXISTS (
    SELECT 1
    FROM dbo.Orders AS o
    WHERE o.CustomerID = c.CustomerID
);
```

This is a **correlated subquery** because it refers to `c.CustomerID` from the outer query. `EXISTS` asks whether any matching row exists; `SELECT 1` does not mean “return only the first row”. Changing `NOT EXISTS` to `EXISTS` finds customers who have ordered.

The same no-orders question can also be answered with a left join followed by a null check on the order key.

### SELECT: add a single value

```sql
SELECT
    od.OrderID,
    od.ProductID,
    od.UnitPrice,
    (SELECT MAX(UnitPrice) FROM dbo.[Order Details]) AS HighestUnitPrice
FROM dbo.[Order Details] AS od;
```

The scalar subquery returns one value: the highest unit price across all order details. It is repeated beside every outer row because the subquery is not tied to a particular order or product.

A scalar subquery must return one column and at most one row. Returning several rows causes an error; returning no rows gives null. See [Microsoft's subquery guide](https://learn.microsoft.com/en-us/sql/relational-databases/performance/subqueries).

### FROM: join to a derived table

```sql
SELECT
    od.OrderID,
    od.ProductID,
    od.UnitPrice,
    od.Quantity,
    totals.ProductTotalBeforeDiscount
FROM dbo.[Order Details] AS od
INNER JOIN (
    SELECT
        ProductID,
        SUM(UnitPrice * Quantity) AS ProductTotalBeforeDiscount
    FROM dbo.[Order Details]
    GROUP BY ProductID
) AS totals
    ON od.ProductID = totals.ProductID;
```

The inner query produces one total per product. Giving that derived table an alias lets it participate in the join like another table source.

The final result still has one row per order line, with the product's overall total repeated alongside it. Do not sum that repeated total again as though each occurrence were a separate sale. This example deliberately calculates the amount before discount.

A derived table belongs to the statement using it; it does not create a permanent table. It can help to run an independent inner query on its own while understanding it, but SQL Server is not required to physically run every subquery first or materialise its result.

## Avoiding accidental Cartesian products

A Cartesian product pairs every row from one input with every row from another. If the inputs contain 100 and 1,000 rows, the result contains 100,000 pairs.

The demonstration used an older comma-separated join style and left out the relationship to `[Order Details]`. That caused each customer-order row to be paired with unrelated order lines. Adding `DISTINCT` at the end can hide repeated output without fixing the missing relationship.

A comma-separated list of tables is not an outer join. Without a linking condition it produces a cross join; appropriate equality conditions in `WHERE` can make it equivalent to an inner join.

Explicit joins make the relationships easier to review:

```sql
SELECT c.CustomerID, c.CompanyName, o.OrderID, od.ProductID
FROM dbo.Customers AS c
INNER JOIN dbo.Orders AS o
    ON c.CustomerID = o.CustomerID
INNER JOIN dbo.[Order Details] AS od
    ON o.OrderID = od.OrderID;
```

If the question is only whether a customer has ordered, the `EXISTS` approach is a direct way to express it. There is no need to join every order line just to answer that question.

Cross joins can be intentional, such as generating all combinations of two small sets. The problem is producing those combinations accidentally. Their row count is the product of the input counts, not automatically an exponential increase whenever one row is added.

## Views and SELECT INTO

These both reuse query results, but they store different things.

### A view stores a query definition

```sql
USE Northwind;
GO

CREATE VIEW dbo.ProductCategorySummary
AS
SELECT
    c.CategoryID,
    c.CategoryName,
    COUNT(p.ProductID) AS ProductCount
FROM dbo.Categories AS c
INNER JOIN dbo.Products AS p
    ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryID, c.CategoryName;
GO

SELECT CategoryName, ProductCount
FROM dbo.ProductCategorySummary
ORDER BY ProductCount DESC, CategoryName;
```

The first statement creates the view. The later `SELECT` queries it. This inner join version only includes categories with matching products.

An ordinary view stores the definition, not a saved copy of the result rows. Querying it uses the underlying data visible to that query. A view is a persistent database object, not a temporary table. Indexed views are a separate case with additional rules.

Views can simplify frequently used joins or aggregates and give users a consistent interface. They can also be joined to other tables. Use a descriptive name and follow the team's naming convention; prefixes such as `vw_` are optional.

`CREATE VIEW` needs to start its batch. To change an existing definition, use `ALTER VIEW`. Put `ORDER BY` in the query consuming the view when a particular output order matters. See [Microsoft's CREATE VIEW documentation](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-view-transact-sql).

### SELECT INTO creates a table containing data

```sql
SELECT CustomerID, CompanyName, ContactName, Phone
INTO dbo.FrenchCustomers
FROM dbo.Customers
WHERE Country = N'France';
```

This creates a new table and fills it with the selected rows. Including `CustomerID` makes it easier to identify the copied records later.

The table is a snapshot: changes to `Customers` do not automatically update `FrenchCustomers`. The destination must not already exist. To add rows to an existing table, use `INSERT INTO ... SELECT` instead.

The selected expressions determine the new columns, but indexes, primary and foreign key constraints, and triggers are not copied across. Copying `CustomerID` does not automatically make it a primary key in the new table. See [Microsoft's SELECT INTO documentation](https://learn.microsoft.com/en-us/sql/t-sql/queries/select-into-clause-transact-sql).

## Query performance and indexes

An index is an extra access structure that can help SQL Server locate rows. The book-index analogy is useful: find a term in the index, then use its reference to reach the relevant content.

Creating an index normally does not change how the query is written or which rows logically match. It gives the optimiser another way to retrieve them. SQL Server can still query columns that have no index, and an index does not guarantee any particular result order.

### Filter directly on the indexed value

These date filters aim to find orders from 1997:

```sql
-- Applies a function to the column.
SELECT OrderID, OrderDate
FROM dbo.Orders
WHERE YEAR(OrderDate) = 1997;

-- Expresses the requirement as a date range.
SELECT OrderID, OrderDate
FROM dbo.Orders
WHERE OrderDate >= '19970101'
  AND OrderDate < '19980101';
```

The range form gives an ordinary index on `OrderDate` a better opportunity to locate the relevant entries directly. The exclusive upper bound includes all of 31 December even when the column contains times.

This kind of usable search condition is called **SARGable**. Applying a function to a column can prevent a direct seek on its ordinary index. Another example from the lesson was expressing a name prefix with `CompanyName LIKE N'A%'` instead of `LEFT(CompanyName, 1) = N'A'`.

The issue is the expression being searched, not simply which side of the equals sign the column appears on. A date column is not automatically indexed, and writing a range does not create an index. The chosen plan still depends on the available indexes, statistics and amount of matching data. See [Microsoft's index design guide](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide).

### Creating indexes

Illustrative definitions from the lesson's customer and order examples:

```sql
CREATE INDEX IX_Customers_City
ON dbo.Customers (City);

CREATE INDEX IX_Orders_CustomerID_OrderDate
ON dbo.Orders (CustomerID, OrderDate);
```

Check existing indexes first; Northwind may already have an index serving the same purpose. Adding another equivalent index creates maintenance work without necessarily helping queries.

The second example is a **composite index**. Its key order matters: customer ID comes first, followed by order date. It can suit queries that select one customer and then a date range; it is not interchangeable with an index starting with `OrderDate`.

A regular index allows duplicate values, which makes sense for cities shared by many customers. A `UNIQUE` index additionally enforces uniqueness. Only apply that rule to product names, for example, if the business actually requires every name to be unique and the existing data satisfies it.

SQL Server creates an index to enforce a primary key. Foreign key columns and ordinary date columns do not automatically receive their own indexes just because of their role or data type.

Indexes take storage and need maintenance when relevant data changes. Choose them around the workload rather than indexing every column.

To remove the illustrative city index:

```sql
DROP INDEX IX_Customers_City ON dbo.Customers;
```

This removes the index, not the city values or the customer table.

### Looking at an execution plan

- A **scan** reads through a table or index to find qualifying data.
- A **seek** uses an index's key structure to locate matching values or ranges.

A seek can avoid reading much of a large input, but a scan is not automatically a bad plan. For a small table or a query needing most rows, scanning can be appropriate.

The SQL Server example used `SHOWPLAN_ALL`:

```sql
SET SHOWPLAN_ALL ON;
GO

SELECT CustomerID, CompanyName, City
FROM dbo.Customers
WHERE City = N'London';
GO

SET SHOWPLAN_ALL OFF;
GO
```

This returns an **estimated plan** without executing the query. Estimated row counts are not measurements of rows actually read. Each `SET SHOWPLAN_ALL` statement needs its own batch, and it must be turned off before running statements normally. See [Microsoft's SHOWPLAN_ALL documentation](https://learn.microsoft.com/en-us/sql/t-sql/statements/set-showplan-all-transact-sql).

An actual execution plan and read/time statistics are more useful when measuring what happened. Repeated runs can be faster because data pages or execution plans are cached; that does not mean SQL Server generally saves and replays the entire query result. Opening another query tab is not a reliable way to clear those caches.

The Northwind examples are small, so timing differences alone are weak evidence. Check correctness first, then compare the work the plans perform. A subquery is not automatically faster than a join, and adding an index does not guarantee the optimiser will use it.

## Updating and deleting records

`UPDATE` changes column values on existing rows. `DELETE` removes rows. Both need the intended filter; without `WHERE`, they apply to all rows.

This practice example uses the copied table and rolls back the change:

```sql
BEGIN TRANSACTION;

UPDATE dbo.FrenchCustomers
SET Phone = N'000-000-0000'
WHERE CustomerID = N'BONAP';

SELECT CustomerID, CompanyName, Phone
FROM dbo.FrenchCustomers
WHERE CustomerID = N'BONAP';

ROLLBACK TRANSACTION;
```

The same filter can identify a row for deletion:

```sql
BEGIN TRANSACTION;

DELETE FROM dbo.FrenchCustomers
WHERE CustomerID = N'BONAP';

ROLLBACK TRANSACTION;
```

Use a key when identifying one particular record and check how many rows match. The copied table has no inherited key constraint, so keeping an ID column alone does not enforce uniqueness.

In the original Northwind tables, deleting a product referenced by order details can fail because of a foreign key constraint. That protects the relationship. Cascading deletion is a rule configured on a foreign key, not a general extra keyword to append to any `DELETE`. It should reflect the intended data lifecycle.

An identity column also cannot be changed with an ordinary `UPDATE`, as the product-ID demonstration showed. Changing a product's name is a different operation from changing its identifier.

### Apostrophes and accented characters

In a T-SQL string literal, represent an apostrophe by doubling it:

```sql
SELECT CustomerID, CompanyName
FROM dbo.Customers
WHERE CompanyName = N'Bon app''';
```

The final pair within the string represents the apostrophe in `Bon app'`; the last quote closes the literal. A backslash is not the usual escape for this in T-SQL.

Unicode text types and `N'...'` literals support accented characters. Whether a comparison treats accented and unaccented letters as equal is controlled by the collation's accent sensitivity. Character storage and comparison rules are related but different concerns.

## Introduction to data pipelines

A data engineer builds and maintains pipelines that move data from its sources into a form and location where it can be used.

| Stage | What it does | Example |
| --- | --- | --- |
| Extract | Reads data from source systems or files | Bring in customer records from a database, CSV file or API. |
| Transform | Changes the data into the required structure and quality | Standardise formats, validate values and combine related records. |
| Load | Writes the data into its destination | Insert prepared records into database tables. |

Extraction normally means taking data from an existing source into the pipeline, not necessarily conducting the original survey or collecting every website event ourselves.

- **ETL:** extract, transform, then load into the target.
- **ELT:** extract and load first, then transform using the destination platform.
- **ELTL:** a sequence that loads to an intermediate location, transforms, then loads the prepared result elsewhere.

In SQL, `INSERT INTO` is a simple example of loading records. `CREATE TABLE` defines the structure but does not by itself populate it. A real loading process may also update existing records or use bulk operations.

## OLTP and OLAP

| | OLTP — Online Transaction Processing | OLAP — Online Analytical Processing |
| --- | --- | --- |
| Main purpose | Support everyday business operations | Support analysis and business intelligence |
| Typical work | Many short transactions and targeted lookups | Larger queries, comparisons and aggregations |
| Example | Record an order and update stock | Compare product sales across regions and quarters |
| Data design | Often normalised to protect consistency | Often arranged around measures and dimensions for analysis |

OLTP includes reads as well as writes. Looking up an order's status does not turn the system into OLAP. The distinction is the purpose and workload being supported. See [Microsoft's OLTP overview](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/online-transaction-processing).

OLAP focuses on analytical questions across larger sets of data, often including history. A cube is one way to organise measures such as sales revenue against dimensions such as product, region and time. It can support comparing the same measure across different categories and levels of detail. See [Microsoft's OLAP overview](https://learn.microsoft.com/en-us/azure/architecture/data-guide/relational-data/online-analytical-processing).

We also revisited **ACID**: atomicity, consistency, isolation and durability. These concern reliable transactions. A savepoint is not a backup, and full serial behaviour depends on the isolation level; the fuller notes are in [Day 2](day-02-database-design-and-stored-procedures.md#transactions-and-acid).

## Data warehouses and data marts

A **data warehouse** is a data store designed for analysis and reporting. It can integrate data from several operational systems and maintain consistent definitions and historical information for business questions.

For example, customer, sales and product data could be brought together to investigate which products perform well in different regions over time. An operational system still handles individual orders; the analytical store supports broader comparisons.

A warehouse is a kind of database system, so “database” does not always mean “transactional database”. The useful comparison is between the operational and analytical roles.

A **data mart** focuses on a subject or business area, such as sales or finance. It may be a subset of a larger warehouse, although marts can also be built independently. The purpose is to provide data suited to that area's reporting needs.

## Connecting the technical work to business questions

The final discussion was about combining data skills with communication and business understanding. A dashboard needs more than correct charts: someone should be able to understand the finding and why it matters.

For a sales analysis, useful questions include which products are performing well, whether that varies by season or region, and what evidence would support a change to stock or promotion decisions. Explain the scope and limitations before recommending an action.

The practice work set alongside the lesson included further Northwind queries, the database creation and ERD exercise, and the separate AI-agent task.
