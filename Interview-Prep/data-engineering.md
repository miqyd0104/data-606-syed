# Data Engineering

Interview questions and answers for our Data Engineering course.

## Data Concepts

### 1. What is SIMPLE for critical thinking?

For **critical thinking itself**, you could say:

“It’s about checking information rather than accepting it straight away. I’d ask where it came from, what evidence supports it and whether there’s another explanation. For example, if sales went up after a promotion, I’d check whether it was also a busy shopping period before saying the promotion caused the increase.”

### 2. What should you look out for when cleaning data?

“I’d look for things like missing values, duplicates, inconsistent formats and values that don’t make sense. For example, the same customer might appear twice, or dates might be written differently. I’d check what the data is supposed to represent before changing anything, because something unusual isn’t necessarily an error.”

### 3. What are the three principles of data visualisation?

*These are general principles; your course’s exact three labels still need checking.*

“I’d say accuracy, clarity and relevance. The chart needs to represent the figures honestly, be easy to understand and answer the question we’re looking at. For example, if I’m showing monthly sales, I’d use a clear title, labelled axes and a suitable scale so someone can understand the trend quickly.”

### 4. What data is a line chart suitable for?

“I’d use a line chart to show how something changes over time, like sales each month. It makes it easier to spot whether sales are growing, falling or following a seasonal pattern. It works because the points have a meaningful order, rather than just being unrelated categories.”

### 5. What data is a bar chart suitable for?

“A bar chart is useful for comparing categories. So, with a clothing business, I could compare sales of dresses, jackets and shoes. You can quickly see which sold the most by comparing the bars. I’d normally start the value axis at zero so I don’t exaggerate the differences.”

### 6. What data is a stacked bar chart suitable for?

“I’d use a stacked bar chart when I want to show a total and what makes it up. For example, each bar could show a month’s sales, with different sections for dresses, jackets and shoes. That shows the overall sales and how each category contributed. For percentage shares, I’d use a 100% stacked bar.”

### 7. What data is a histogram suitable for?

“A histogram shows how numerical values are spread out by putting them into ranges. For example, I could group delivery times to see how many orders took one to two days, three to four days, and so on. That helps me see what’s typical and whether some deliveries are taking much longer.”

### 8. What data is a scatter plot suitable for?

“A scatter plot is useful for looking at the relationship between two numerical values. For example, I could compare advertising spend with sales, with each point representing a week. It might show that higher spending tends to go with higher sales, but I’d need more evidence before saying one caused the other.”

### 9. What data is a pie chart suitable for?

“A pie chart shows how a total is divided into different parts. For example, I could show what percentage of orders were paid by card, digital wallet or bank transfer. It’s best with a small number of categories. If the percentages are very similar, I’d use a bar chart because they’re easier to compare.”

### 10. What data is a treemap suitable for?

“A treemap is useful for showing how different groups contribute to a total, especially when there are quite a few groups. Bigger rectangles represent bigger values. For example, it could show sales by department, with each department broken down into product categories. It’s good for seeing which groups dominate, rather than comparing exact figures.”

### 11. What data is a waffle plot suitable for?

“A waffle plot makes proportions easy to see using a grid of squares. If there are 100 squares, each one can represent 1%. So, if 80% of deliveries arrived on time, I could colour 80 squares. It’s a straightforward way to communicate a percentage without someone having to interpret lots of figures.”

### 12. What data is a map suitable for?

“I’d use a map when location is part of the question. For example, I could show where customers are ordering from to understand demand. I’d be careful with the comparison, though—a region might have more orders simply because more people live there, so sometimes a rate is more useful than a total.”

### 13. What are the six types of data errors?

*These are six common categories, rather than confirmed labels from your course.*

“I’d check for missing data, duplicates, incorrect values, inconsistent values, invalid values and records that don’t link properly. For example, an order could appear twice or refer to a customer ID that doesn’t exist. These problems matter because they can lead to incorrect totals or information being linked to the wrong person.”

### 14. What are the different data types?

“For analysis, there’s categorical data and numerical data. Categorical data describes groups, like payment methods. Some categories have an order, like low, medium and high. Numerical data includes counts, like the number of orders, and measurements, like weight.

In Python or a database, we then choose suitable types such as strings, integers, decimals and dates so we can work with those values correctly.”

### 15. How is data stored?

“It depends on what the data is and how we need to use it. We might keep a sales export in a CSV, customer records in a database and product photos as image files. Underneath, it’s all represented digitally as bits. The storage choice affects how easily we can find, update and process it.”

### 16. What steps are taken when analysing data?

“I’d start by getting clear on the question. Then I’d collect the relevant data, check it and clean any issues before exploring it. After analysing it, I’d check whether the results make sense and explain what I found.

For example, if I’m looking at profit, I need expenses as well as sales. Otherwise, I’m not really answering the question.”

### 17. What is data cleaning, and why is it used?

“Data cleaning is checking the data for problems and dealing with them appropriately. That might mean investigating duplicate orders, fixing inconsistent dates or handling missing values. We do it because those issues can affect the results. I’d keep the original data and record my changes so I can explain what I’ve done.”

### 18. Under what conditions should you use a pie chart?

“I’d use one when a few categories make up a complete total, like the share of orders by payment method. The categories shouldn’t overlap, and their percentages should add up to 100%. If there are lots of categories or the slices look almost identical, a bar chart would be clearer.”

### 19. Why is it important for data to be unbiased?

“Because biased data can give us the wrong picture and lead to poor or unfair decisions. For example, if I only ask customers who left positive reviews about their experience, I’m missing the unhappy customers. I’d want the data to reflect the wider group, rather than just the people who are easiest to reach.”

### 20. How do we check for bias?

“I’d look at how the data was collected and who might be missing. For example, an online survey might miss customers who only shop in person. I’d compare the people represented with the wider group we’re trying to understand. We can’t always rule out every bias, but we can identify likely issues and explain the limitations.”

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
