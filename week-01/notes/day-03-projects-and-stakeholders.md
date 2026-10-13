# Day 3 — Projects and stakeholders

23 September 2026

[← Week 1](../README.md) · [Day 2](day-02-presentations-and-interview-skills.md)

We started with practice and feedback on our introductions, then looked at Markdown for documentation. Most of the day focused on how projects are planned and how to identify and manage stakeholders. We used a parachuting school as a group scenario and finished with professional awareness.

## Feedback on my introduction

I gave my “tell me about yourself” introduction, covering my psychology background, my move into data and AI, my project work and volunteering, and what I want to develop at Sparta.

The feedback was to make the connection between those parts clearer:

- Explain **why I moved from psychology into data**, rather than only listing the qualifications and skills.
- Bring the volunteering into the story more naturally instead of making it feel like a separate point at the end.
- Shorten the project explanation. Give enough detail to make it interesting and leave room for follow-up questions.
- Keep working on voice projection so the delivery gives the content more impact.
- Be more specific about the direction I want to take, such as the type of role or skills I want to work towards.

The trainer noticed improvement in my delivery from the previous day. The next step is to keep the introduction focused and explain the decisions behind my journey. I do not need to present myself as an expert; I need to show what I can already do and where I want to develop as a junior.

## Markdown for notes and documentation

Markdown is a way to format plain text using simple symbols. Files use the `.md` extension, and tools such as VS Code and GitHub can display the formatted result.

The main features we covered were headings, lists, bold and italic text, inline code and code blocks.

````markdown
# Main heading
## Section heading
### Smaller heading

- A bullet point
- Another point

1. First step
2. Second step

**Bold text**
*Italic text*

Use `print()` to display a value.

```python
name = "Syed"
print(name)
```
````

Single backticks are useful for a filename, command or short piece of code inside a sentence. Three backticks create a code block. Adding a language name, such as `python` or `sql`, allows supporting tools to highlight the syntax. Displaying code in a Markdown block does not run it.

The preview helps check how the document will look when someone reads it. Remember to save changes if autosave is not enabled.

### Naming files and folders

Use clear, consistent names such as `projects-and-stakeholders.md` or `week-01`. Hyphens and underscores avoid the need to deal with spaces in command-line paths. Filenames with spaces can work, but often need quotes around them when used in commands.

### Why documentation matters

Someone else should be able to understand a process when the person who created it is unavailable or has moved to another team. A useful guide explains the steps, the relevant code and what the result should look like.

For a longer program, it can be clearer to explain one section at a time with small code blocks rather than paste the whole file without context.

## BAU, projects and programmes

- **Business as usual (BAU)** is the ongoing work that keeps an organisation running. For a data team, this could include checking regular pipeline runs, investigating failures and maintaining existing reports.
- **A project** is temporary work with a defined purpose and an intended outcome. Implementing a new CRM system is an example.
- **A programme** brings related projects together to achieve a wider objective. A digital transformation programme might include a website, an online store and a CRM implementation.

A project has an endpoint and needs to be formally closed. Once a system is handed over, its ongoing operation and support can become part of BAU.

We also discussed **CRM**, meaning customer relationship management, and **ERP**, meaning enterprise resource planning. A CRM supports work with customer information and interactions. An ERP brings together information and processes across different parts of an organisation.

### Why projects become difficult

Common challenges include unclear requirements, limited resources, conflicting priorities, access problems and teams working to different schedules. Changes in budget, staffing or scope can affect work that has already been planned.

The NHS Test and Trace programme was used as a research case study. The questions were about its goals, what went wrong, who was responsible for delivery and the wider impact. The project-management lesson was to consider coordination, reliable systems, adoption and trust as well as whether the technology had been built.

## The project life cycle

| Stage | Main purpose |
| --- | --- |
| Initiation | Understand the problem, objectives, requirements, scope and whether the project is feasible. |
| Planning | Work out the tasks, resources, budget, responsibilities and schedule. |
| Execution | Carry out the work and produce the deliverables. |
| Monitoring and control | Check progress, quality, risks and whether changes are needed. |
| Closure | Agree that the deliverables have been accepted, complete the handover and record lessons learned. |

Execution and monitoring happen together. A team may produce something, review it and adjust the work several times before it is ready. The life cycle gives a broad view of the project; methods such as Agile or Waterfall describe more about how the work is organised.

Closure involves more than saying the system works. It includes acceptance, documentation and clarity about what has been delivered and how it will be supported.

## Planning the parachuting school projects

The scenario was a parachuting school in New Zealand carrying out a digital transformation programme with three projects:

1. A website with information about the school, instructors and class bookings.
2. A separate online store for buying and renting equipment.
3. A CRM for managing customer information and bookings.

I was in the **website team**. Our first task was to think about the considerations and deliverables needed before development could start.

Our group discussed ease of use, mobile access, school and instructor information, booking availability, payments, and the ability to amend or cancel bookings. We also considered access to data and the safety information users would need.

The feedback was to group the detailed ideas into broader categories rather than leave them as one long list. Before starting a project, consider:

- **Objectives and success measures:** what problem are we solving, and how will we know the result is useful?
- **Scope:** what is included, and what is outside the project?
- **People and resources:** who needs to be involved, and what time, budget and skills are available?
- **Technology and integrations:** what systems are needed, and how will they connect?
- **Current processes:** how does the work happen now, and what will change?
- **Risks and requirements:** what could go wrong, and what security, privacy or other requirements apply?
- **Timelines and deliverables:** what needs to be produced, by whom and when?

Possible deliverables discussed across the groups included requirements documents, process maps, a solution design, a data migration plan and training material. A list of features is useful, but it is only part of the preparation.

## Time, cost and scope

The **triple constraint** describes the relationship between time, cost and scope. Changing one can put pressure on the others and affect quality.

- Adding more features may need more time, more resources or both.
- Bringing a deadline forward may mean reducing scope or changing the resources available.
- Cutting the budget may limit what can be delivered within the original schedule.

For the school website, adding a chatbot after agreeing the booking system would need to be considered as extra work. It should not be assumed that the team can deliver it within the same time and budget without a trade-off.

The practical point is to discuss changes openly and agree what can realistically be delivered.

## POPIT — looking beyond the technology

POPIT considers the wider effect of a change:

| Area | Questions to ask |
| --- | --- |
| People | Who will use the system? What training or support will they need? |
| Organisation | Will responsibilities, team structures or decision-making need to change? |
| Processes | How will everyday tasks and workflows change? |
| Information technology | What software, hardware, infrastructure and security measures are needed? |

For example, launching an online store also creates work around checking orders, managing rentals and handling returns. The software needs people and processes around it to work properly.

## Stakeholders

A stakeholder is a person, group or organisation with an interest in, or affected by, a change. Stakeholders are not limited to the people building or directly using a system.

Categories discussed included customers, employees, managers, owners, suppliers, partners, regulators and competitors. These are starting points for identifying people, not a complete list or a fixed classification.

For example, a customer can be affected by a CRM even if they never log into it. Staff use it to manage the customer's information and interactions.

### Identifying and managing stakeholders

The process is to:

1. Identify who is involved or affected.
2. Understand their interest and their ability to influence the project.
3. Consider their attitude towards the change.
4. Decide how to communicate with them and involve them.
5. Review this as the project develops.

A stakeholder's position can change. Someone may gain more authority, become more interested or raise a concern that changes the way the team needs to work with them.

### Power and interest

The grid we discussed used power or influence alongside interest to help choose an approach:

| Power or influence | Interest | Approach |
| --- | --- | --- |
| High | High | Actively manage and involve them closely. |
| High | Some | Keep them satisfied. |
| High | Little or none | Watch for changes in their interest or involvement. |
| Some | Some or high | Keep them on side and address relevant concerns. |
| Little or none | Some or high | Keep them informed. |
| Little or none | Little or none | Give them a lower communication priority. |

High power does not automatically mean high interest. A senior decision-maker may control the budget without wanting every technical update. Someone using the system every day may be very interested but have less authority over the project.

“Keep satisfied” and “keep on side” are also different. A person with high power may be able to stop funding or redirect the project. Someone with less power may still influence others or affect cooperation, even if they cannot make those decisions themselves.

### Stakeholder attitudes

- **Champion:** actively helps the project move forward.
- **Supporter:** is in favour of the project but may not be actively involved.
- **Neutral:** has no strong view for or against it.
- **Critic:** has concerns or a negative view without actively obstructing the project.
- **Opponent:** actively works against the project.
- **Blocker:** can prevent progress.

These descriptions help decide how to engage with someone. They can change over time, so they should not become permanent labels.

## Stakeholder mapping exercise

We returned to our groups to identify stakeholders for our assigned project and place them on the power-interest grid, with reasons for our choices.

For the website, our group considered new and existing customers, instructors, managers, IT staff, advertising partners, suppliers, payment providers, regulators and competitors.

One discussion was whether existing customers had some influence. Our group argued that feedback, reviews and the choice to use a competitor could affect the business. The trainer questioned how much direct power that gave them over this particular website project, but accepted that the reasoning mattered.

The main lessons from the feedback were:

- Be specific. “Employees” is too broad if it includes both the people building the system and those only using it occasionally.
- Assess the stakeholder against the particular project. Someone may have a different interest in the website, store and CRM.
- Separate importance from interest. Being important does not mean needing every update.
- Explain the reasoning behind the placement rather than treating the grid as a set of automatic answers.

Clear communication, respect and trust make it easier to deal with disagreements and keep the project moving.

## Professional awareness

We discussed everyday choices that matter when joining a client team.

**Lock the workstation when stepping away.** Even a short break can leave sensitive information or systems accessible to someone else. Saving work and keeping the desk tidy are useful habits too, but they do not replace securing the screen.

On the first days in a new team:

- Introduce myself and make an effort to get to know people.
- Arrive with enough time to allow for delays.
- Be patient while access, equipment and induction are arranged.
- Understand how and why the team works before suggesting that they change their approach.

Being proactive should go alongside listening and learning the context.

## Work for the next day

Prepare **three professional-awareness quiz questions** in our groups, covering office or remote work and the first days with a team. The original suggestion was five questions, but this was reduced to three.

The questions should require some thought, with plausible choices and a reason for the best answer. Slides were optional; having the questions ready to present was the main requirement.

There was also optional introductory research on Agile and Scrum ahead of the next day, with Markdown encouraged for taking notes.
