[agile-and-projects.md](https://github.com/user-attachments/files/33499348/agile-and-projects.md)
# Agile and Project Management

Interview questions and answers for our Data Engineering course.

## Project and Stakeholders

### What is the difference between BAU and a project?

BAU stands for **Business as Usual**, which is the regular work that keeps an organisation running. A project is temporary work carried out to achieve a specific outcome.

For example, checking that a daily data pipeline has run successfully would be BAU. Building a new pipeline to replace manual spreadsheet reporting would be a project.

Once that pipeline is built and handed over, running and maintaining it becomes part of BAU.

### What is a project vs a programme?

A **project delivers a specific outcome**, whereas a **programme coordinates related projects** to achieve a bigger business change.

For example, building a data warehouse could be one project. A wider programme to improve how an organisation uses data might include that warehouse, new dashboards and staff training.

Managing them together helps make sure the individual projects support the same overall goal.

### What are the typical five stages of the project lifecycle?

The five stages commonly taught are:

1. **Initiation:** Understand the problem, the expected benefits and whether the project should go ahead.
2. **Planning:** Work out the scope, tasks, budget, timescales, resources and risks.
3. **Execution:** Carry out the work and produce the deliverables.
4. **Monitoring and controlling:** Check progress and deal with changes or problems.
5. **Closure:** Get acceptance, hand over the work and record lessons learned.

For a data pipeline project, that means agreeing why it is needed, planning it, building it, checking progress and finally handing it over.

**Technical note:** These are formally project management process groups. Monitoring and controlling happens alongside other work, rather than waiting until execution finishes.

### Describe the triple constraint.

The triple constraint is **scope, time and cost**. Scope is what we need to deliver, time is how long we have, and cost is the budget available.

They affect each other. If a customer asks us to add three extra data sources to a pipeline, we may need more time, more budget or an agreement to remove something else.

It helps us explain the impact of changes and agree realistic expectations while protecting quality.

### What is the POPIT model?

POPIT stands for **People, Organisation, Processes, Information and Technology**. It helps us look at all the areas affected by a business change.

For example, introducing a reporting system means thinking about:

- **People:** Do staff have the skills and training?
- **Organisation:** Who owns the system and makes decisions?
- **Processes:** How will reports be requested and produced?
- **Information:** Is the data accurate and useful?
- **Technology:** What tools and infrastructure are needed?

It matters because a technically working system can still fail if people cannot use it or nobody takes responsibility for it.

### Name a stakeholder likely to have high power and high interest. How should they be managed?

A **project sponsor** is a good example. They may control funding and be accountable for the project's success, so they have both influence and a strong interest in the outcome.

I would manage them closely through regular updates, early discussions about risks and involvement in important decisions.

For example, if a data migration is falling behind, I would explain the impact and available options early so they can help resolve it.

### Name a stakeholder likely to have little or no power and high interest. How should they be managed?

An **end user**, such as an analyst who will use a new dashboard, could have high interest but limited decision-making power.

I would keep them informed and involve them in gathering requirements, demonstrations and testing.

Their feedback matters because they understand the daily work. Even if they cannot approve the budget, they can identify whether the solution will actually be useful.

### What is the difference between a supporter of a project and a critic?

A supporter has a positive attitude towards the project and wants it to succeed. A critic questions aspects of it or raises concerns.

For example, a supporter might welcome automated reporting, while a critic might question whether the underlying data is reliable.

I would listen to both. A critic can highlight genuine weaknesses, so I would investigate their concerns rather than assume they are being difficult.

### What is the difference between initiation and planning?

**Initiation establishes why we should do the project and whether it should go ahead. Planning works out how we will deliver it.**

For example, during initiation we might identify that manual reporting takes too long and agree that automation would be worthwhile.

During planning, we would identify the data sources, allocate resources, estimate costs and agree a schedule. That gives the team a practical way to deliver the approved idea.

### What is the difference between a champion and a supporter?

Both are positive about the project, but a **champion actively promotes it** and encourages others to get behind it.

A supporter might agree that a new reporting system is useful and cooperate when asked. A champion might demonstrate its benefits, encourage colleagues to use it and help build enthusiasm.

The difference is how actively they advocate for the change.

### What is the difference between an opponent and a blocker?

An opponent disagrees with the project or wants it changed. A blocker actively prevents progress, or has control over something the project needs.

For example, someone might oppose moving to a new database because they prefer the existing system. Someone withholding essential access could become a blocker, even if they do not oppose the overall project.

I would understand the reason, discuss the impact and work towards a resolution. If necessary, I would escalate the issue through the appropriate person.

**Note:** These attitude labels can vary between organisations, so the person's behaviour matters more than the label.

### How would you manage stakeholders with different levels of influence and interest?

I would adapt the amount and type of communication to their influence, interest and needs.

| Stakeholder position | Approach | What I would do |
| --- | --- | --- |
| High influence, low interest | Keep satisfied | Provide concise updates and involve them when a decision affects their responsibilities. |
| High influence, high interest | Manage closely | Maintain regular contact, discuss risks early and involve them in key decisions. |
| Some power, some interest | Engage proportionately | Give relevant updates, consult when their area is affected and watch for changes in their involvement. |
| High interest, low power | Keep informed | Share progress, invite feedback and involve them in demonstrations or testing. |

I would also review this throughout the project, because someone's interest or influence can change.

## Agile

### What are the Agile values?

The four Agile values prioritise:

- **People and their interactions** over processes and tools.
- **Working software** over extensive documentation.
- **Collaboration with customers** over negotiating contracts.
- **Adapting to change** over sticking rigidly to a plan.

The things on the other side still matter. For example, we still need documentation, but writing a large document should not take priority over delivering something useful.

In a data team, that could mean showing users a working report early and improving it through feedback.

### What are the Agile principles?

The Agile Manifesto has 12 principles. In everyday language, they encourage teams to:

1. Deliver useful software early and keep delivering value.
2. Accept changing requirements, including late changes.
3. Release working software frequently.
4. Keep business people and developers collaborating.
5. Support motivated people and trust them.
6. Communicate directly and effectively.
7. Measure progress through working software.
8. Maintain a sustainable pace.
9. Pay attention to technical quality and good design.
10. Keep things simple and avoid unnecessary work.
11. Give teams room to organise their work.
12. Regularly reflect and improve.

Together, they encourage frequent feedback, useful results and continuous improvement.

### What is your favourite Agile principle? Describe it.

My favourite is **regularly reflecting on how the team can improve**.

I like that it makes improvement part of the work. For example, if unclear requirements repeatedly cause us to redo a data transformation, we can discuss that and agree to review examples with the analyst before starting.

For me, the important part is acting on what we learn, so we avoid repeating the same problems.

### What Agile principle are you looking out for? Describe it.

One principle I would particularly look out for is **maintaining a sustainable pace**.

As someone starting in data engineering, I want to work carefully and consistently. If a team constantly relies on overtime, it can become harder to concentrate, test properly and spot mistakes.

I would look for realistic workloads and a team where people raise capacity concerns early. That supports reliable delivery and gives people time to do the work properly.

### What is the most popular Agile method?

**Scrum is generally recognised as the most widely used Agile framework.**

It gives teams a structure for working in short cycles, reviewing results and improving how they work. Other approaches include Kanban and Extreme Programming, and teams sometimes combine practices to suit their needs.

### What is the difference between Agile and Scrum?

**Agile is a set of values and principles, while Scrum is a framework that helps teams apply them.**

For example, Agile encourages frequent feedback. Scrum creates a regular opportunity for that through the Sprint Review.

A team can follow Agile principles using Scrum, Kanban or another approach. Scrum is one way to put Agile into practice.

### What is the difference between functional and non-functional requirements?

**Functional requirements describe what a system must do. Non-functional requirements describe the qualities or constraints it must meet.**

For a data pipeline, a functional requirement might be to read a CSV file, remove duplicate records and load the results into a database.

A non-functional requirement might be to process one million records within ten minutes or encrypt data during transfer.

Both matter: the pipeline needs to perform the right task and meet the performance and security needs of the business.

### What are the Scrum ceremonies?

The meetings commonly called ceremonies are:

- **Sprint Planning:** Agree the goal and plan the work.
- **Daily Scrum:** Inspect progress and adjust the Developers' plan.
- **Sprint Review:** Discuss results and next steps with stakeholders.
- **Sprint Retrospective:** Improve how the team works.

The formal term is **events**, and the Sprint itself is also an event.

### What are the Scrum artifacts?

The three artifacts are:

- **Product Backlog:** The ordered work needed to improve the product.
- **Sprint Backlog:** The Sprint Goal, selected work and delivery plan.
- **Increment:** The usable result meeting the Definition of Done.

Their commitments are the **Product Goal, Sprint Goal and Definition of Done**, respectively.

### What is a sprint?

A Sprint is a fixed-length event lasting **one month or less**, during which the team works towards a Sprint Goal and creates usable value.

For example, a two-week Sprint could focus on making validated sales data available for reporting.

### What is a Scrum Master?

The Scrum Master helps establish Scrum and improve the team's effectiveness. They coach the team, help address impediments and support productive events.

For example, they might help resolve an access issue affecting delivery. They are not there to allocate everyone's tasks.

### What is a Product Owner?

The Product Owner is accountable for maximising the product's value and managing its backlog effectively.

For example, they might prioritise reliable sales figures over extra dashboard styling because accurate figures deliver more immediate business value.

### What are personas?

Personas are **research-informed descriptions of the types of people who will use a product**. They capture things such as their goals, responsibilities and difficulties.

For example, a sales analyst persona might need reliable figures each morning but have limited technical knowledge.

That helps the team make decisions around actual user needs, such as providing clear error messages instead of expecting the analyst to investigate technical logs.

### What makes a good user story?

A good user story explains **who needs something, what they need and why it matters**.

For example:

> As a sales analyst, I want validated sales data available each morning so that I can prepare accurate daily reports.

It should be small enough to deliver, clear enough to discuss and supported by testable acceptance criteria.

A useful checklist is **INVEST**: Independent, Negotiable, Valuable, Estimable, Small and Testable. That helps us avoid stories that are too vague or too large.

### What types of people are on a Scrum Team?

A Scrum Team includes a **Product Owner, Scrum Master and Developers**.

Developers covers the people creating the product, which can include data engineers, testers and other specialists. The team collectively needs the skills to deliver usable results.

### Who decides who does what user story on a Scrum Team?

The team organises its own work. The Developers decide together how to divide and complete it, considering skills, capacity and the Sprint Goal.

For example, I might take a Python transformation task while pairing with someone on database work. The Scrum Master would not assign everyone their stories.

### Should a user story be fleshed out immediately when it is created?

No, it does not need every detail immediately. A story can start as a brief idea and become clearer through discussion and refinement.

For example, 'automate monthly reporting' might initially be a large backlog item. As it becomes a priority, we would identify the users, data sources and acceptance criteria, then split it into smaller stories.

That avoids spending lots of time detailing work that may change or never be selected.

### What is a Gherkin script?

Gherkin is a structured way of describing a system's expected behaviour using readable scenarios, commonly with **Given, When and Then**.

For example:

```gherkin
Feature: Validate sales data

  Scenario: Reject a record with no order ID
    Given a sales record has no order ID
    When the pipeline validates the record
    Then the record should be rejected
    And the rejection reason should be recorded
```

It helps business people, developers and testers agree on what should happen. Tools such as Cucumber can connect those steps to code to run automated tests.

### What makes a good Definition of Done?

A good Definition of Done is **clear, shared and objectively checkable**. It describes the quality standards work must meet before it can count as complete.

For a data pipeline, that could include code review, passing automated tests, checked data quality, useful error logging and updated documentation.

That prevents one person calling something done because the code runs while someone else still needs to test or support it.

### What is a Definition of Ready?

A Definition of Ready is a checklist some teams use to judge whether a backlog item is clear enough to start.

For example, a pipeline story might need an agreed data source, sample data, clear acceptance criteria and understood dependencies.

It helps reduce avoidable uncertainty, but it should leave room for learning during the work. It is an optional team practice rather than a required part of Scrum.

### What are the advantages and disadvantages of Agile methodologies over Waterfall?

Agile's main advantage is that teams **deliver in smaller pieces and get feedback earlier**. That makes it easier to adapt when requirements change.

For example, we could deliver a pipeline for one data source, get feedback from analysts and use that learning before adding the next source.

The challenges are that it needs regular stakeholder involvement, scope needs careful management, and exact long-term costs or delivery dates can be harder to predict when requirements are evolving.

Waterfall generally plans work through sequential phases. It can suit work with stable requirements and clear approval stages, but feedback on the completed solution can arrive later, making changes more expensive.

I would consider the uncertainty, dependencies and business needs before choosing an approach.

