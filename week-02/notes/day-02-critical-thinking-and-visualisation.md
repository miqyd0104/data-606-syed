# Day 2 — Critical thinking and visualisation

29 September 2026

[← Week 2](../README.md) · [Day 1](day-01-git-and-data-concepts.md)

Today focused on questioning data and presenting it clearly. We worked through examples of misleading conclusions and charts, then looked at visualisation design before starting the Excel dashboard task.

## Critical thinking as a data analyst

People may make important business decisions based on an analyst's work. That means checking whether the data supports the conclusion, as well as making the calculations correctly.

A chart can contain accurate numbers and still give a misleading impression. The choice of data, time period, comparison, scale and wording all affect what the audience takes away.

The aim is to ask useful questions:

- Where did the data come from, and how was it collected?
- Does it represent the people or situation we are interested in?
- What information is missing?
- What assumptions are being made?
- Could there be another explanation?
- What can we confidently conclude from the evidence available?

### The new-recipe scenario

We were given a scenario where a new recipe performed better than the existing product and a competitor in taste tests involving over 200,000 people. The question was whether the company should replace its existing product.

The large number of participants did not answer every business question. We still needed to know:

- Whether the participants represented the company's actual customers.
- How the test was conducted and what “almost always wins” meant numerically.
- Whether the preference was strong enough to affect buying decisions.
- How much production would cost and whether the selling price would change.
- How existing customers would react to losing a familiar product.
- Whether both versions could be offered or tested before making a full change.

The example was linked to New Coke. The main lesson was that **taste preference is only one part of a purchasing decision**. Evidence about one measure does not automatically justify a wider business decision.

### Reliability of reports

Another scenario explored the risk of acting on reports without checking their reliability. Before changing a system, question whether the reported problem is accurate, whether sources agree and whether the information could be biased or deliberately misleading.

For a business problem, this means investigating the cause before recommending a major change. The issue might involve the system, its inputs, the way it is being used or the way results are being measured.

## SIMPLE

We used **SIMPLE** as a reminder of the areas to check when analysing data or reviewing someone else's findings. The “L” was used for alternative explanations in the session.

| Area | Questions to ask |
| --- | --- |
| Source | Who collected the data? How reliable is it? Could the collection method or the source's interests influence the result? |
| Irrelevant data | Does this information relate to the question, time period, population and location we care about? |
| Missing data | What information would we need to make a stronger conclusion? Has anything important been left out? |
| Presentation | Do the chart type, axes, units, scale, colours and wording represent the data fairly? |
| Alternative explanations | What else could explain the pattern? Are we only looking for an expected result? |
| Evidence | Which claims are supported, and which are still possibilities that need investigating? |

### Source and relevance

A large dataset can still be biased. For example, a survey may include many people while leaving out the group whose behaviour the business actually needs to understand.

Check how the information was gathered. A quick taste test and a week of using a product measure different experiences. Similarly, results from one region or time period may not apply to another.

Not every column needs to be analysed. Start with the question and decide which fields help answer it, keeping the original data available.

### Missing information

Missing information means more than blank cells. An analysis may have complete rows but still lack a comparison group, the starting position or an important business cost.

A useful question is: **What extra information would make this conclusion more convincing?**

For example, knowing that sales increased is helpful, but assessing a campaign may also require the previous trend, campaign costs and what happened in places where it did not run.

### Totals and percentages

A higher count does not necessarily mean something has become more common relative to the population.

The class example compared 3,000 people wearing bowler hats in one period with 6,000 in another. The count doubled, but we would also need the size of the population being measured before claiming the hats had become more popular.

Choose counts, percentages or rates according to the question. Make the denominator clear when using a percentage or rate.

## Reading charts critically

### Leading survey questions

One political polling example asked respondents to imagine that only two parties were competitive. Its results were then presented in a way that could be read as general voting intention.

The problem was the gap between the question asked and the conclusion implied. A person's choice in a restricted hypothetical situation is not necessarily the same as their choice in an actual election.

Read the question, sample description and source as well as the bars. The chart alone may leave out the most important context.

### Comparing different time periods

Another chart compared several years of university costs with annual earnings. That comparison could show a cost burden, but would not by itself establish whether a degree was worthwhile over a lifetime.

The discussion raised questions about longer-term earnings, living costs, the comparison group and how the figures were collected.

An incomplete comparison can still contain useful information. The task is to explain what it shows and where its conclusion goes beyond the evidence.

### Axes, units and headlines

A chart comparing unemployment and uninsured people raised several issues:

- One measure was a percentage and the other a count.
- The two axes could make the lines look more closely related than they were.
- A short time window gave limited context for the apparent trend.
- The source was unclear.
- A headline about people becoming uninsured did not explain the period used or account for people gaining insurance.

Dual axes are not automatically wrong, but their scales need careful reading. Two lines moving together do not establish a causal relationship.

Also distinguish **flows** from **net change**. The number leaving a group is not the same as the change in its total size if other people are joining it.

## Alternative explanations

### Numeracy intervention

The scenario described 30 children receiving three hours of extra maths teaching every Saturday for six months. Their average score increased by 50%, leading to the claim that the new teaching technique was effective.

Possible explanations included:

- The additional time spent practising maths.
- Extra attention or motivation.
- Progress through the normal school curriculum.
- A small number of pupils improving greatly and lifting the average.

To investigate the particular technique, we would want individual before-and-after scores and a suitable comparison group. Comparing with children receiving a similar amount of additional teaching through another method would help separate the effect of the technique from the effect of extra teaching time.

### Farming intervention

A project supported farmers using fertiliser, and they later had higher income and wellbeing than farmers in neighbouring regions. The proposed conclusion was that the project would work in another region too.

Other factors could include climate, soil, crops, farm size, resources, markets and selling prices.

I raised the question of **where the farmers were starting from**: they may already have had more money or a better starting position than the neighbouring farmers.

That baseline matters. Higher income after a project does not tell us how much income changed or whether the project caused the difference. We would need information from before the intervention and more comparable groups to investigate it properly.

Applying a result elsewhere also requires checking whether the conditions are similar enough for the finding to transfer.

### Findings, explanations and opinions

Keep the language matched to the strength of the evidence:

- **Finding:** “This category has the highest recorded sales in the dataset.”
- **Possible explanation:** “Seasonal demand may contribute to the difference.”
- **Further investigation:** “Compare the same period across several years and check promotions before attributing the increase to seasonality.”

The expectation is to go beyond describing the tallest bar. Suggest useful explanations and investigate them where possible, while making clear what remains uncertain.

## Principles of a good visualisation

We covered Andy Kirk's three principles: **trustworthy, accessible and elegant**.

| Principle | What to consider |
| --- | --- |
| Trustworthy | Accurate representation, appropriate scales, clear sourcing and wording that avoids sensationalism. |
| Accessible | The intended audience can see, understand and interpret the information. |
| Elegant | The design communicates clearly without unnecessary distraction. |

A professional appearance can encourage trust, but it does not prove the analysis is correct. Both the underlying work and the presentation need care.

### Designing for the audience

The audience does not have all the context gained from working with the data. Use clear titles, readable labels and enough explanation for someone else to understand the chart.

Consider colour blindness and avoid relying only on a red/green distinction. Labels and other visual differences should help communicate the meaning too.

Some visual flair can make the subject more engaging. Examples included chocolate-themed bars and a chart presenting Vienna as an apartment. The design still needs to help the audience read the data.

## Tables and headline figures

A dashboard can include useful tables and KPI figures as well as charts. A carefully aggregated table may answer a question more directly than another graph.

The table example showed how heavy borders, excessive bold text, strong colours and unnecessary precision can make information harder to read.

Useful formatting habits:

- Left-align text and right-align numbers.
- Keep units and decimal precision consistent.
- Use clear spacing and restrained borders.
- Use bold and colour selectively, so emphasis has meaning.
- Include a title and enough context to explain the values.
- Round displayed figures where appropriate for the audience, without changing the underlying data unnecessarily.

A highlight table can use colour to show patterns across rows and columns. Keep the scale understandable, and retain exact values where the audience needs them.

A **KPI**, such as total sales for a stated period, can also be shown as a headline figure. Make clear what it measures and what filters or period apply.

## Choosing and improving charts

Choose the chart around the relationship being shown: comparison, change over time, ranking, composition, deviation or distribution.

### Line charts

Line charts are useful for changes over time. Too many thick, overlapping lines make it difficult to follow individual series.

- Keep the number of series manageable; around four was suggested as a useful starting limit.
- Use thinner lines and deliberate highlighting.
- Make sampling intervals clear, especially if observations are irregular.
- Consider separate panels for different categories rather than forcing everything into one chart.

One example repeated the same chart across several panels, highlighting a different series in each while fading the others. This kept the context while making the selected series easier to follow.

A **slope chart** is another option when the question is about change between two time points. It can show which categories increased or decreased without displaying every intermediate value.

### Bar charts

Bar charts compare magnitudes across categories. Their design should make the comparison easy.

- Start the value axis at zero so bar lengths represent the quantities fairly.
- Sort categories in a useful order, such as by value for a ranking.
- Use horizontal bars when category names are long.
- Avoid vertical text and unnecessary colours.
- Keep gridlines light and limited to what helps the reader.
- Use sensible bar widths and spacing.

If the question is about the difference from a benchmark, a **deviation chart** can show values above or below that benchmark. Label the reference clearly instead of truncating a normal bar chart to exaggerate small differences.

### Grouped and stacked bars

**Grouped bars** place related series alongside each other so the audience can compare them within and across categories.

**Stacked bars** show how components contribute to a total. A **100% stacked bar chart** shows proportions, with every bar representing the whole.

Middle segments can be harder to compare because they do not share a common starting point. Consider whether the audience needs to compare totals, proportions or one particular component.

### Part-to-whole charts

The training guidance was to avoid pie charts and 3D charts for the dashboard. A 3D effect can distort the apparent sizes and make comparisons harder.

Alternatives discussed included:

- **Doughnut chart:** keep the number of segments manageable and highlight a clear takeaway, such as the share contributed by the largest categories.
- **Treemap:** use rectangles to show parts of a whole.
- **Waffle chart:** use a grid of equal cells to represent proportions.

A doughnut still becomes difficult to read with many similar segments. Choose the form that makes the intended comparison clearest.

## Excel dashboard task

The main deliverable is a professional Excel dashboard based on the chosen dataset.

The requirements discussed were:

1. Explore the data and deal with relevant cleaning issues, including missing values and unnecessary fields.
2. Create **five original visualisations in Excel**, brought together as a dashboard.
3. Include at least one element beyond a basic bar or line chart. Examples included a treemap or an interactive PivotChart with slicers.
4. Present useful findings and consider possible explanations behind them.
5. Make the dashboard understandable on its own and suitable to present to someone else.

An example of interactivity was selecting a country and having the chart update to show that country's data. Any extra feature should help answer a question rather than just make the dashboard more complicated.

The working target was to finish by the end of Wednesday, ready for Thursday if asked to present. The dashboard was the immediate focus; a separate presentation was not confirmed.

Excel learning resources were provided for independent work, including Microsoft training, formulas and functions, and a dashboard walkthrough. A walkthrough could help build a first version, but it needed to be adapted to the chosen data and extended to meet the brief.

The afternoon was set aside to start the practical work, with a later check-in. The first version did not need to be perfect: get the analysis working, then improve the layout, readability and detail.
