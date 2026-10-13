# Day 4 — Agile and Scrum

24 September 2026

[← Week 1](../README.md) · [Day 3](day-03-projects-and-stakeholders.md)

Today covered how teams organise development work, from Waterfall to Agile and Scrum. We then looked at requirements, user stories, acceptance criteria and planning a sprint. We also continued practising introductions and presented our professional awareness quizzes.

## More practice with introductions

The feedback from the morning introductions built on the previous day:

- Choose a few useful points and explain them clearly. Trying to fit everything in can make the introduction too long.
- Explain the decisions behind a career change so the listener can follow the story.
- Use natural wording and practise enough to avoid relying heavily on a script.
- Speak deliberately, with pauses, and finish clearly before handing back to the interviewer.
- Give specific experience that can lead to follow-up questions, rather than a long list of claims about personal qualities.

After practising, identify one thing that went well and one thing to improve.

## Projects and the development life cycle

The **project life cycle** covers the whole project, including its purpose, planning, delivery and closure. The **systems development life cycle (SDLC)** focuses on developing the system that meets the requirements.

There are different ways to organise that development. A team can move through stages mainly in sequence, or work through smaller cycles and improve the product over time.

### Waterfall

Waterfall takes a mainly sequential approach: requirements and analysis, design, development, testing and operation. There is substantial planning before development begins.

This can suit work where the requirements are stable, the stages are well understood and there is a clear picture of the intended result.

| Advantages | Limitations |
| --- | --- |
| Clear stages, with an identifiable start and finish. | Moving back to an earlier stage can be difficult and expensive. |
| Requirements are considered before building starts. | Requirements may change before the finished system is delivered. |
| Progress is easy to describe in terms of the current stage. | Users may discover misunderstandings late if they only see the result near the end. |
| Detailed planning can help with budgets and coordination. | Waiting for one stage to finish can delay the next team's work. |

Leaving most testing until late in development also makes faults harder to deal with. Going backwards is possible, but it can involve substantial rework.

I raised the point that a mistake discovered further down the sequence could be difficult to backtrack and correct. This also applies when the original requirement changes.

### Iterative and incremental development

**Iterative** means revisiting and improving the work through repeated cycles. **Incremental** means building up the product in usable additions.

Instead of waiting for one large delivery, the team produces smaller results, gets feedback and uses it to decide what to do next. Users can start receiving value earlier, and the team has more opportunities to correct its direction.

The football analogy helped explain this: several smaller kicks allow adjustments as the target moves, while one big kick depends heavily on getting the direction right at the start.

This still needs discipline. Without enough structure, scope can keep growing, documentation can become too thin and it can become unclear when something is finished.

## Agile

Agile is an approach to working that emphasises feedback, collaboration and adapting as more is learned. Scrum is one framework used to put that approach into practice.

The four values in the [Agile Manifesto](https://agilemanifesto.org/) emphasise:

| Value | What it means in practice |
| --- | --- |
| People and their interactions | Make communication and teamwork central to delivery. Tools and processes should help people work together. |
| Working software | Deliver something useful and working. Documentation supports that work and still matters. |
| Collaboration with the customer | Keep discussing needs and reviewing results as the work develops. |
| Responding to change | Adjust the plan when new information changes what is needed. |

The values describe priorities. They do not mean abandoning planning, documentation, contracts or tools.

I contributed to the discussion about working software: spending months documenting a system does not achieve the goal if the system itself is not being developed.

We also discussed a **sustainable pace**. The team should be able to keep working effectively over many iterations, rather than rely on a burst of effort that cannot be maintained.

## Scrum

Scrum gives the team a regular structure for planning, doing work, inspecting the result and improving how it works.

A **sprint** is a fixed period of work towards a goal. Two-week sprints were used as a common example. The [Scrum Guide](https://scrumguides.org/scrum-guide.html#the-sprint) sets the maximum length at one month.

### The Scrum team

| Role | Main responsibility |
| --- | --- |
| Product Owner | Maximise the product's value, communicate its goal and manage the Product Backlog, including the order of work. |
| Scrum Master | Help the team use Scrum effectively, support the events and help remove obstacles. |
| Developers | Plan and carry out the work needed to create a usable Increment. |

In Scrum, **Developers** includes the people doing the product work, which can include analysts, data engineers and testers as well as software developers.

The team is cross-functional and self-managing. It brings together different skills and decides how to organise the work. The Scrum Master supports this; they do not simply assign everyone tasks as a line manager would.

The Product Owner brings together stakeholder needs, but communication is still a team responsibility. People need to be able to ask questions and clarify requirements during the work.

### The three artefacts

- **Product Backlog:** the ordered, evolving list of work needed for the product. Items can be added, refined, removed or reordered as needs change.
- **Sprint Backlog:** the Sprint Goal, the items selected for that sprint and the plan for delivering them.
- **Increment:** a usable addition to the product that meets the Definition of Done.

Backlog items are pieces of work for the product, rather than separate products. The Sprint Backlog gives the team a manageable focus within the larger Product Backlog.

I asked whether there was a particular tool required to track the backlogs. There is no single required tool: a digital board, a whiteboard or sticky notes can support the process. The important part is that the work is visible and understandable to the team.

### How a sprint works

1. **Sprint Planning:** agree the goal, select suitable work from the Product Backlog and plan how to approach it.
2. **Work during the sprint:** develop, test and collaborate on the selected work, adjusting the plan as needed.
3. **Daily Scrum:** check progress towards the goal, identify blockers and coordinate the next work.
4. **Sprint Review:** inspect the product outcome with stakeholders and discuss what should happen next.
5. **Sprint Retrospective:** reflect on how the team worked and agree useful improvements.

The Daily Scrum is a 15-minute planning and coordination event; the development work happens throughout the sprint. A completed Increment can be delivered before the Sprint Review. Work must meet the Definition of Done to count as part of an Increment. These distinctions are set out in the [Scrum Guide](https://scrumguides.org/scrum-guide.html#daily-scrum).

Unfinished work needs to be reconsidered in the Product Backlog. It may still be a priority for the next sprint, but the team should review that rather than assume every item automatically carries over unchanged.

The distinction to remember is **review = product**, **retrospective = how we work**. Retrospective ideas briefly shown included a mood graph and discussing what to keep doing, do more or less of, start and stop.

### Transparency, inspection and adaptation

These are the three pillars of Scrum:

- **Transparency:** make the real situation visible, including problems, delays and uncertainty.
- **Inspection:** regularly check the work and progress against the goal.
- **Adaptation:** use what has been learned to change the approach.

They depend on each other. If the information is inaccurate, the team cannot inspect it properly or make useful changes.

If a task is taking several days, be clear about that in updates. Explain what has progressed and what is blocking it. Rewording the same work to make it sound like something new does not help the team.

## Requirements

Requirements describe the needs and conditions that the solution must meet. Business stakeholders, people building the system and testers all use them, but bring different perspectives.

### Functional and non-functional requirements

| Type | Meaning | Example |
| --- | --- | --- |
| Functional | What the system needs to do. | Adding an item to a basket updates the item count and total. |
| Non-functional | The qualities and constraints the system must satisfy. | Transactions complete within two seconds under agreed normal load conditions. |

Non-functional requirements are not automatically optional or lower priority. A system can have the required features and still be unsuitable because it is unreliable, inaccessible or insecure.

Examples include performance, security, reliability, scalability, maintainability, usability and accessibility. Make the requirement clear enough to assess, rather than simply saying the system should be “fast” or “easy to use”.

### Gathering requirements

Different methods reveal different information:

- **Observation:** watch how people use the current system and where they struggle.
- **Interviews and workshops:** discuss needs, expectations and problems directly.
- **Document analysis:** review existing processes and system information.
- **Brainstorming:** explore possible improvements.
- **Surveys and questionnaires:** collect views from a larger group.
- **Prototypes and wireframes:** show an early idea so users can respond to something concrete.

The Product Owner has a central role, but gathering and clarifying requirements can involve the whole team.

## User stories

A user story is a short description of a need from a user's perspective. The structure we covered was:

> As a [type of user], I want [goal], so that [reason].

For example: **As a registered user, I want to sign in securely so that I can view my profile.**

The story starts a conversation. It is not a full specification on its own. Discussing the story helps the team understand the need and agree the details when the work is approaching.

Be specific about the user and the benefit. Avoid filling the story with technical implementation choices before the team has discussed the options.

An **epic** is a larger piece of work that needs to be broken into smaller stories. Secure account access could involve registration, signing in and password recovery.

### Who should discuss a story?

Anyone with a relevant need can suggest a story. The Product Owner remains responsible for managing the backlog.

The **Three Amigos** approach brings together three perspectives:

- **Business:** what problem are we solving and why does it matter?
- **Development:** how could we build it?
- **Testing:** how will we check it, and what could go wrong?

Other perspectives can be useful, including end users, security and operations. The point is to involve the people needed to understand the story properly, rather than add people just to reach a particular number.

### INVEST and the three Cs

**INVEST** is a checklist for thinking about story quality:

| Letter | Meaning |
| --- | --- |
| Independent | The story makes sense on its own; minimise dependencies where possible. |
| Negotiable | Leave room to discuss the solution. |
| Valuable | It provides a benefit to the user or business. |
| Estimable | The team understands enough to judge its size. |
| Small | It is a manageable piece of work; split large stories. |
| Testable | There is a clear way to check whether it has been achieved. |

The **three Cs** describe how the story develops: **Card** records the initial idea, **Conversation** builds shared understanding, and **Confirmation** checks the agreed outcome.

## Acceptance criteria

Acceptance criteria describe what must be true for a particular story to be accepted. They are specific to that story.

We covered the **Given / When / Then** structure:

- **Given:** the starting situation.
- **When:** the action or event.
- **Then:** the expected result.

For the sign-in example:

| Scenario | Given | When | Then |
| --- | --- | --- | --- |
| Successful sign-in | I am a registered user on the sign-in page. | I enter valid credentials. | I can access my profile. |
| Incorrect password | I am on the sign-in page. | I enter an incorrect password. | Access is refused and an appropriate error message appears. |

Consider the happy path, failure cases and relevant alternatives. Testing only the successful route leaves important behaviour unspecified.

The user-story and acceptance-criteria writing exercises were skipped because of time, so this part of the day focused on the concepts and examples.

## Estimation and prioritisation

Estimation asks how much work something involves. Prioritisation asks how important it is to do. A small task can still be a high priority.

Teams can estimate using story points, time or relative sizes such as small, medium and large. The scale needs a shared meaning so estimates can be compared sensibly.

**Planning poker** involves people choosing estimates independently and revealing them together. If the estimates differ widely, discuss the reasons and estimate again. The discussion can reveal assumptions, missing information or work that someone else had not considered.

### Building-height exercise

We estimated a building's height from a photograph. My first answer was **50 metres**, which was a guess. Other approaches included counting floors and estimating the height of each floor.

After comparing answers and hearing the reasoning, the group estimated again. The height given was **82 metres**. The exercise showed why explaining an estimate is useful: the team can improve its judgement by understanding how people reached their answers.

### MoSCoW prioritisation

| Category | Meaning |
| --- | --- |
| Must have | Essential for the agreed delivery. |
| Should have | Important, but the delivery can still work without it for now. |
| Could have | Useful if time and resources allow. |
| Won't have this time | Explicitly outside the current scope; may be reconsidered later. |

Agreeing what will not be included helps control scope. Priorities can change, but the changes need to be understood by the team.

## Minimum viable product

An **MVP** has enough functionality to be useful to early users and generate feedback for further development.

The emphasis was on getting a useful first version in front of someone, finding out what needs changing and improving it. Spending too long polishing before getting feedback can mean polishing the wrong thing.

For training tasks, this means producing a working first version within the available time and being clear about what it can do and what still needs work.

## Definition of Ready and Definition of Done

These give the team shared expectations about starting and completing work.

| Term | Purpose |
| --- | --- |
| Definition of Ready | A team's agreed checks for whether work is understood enough to begin, such as clear acceptance criteria and known dependencies. |
| Definition of Done | The shared quality standard work must meet to be considered complete, such as required testing and review. |
| Acceptance criteria | The specific behaviour or outcome required for an individual story. |

The distinction is between **shared standards** and **story-specific requirements**. A successful sign-in is specific to the login story. Required testing and review can apply across many stories.

A Definition of Ready is an optional team practice. The Definition of Done is part of Scrum and applies to the Increment; it should reflect the product's quality requirements. See the [Scrum Guide](https://scrumguides.org/scrum-guide.html#definition-of-done).

## Professional awareness quiz

I presented the website group's three questions:

1. **Running late to a meeting:** let the organiser or team know as soon as possible.
2. **Unclear task outcome:** ask for clarification on the requirements and expected result before making assumptions.
3. **Finishing work early:** review the work, then ask whether there are other priorities to support.

The other groups covered speaking privately and politely about distractions, reporting mistakes, warning about a likely missed deadline and helping a colleague correct a report before it goes to a client.

Some answers depended on the situation and the organisation's process. The common points were to communicate early, take responsibility, explain the problem clearly and help find a way forward.

For joining a client team, this also means looking for work I can contribute to, asking for help when needed and keeping the team informed rather than waiting silently for instructions.
