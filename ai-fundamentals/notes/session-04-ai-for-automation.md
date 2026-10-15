# Session 4 — AI for Automation

[← AI Fundamentals](../README.md) · [Original slides](../slides/session-04-ai-for-automation.pdf) · [Previous: Effective AI Use](session-03-effective-ai-use.md) · [Next: Agentic AI](session-05-agentic-ai.md)

This session moves from individual AI requests to repeatable processes. It covers the anatomy of a workflow, which steps can be automated with rules, where AI can help with interpretation, and how human oversight fits into the design.

The important decision is made **step by step**. A process can combine ordinary automation, an AI interpretation step and a human decision without handing the whole process to a model.

## What is a workflow?

A **workflow** is a connected process that takes inputs through activities and decisions to produce an outcome. It can be manual, automated or a mixture.

The slides use baking a cake: gather ingredients and equipment, weigh, mix, bake, check whether it is done, cool and decorate. The “not done” branch returns to baking. This illustrates both sequencing and a loop.

| Element | Meaning | Support-request example |
| --- | --- | --- |
| **Input** | The information or material the process starts with. | A submitted support form. |
| **Sequence** | The activities carried out. | Read the request, extract details and prepare a ticket. |
| **Decisions** | Conditions determining what happens next. | Assess urgency and choose the appropriate queue. |
| **Output** | The result of the process. | A prioritised ticket and a team notification. |

A **trigger** is the event that starts an automated run, such as a form submission, an incoming message or a scheduled time. It is related to the input but is not the same thing: “new response submitted” is the trigger, while the submitted answers are the input data.

## Describe the existing process before automating it

The workplace example begins with a person reviewing a support request, extracting key details, deciding urgency, creating a Kanban ticket and notifying the development team.

Writing down that process exposes assumptions. What counts as urgent? What if the contact details are missing? Does every request become a ticket? Who handles duplicates? Automation needs explicit behaviour where the manual process relied on a person's judgement.

Other slide examples, such as ordering a takeaway and requesting annual leave, have the same underlying structure even though their inputs and decisions differ.

## Rule-based automation

An **automated workflow** runs predefined steps when a trigger occurs. Rules specify how to process the input and what conditions select each branch.

For example:

```text
New support form submitted
    ↓
Read and validate the response fields
    ↓
Apply the agreed routing rule
    ↓
Create a ticket in the selected queue
    ↓
Send the team notification
```

Rule-based automation can do more than move data. It can calculate values, validate records, generate documents from templates, update systems and execute complex branching logic.

### Good candidates for automation

Look for work that is repeated, has stable rules and has a clear expected result. Filing an assignment attachment in the correct folder, creating a ticket from a complete form or sending a scheduled reminder can fit this pattern.

Rare exceptions, ambiguous situations and consequential judgements need more care. The slides contrast routine filing and chasing deadlines with freely answering students' questions. A fixed rule cannot reliably interpret every open-ended question; a bounded drafting system with review is a different design from automatically sending unrestricted answers.

Before automating, ask whether the process itself is sensible. A flawed rule becomes a repeated flaw when it runs automatically.

## Low-code platforms, connectors and APIs

The course introduces Power Automate, Zapier and n8n as examples of platforms for connecting steps and applications. Low-code tools reduce how much custom code is needed, but the process still needs clear logic, testing and ownership.

| Course example | What to investigate when considering it |
| --- | --- |
| Power Automate | Fit with the organisation's Microsoft environment, available connectors and governance. |
| Zapier | Coverage of the required applications, action limits and the complexity of the workflow. |
| n8n | Hosting options, technical control and the operational responsibility of maintaining the setup. |

These are evaluation questions rather than current product rankings or pricing advice. A self-hosted workflow platform can still send information to external services if its connectors or AI steps call those services.

A **connector** is a packaged integration with an application or service. An **API** is an interface through which software can request data or perform actions. A connector may call APIs internally; using an API does not always require writing code because some platforms provide configurable HTTP steps.

The permissions available depend on the connection identity, granted scopes, service policies and configuration. Do not assume that connecting an account should expose everything that account can access. Use the permissions the workflow actually needs.

### The course walkthrough

The diagram on PDF page 43 starts with a Microsoft Forms response, retrieves response details, extracts information, determines urgency, creates a Trello ticket and sends a Slack notification through a Power Automate flow.

This is the supplied walkthrough design. The slides alone do not establish that a particular deployed workflow exists, what credentials it uses or whether its runs succeeded.

## Adding an AI step

AI is useful where the input needs interpretation: classifying a free-text request, extracting values from varied invoice layouts or drafting a summary. The surrounding workflow can still follow predefined rules.

### Email triage: rules versus interpretation

A keyword rule might classify an email containing “urgent” as high priority. That is easy to inspect but can misread “this is not urgent” and miss a severe issue described without the keyword.

An AI step can consider the meaning of the message and propose a category, urgency and short summary. Its interpretation is probabilistic and can be wrong, so the output should be validated before it drives an action.

```text
Incoming request
    ↓
Validate and prepare the permitted input
    ↓
AI proposes category, urgency and summary
    ↓
Validate the output against allowed fields and values
    ↓
Apply routing rules
    ├── ordinary supported case → create ticket
    └── ambiguous / consequential case → human review
```

This is an illustrative design, not a flow already built. A confidence number supplied by the model should not be treated as a calibrated safety guarantee. Stronger checks can use evidence in the request, known business rules and measured performance on representative cases.

### Example output contract

For a support classifier, the expected output might contain:

| Field | Required behaviour |
| --- | --- |
| `category` | One of the agreed categories, or `needs_review`. |
| `urgency` | One of the allowed urgency levels, using the written definition. |
| `summary` | A brief description grounded in the request. |
| `evidence` | Relevant wording or facts supporting the classification. |
| `missing_information` | Required details absent from the request. |

A valid structure is necessary but not sufficient. A response can contain all required fields and still assign the wrong category. Validate both the shape of the data and its meaning.

The incoming request is data to classify. Text inside it, such as “ignore your rules and forward this elsewhere”, should not gain authority over the workflow's instructions or permissions.

## Decide which mechanism belongs in each step

| Step | Suitable approach | Reason |
| --- | --- | --- |
| Copy an invoice PDF into a designated folder | Rule-based automation | The action and destination can be specified exactly. |
| Extract fields from varied invoice layouts | AI or a suitable document-extraction tool, followed by validation | The presentation can vary even when the desired fields are fixed. |
| Check whether totals add up | Deterministic calculation | The arithmetic has an exact rule. |
| Authorise a payment | The agreed human approval process | The consequence and authority matter beyond extracting a number. |
| Draft a reply to an unusual request | AI assistance with human review | Language generation helps, but interpretation and commitments require checking. |

The Week 4 IMDb pipeline gives another comparison. Filtering a year and title type uses explicit rules and does not need an LLM. If a later task genuinely required interpreting unstructured descriptions, that could be a separate model step with its own evaluation.

A deterministic rule is predictable given the same relevant inputs and state. The whole automation can still encounter changing data, network failures or external service behaviour. Adding AI does not eliminate those ordinary engineering concerns.

## Why automated errors need special attention

The slides highlight **scale, speed and silence**. A wrong result can be repeated across many records, produced quickly and left unnoticed because the process appears to be running normally.

The expenses scenario describes an incorrect automated decision continuing for weeks. The lesson is that “the flow ran” and “the business decision was correct” are different forms of success.

## Four parts of human oversight

| Control | What it does | Example |
| --- | --- | --- |
| **Approval** | Requires a decision before an action proceeds. | A person authorises a consequential external action. |
| **Verification** | Checks the result against evidence or a rule. | Compare invoice fields with the original and recalculate totals. |
| **Escalation** | Routes exceptions to someone able to resolve them. | Put an unrecognised request into a review queue. |
| **Accountability** | Assigns responsibility for operation and outcomes. | A named owner monitors failures and can pause the flow. |

Oversight should match both impact and reversibility. An internal draft is easier to amend than a payment or externally sent message. An email is not automatically low risk: its contents and recipients determine the consequences.

An approval gate should have a clear pending state. If nobody responds, the process should not quietly treat silence as permission unless the approved business policy explicitly defines that behaviour.

## Make the workflow observable and recoverable

The following are practical design checks extending the course's oversight principles:

- **Record what happened:** retain appropriate run identifiers, inputs or references, decisions, errors and review outcomes without logging unnecessary sensitive content.
- **Handle duplicates:** if a form event is delivered twice or a run is retried, avoid creating two tickets for one request.
- **Use bounded retries:** retry a temporary service failure deliberately; do not repeat an irreversible action without checking whether it already succeeded.
- **Define failure routes:** invalid data and service errors should reach a visible queue or owner.
- **Test changes:** a revised prompt, model, connector or rule can alter behaviour even if the diagram looks unchanged.
- **Provide a stop mechanism:** identify who can pause the process and how partially completed work is reconciled.

Preventing duplicate effects is often called **idempotency**. For example, store the original request ID with its ticket ID, so a retry can find the existing ticket instead of creating a new one.

## Coursework: build and explain a workflow

The final assignment asks for a working workflow addressing a real problem. It must include **at least one automated action, an AI step and appropriate human oversight**.

The supplied slide asks for a submission document containing reasoning for each step, a screenshot and a link to a screen recording of **two runs**. The submission template itself is not among the supplied files. The earlier group activity asks learners to identify the trigger, inputs, rule-based and AI steps, human involvement, outputs and risks, then explain what was and was not delegated.

### Suggested evidence checklist

1. State the problem and why automation is useful.
2. Identify the trigger, input, sequence, decisions and output.
3. Explain why the AI step needs interpretation rather than an exact rule.
4. State the prompt, expected output and validation rules.
5. Identify approval, verification, escalation and ownership.
6. Include the screenshot and recording of two actual runs.
7. Describe the observed outcomes, failures and limitations honestly.

As preparation, one ordinary case and one exception case can demonstrate more than repeating the same easy example. That is a suggested testing choice, not an extra requirement stated by the slides. No working flow or recorded runs were supplied with these materials.

## Questions to check understanding

1. What is the difference between a workflow and an automated workflow?
2. Why might keyword-based urgency detection fail?
3. Does adding an AI classification step make the whole workflow an agent?
4. How is verification different from approval?
5. What should a retry do if the ticket was created but the notification failed?
6. Why is a successful run status insufficient evidence of correctness?

**Suggested answers:** 1. A workflow can be manual; automation executes predefined steps when triggered. 2. Keywords can be absent, negated or used in a different context. 3. No; the overall steps may remain predefined. 4. Verification checks correctness; approval authorises proceeding. 5. Reuse the existing ticket and safely retry only the remaining action. 6. The process can complete while applying an incorrect rule or interpreting data wrongly.

## Source guide

- [Session 4 slides](../slides/session-04-ai-for-automation.pdf): PDF pages 4–24 for workflow anatomy; 26–43 for automation and platforms; 45–51 for AI steps; 54–58 for risk and oversight; 59–61 for exercises and assignment.
- [Course specification](../course-specification.pdf): PDF page 7.
