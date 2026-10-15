- [Data Storage](Data-Storage.md)

## Data Storage & Design

### 21. What is ETL?

“ETL stands for Extract, Transform, Load. We get the data, make the changes we need, then save it to the destination. Our IMDb task followed that process: we read the file, filtered the movies and selected the columns, then wrote the results to another CSV. It makes the processing repeatable instead of doing it manually each time.”

### 22. What is ELT?

“ELT stands for Extract, Load, Transform. This time, we load the data into the destination before making the changes there. For example, we could load sales records into a warehouse and then use SQL to clean them and create reporting tables. That works well when the destination can handle the processing.”

### 23. What are the main differences between ETL and ELT?

“The main difference is when the transformation happens. With ETL, we change the data before loading it. With ELT, we load it first and change it in the destination.

For example, ETL might reject invalid records before they reach a reporting database. ELT could keep the source data and build different cleaned datasets from it. The choice depends on the system and what we need the data for.”

### 24. What is a database?

“A database is an organised collection of data that we can search, update and manage. For example, an online shop needs to store its customers, products and orders. A database lets it find a particular order, update its status and connect it to the right customer, while applying rules to keep the records consistent.”

### 25. Explain the two main database types.

“The broad types are relational and non-relational. A relational database uses tables with relationships between them, like customers linked to orders through a customer ID.

Non-relational databases use other structures, such as documents or key-value pairs. For example, a document database could hold products with different sets of attributes. I’d choose based on how the data needs to be stored and accessed.”

### 26. What is a data warehouse?

“A data warehouse brings together data from different sources so we can analyse it, including how things have changed over time. For example, a retailer could combine online and shop sales to compare performance across several years. It gives people a consistent dataset for reporting instead of asking them to piece together separate systems themselves.”

### 27. What is a data lake?

“A data lake can hold large amounts of data in different formats, often close to how it originally arrived. That could include CSV files, JSON, logs and images. It gives us flexibility to process the data for different uses later. But we still need to organise and document it, otherwise people won’t know what’s there or whether they can trust it.”

### 28. How is a database structured?

“In a relational database, we organise data into tables. Each row is a record, and each column holds a particular piece of information. So, an orders table might have an order ID, date and customer ID. The order ID identifies the record, and the customer ID links it to the customer table.”

### 29. What is normalisation?

“Normalisation is organising data into related tables so we don’t repeat the same information unnecessarily. For example, we could keep a customer’s current contact details in one customer table and link their orders to it. That way, if their phone number changes, we update it once instead of trying to fix several copies.”

### 30. What are the advantages and disadvantages of normalisation?

“The main benefit is consistency. We reduce repeated information, so there are fewer places to update and less chance of conflicting values. For example, a department name can be stored once.

The trade-off is that we may need more joins to bring the information together. That makes some queries more complicated and can add processing work, especially for reporting.”

### 31. What is a junction table?

“A junction table handles a many-to-many relationship. In our course example, a trainer can teach several course instances, and an instance can have several trainers. The junction table records each assignment using the trainer ID and course-instance ID. That lets us store every relationship properly rather than putting several IDs into one field.”

### 32. What is dimensional modelling?

“Dimensional modelling organises data to make reporting easier. We have facts, which record events and measurements, and dimensions, which describe the context. For example, a sales fact could contain quantity and revenue, with dimensions for the date, product and customer. That makes questions like ‘What did we sell by category last month?’ easier to answer.”

### 33. What is the difference between a star schema and a snowflake schema?

“In a star schema, the fact table connects directly to the dimension tables. A snowflake splits some of those dimensions into more related tables.

For example, a star’s product table might include the category name. In a snowflake, the category could be stored separately.

A star is usually simpler to query. A snowflake reduces repeated details, but you need more joins to bring everything together.”

---

[Back to Interview Prep](README.md)
