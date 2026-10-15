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


