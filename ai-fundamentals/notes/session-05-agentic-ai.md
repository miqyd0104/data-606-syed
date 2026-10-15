# Session 5 — Agentic AI

[← AI Fundamentals](../README.md) · [Original slides](../slides/session-05-agentic-ai.pdf) · [Previous: AI for Automation](session-04-ai-for-automation.md)

This session moves from specifying a fixed sequence of steps to delegating a goal. An AI agent can choose actions, use tools, inspect results and adjust its approach. That flexibility makes permissions, independent verification and ownership especially important.

The main question is not only whether the answer looks right, but **what the system actually accessed, changed or executed while producing it**.

## From assistance to delegation

The opening slides show a progression in how work is organised:

| Mode | How the work proceeds |
| --- | --- |
| **Manual** | A person performs the work. |
| **Assistance** | AI drafts or suggests; the person directs each step and accepts or rejects it. |
| **Collaboration in a defined flow** | A workflow runs, with AI contributing to a specified part. |
| **Delegation** | A person sets the goal and boundaries; the model chooses steps, order and tools within them. |

The slide heading says “5 levels”, but the supplied diagram shows these four labelled modes. The useful distinction is who controls the sequence of work; there is no missing fifth category to infer from the file.

The course also describes enterprise systems moving from recording information, through assisting people, to acting on goals. Systems of record such as CRM or ticketing tools remain important because an agent still needs reliable information and places to record outcomes.

## What makes a system agentic?

An **AI agent** uses a model to pursue a goal through actions and feedback. Its surrounding software provides tools, context, instructions and controls. A model alone is not the whole agent.

The course suggests asking whether the system has a goal, can use tools, can choose a sequence and can check its own progress. These questions help analyse a setup; they are a practical heuristic rather than a universal industry definition.

Product names alone are insufficient. The same product can offer simple completion, a fixed workflow and a tool-using agent depending on its mode and permissions.

### Agent versus workflow

| Defined workflow | Agent |
| --- | --- |
| The path and branches are specified in advance. | The model can choose parts of the path as work unfolds. |
| A known trigger leads through configured steps. | A goal guides planning and tool selection. |
| Useful when the process is stable and predictable. | Useful when the necessary steps depend on discoveries. |
| Can include AI calls, conditions, loops and retries. | Can also call fixed workflows as tools. |

The key difference is **dynamic control of the process**, not simply the presence of a loop. Ordinary workflows can repeat or retry. Anthropic's [explanation of workflows and agents](https://www.anthropic.com/engineering/building-effective-agents) makes the same distinction between predefined paths and model-directed processes, and recommends adding complexity only where it improves the result.

For a daily report with a fixed source and formula, a script or workflow may be easier to verify. For investigating an unfamiliar codebase, the relevant files and next steps may only become clear after inspection, which can make an agent useful.

## The agent loop

The course describes a cycle of orienting, planning, acting, checking and reporting.

```text
Goal and boundaries
    ↓
Orient: inspect the task, context and available tools
    ↓
Plan: choose useful steps
    ↓
Act: use a permitted tool
    ↓
Check: compare the result with the goal and evidence
    ├── more work needed → adjust the plan and continue
    ├── blocked or outside authority → ask or escalate
    └── complete → report the outcome and supporting evidence
```

The check step might inspect a file, read a tool result or run a test. It should involve evidence about what actually happened. A statement such as “I successfully updated every record” is a claim to verify, not proof that the update was complete.

The loop also needs limits: completion criteria, boundaries on actions, reasonable time or cost limits, and a way to stop. More iterations are not necessarily progress.

## Five things an agent needs

| Need | What to specify | Example for a data-cleaning task |
| --- | --- | --- |
| **Mission** | Goal and definition of success. | Produce a cleaned copy and a report of rejected rows. |
| **Context** | Relevant facts, files and business rules. | Input schema, missing-value definitions and acceptance criteria. |
| **Tools** | Operations it can perform. | Read files, run a local script and inspect outputs. |
| **Permissions** | Which resources and actions are allowed. | Work only in the exercise folder; do not overwrite the source. |
| **Instructions or skills** | Procedures and constraints for the task. | Follow the agreed validation rules and report unresolved cases. |

Tools provide capability; permission provides authority. An instruction to use a tool does not itself create access rights, and having access to a system does not make every action in it appropriate.

The slides mention connectors, plugins, MCP and skills. These are related but different ideas: connectors expose integrations, plugins can package capabilities, MCP is a protocol for connecting tools and context, and skills can supply reusable task instructions. Their exact behaviour depends on the implementation.

Source material also needs boundaries. A webpage, spreadsheet cell or repository file may contain instructions written by someone else. Treat that content according to its role as evidence; it should not silently override the user's goal or authorise a new external action.

## General-purpose agent examples

### Preparing a project meeting brief

The course demonstration asks an agent to work through project information and produce a one-page brief. Compared with Session 3's carefully supplied context, the agent may help locate and select the sources as part of the task.

That adds questions to the review: did it read the right files, miss a relevant document, prefer an obsolete report or confuse a proposed decision with an approved one? Source references help check those choices.

The project material and final demonstrated brief are not supplied here, so these notes describe the task rather than claim its results.

### Updating attendance data

Another example asks an agent to preserve a workbook's structure and formulas, calculate averages and flag attendance below 80%.

Before delegating, clarify:

- How names or identifiers should be matched across sources.
- What counts as an attended, absent or excused session.
- Which sessions belong in the denominator.
- How duplicate names, missing values and conflicting records are handled.
- Which columns or formulas may change.

For illustration, 7 attended sessions out of 10 counted sessions gives 70%. Exactly 80% is not **below** 80%. If some sessions are excluded by the agreed policy, calculate with that denominator rather than silently treating blanks as absence.

Independent checks should include row counts, several manually recalculated cases, threshold cases, ambiguous matches and preservation of existing formulas. The actual workbook is not included in the supplied slides.

## Coding agents

A coding agent can inspect repository files, edit code, run commands and use errors or test results to guide further changes. The model proposes actions; the surrounding tools execute permitted operations and return observations.

Useful feedback includes syntax errors, test failures, application output and differences between the old and new files. A passing test suite is valuable, but it only checks what those tests cover.

The slide demonstration extends the earlier inference-parameter task with repeated trials and an HTML report. To evaluate that kind of result, check that the recorded outputs came from actual runs, that comparisons hold relevant settings steady, and that the report distinguishes observed results from interpretation. No demo source code or completed results were supplied for these notes.

### Version control has limits

Git can help inspect and reverse committed file changes. It does not automatically undo a sent email, an external database update or a leaked credential. Backups and rollback plans need to match the kinds of action the agent can perform.

Terminal access can also be constrained. Do not assume an agent must receive unrestricted access to the machine just because a coding task benefits from running tests.

## Vibe coding and responsibility

The slides describe “vibe coding” as building through natural-language requests and rapid experimentation, sometimes with little understanding of the generated implementation. It can make prototyping accessible, but working-looking output can hide errors, security problems or maintenance costs.

The course guidance is that learners should understand and be able to explain submitted or client-facing work. A useful self-check is to close the AI tool and explain the design, important code paths, assumptions and tests. If I cannot explain or maintain the result, I have not finished taking ownership of it.

The safer development progression in the slides is to begin with a sandbox and synthetic data, test the behaviour, and only move into an appropriately controlled live environment after the required checks. A demo working once is not the same as readiness for real users.

## The five risk questions

The final part of the course provides five questions for assessing a delegated task.

| Question | What to establish | Data-task example |
| --- | --- | --- |
| **Access** | What can the agent read? | Only the agreed input folder, not unrelated client records. |
| **Action** | What can it create, change or execute? | Write a new output and run local validation; no external publishing. |
| **Blast radius** | How far could a mistake reach? | One copied exercise file versus a shared production database. |
| **Reversibility** | Can the effects be undone, and how? | Recreate an output from preserved inputs; identify effects that backups cannot undo. |
| **Verification** | How will correctness be established independently? | Compare counts, reconcile totals, inspect exceptions and test business rules. |

“Blast radius” means the scope of possible harm from an error. Read-only access can still expose confidential information, so lack of write permission does not eliminate all risk.

Apply **least privilege**: restrict resources, actions and access duration to the task's needs. Use explicit checkpoints before consequential steps, and define who can stop the task or resolve an exception.

## Independent verification

An agent checking its own work is useful during execution. Final verification should also use evidence independent of its assertion that it succeeded.

| Claim | Stronger evidence |
| --- | --- |
| “All records were processed.” | Reconciled input, accepted, rejected and output counts, accounting for the intended transformation. |
| “The calculation is correct.” | Recalculation from source values and checks of boundary cases. |
| “The summary is accurate.” | Each significant statement traced to the original material. |
| “The code works.” | Relevant tests, inspection of the change and behaviour against requirements. |
| “The workbook structure is preserved.” | Comparison of sheets, rows, formulas and formatting where required. |

A second model's opinion can be useful, but agreement between models does not replace source evidence or executable checks. They can share the same mistaken assumption.

For the IMDb exercise, a verification plan might check the title-type rule, the minimum-year boundary, missing-year handling and the relationship between input and output records. The correct counts depend on the real data and transformation; they should be measured rather than invented in a report.

## Cost and ownership

The cost of an agent task can include model usage, tool calls, execution time, platform fees, human review and correction. An agent that makes many unnecessary calls or repeatedly pursues a failing approach can cost more without improving the outcome.

Measure benefit against the manual or workflow alternative. Include the consequences of a wrong result, not just the visible usage charge. The person or team accepting the work remains responsible for deciding whether it is fit for purpose.

## Final assignment: delegate and verify a real task

The course asks for a realistic business or coding task delegated to an agent. The submission should demonstrate the process and evidence, not only display a polished final artifact.

The slide refers to a submission document to complete; that template is not among the supplied files. The required areas are:

1. **Starting point and justification:** describe the task and explain why an agent is appropriate compared with a fixed workflow.
2. **Prompt and setup:** show the mission, context, tools, instructions and permissions.
3. **Plan and adjustments:** explain the initial approach and changes made as the task progressed.
4. **Recorded process:** include a recording and identify where a person intervened.
5. **Artifact and verification:** provide the result and evidence of independent checking.
6. **Five risk questions:** cover access, action, blast radius, reversibility and verification.
7. **Ownership, cost and risk:** explain who is accountable and the tradeoffs of the chosen approach.

A useful evidence log records the step, intended outcome, tool or action, observation and verification. Record actual behaviour, including failures and corrections. Do not reconstruct a flawless story after the fact or claim unrun tests.

These notes summarise the assignment; they are not a completed agent project or a record of a submitted assessment.

## Questions to check understanding

1. Can a fixed workflow have loops and retries?
2. What separates a model from an agent system?
3. Why is an agent's statement that it finished not sufficient verification?
4. What does least privilege mean for a file-processing task?
5. Can a Git revert undo every effect of a coding agent?
6. Why might a simple workflow be preferable to an agent?

**Suggested answers:** 1. Yes; loops alone do not make it agentic. 2. The agent system combines the model with goals, tools, context and control logic. 3. The statement may be mistaken; inspect the actual outputs and effects. 4. Limit access and actions to the files and operations needed. 5. No; external actions may remain. 6. A stable, known process can be more predictable, cheaper and easier to verify with fixed steps.

## Source guide

- [Session 5 slides](../slides/session-05-agentic-ai.pdf): PDF pages 4–17 for delegation, agents and the loop; 20–27 for demonstrations and coding agents; 29–38 for risk, responsibility and verification; 39 for the final assignment.
- [Course specification](../course-specification.pdf): PDF page 8 for Session 5 requirements.
