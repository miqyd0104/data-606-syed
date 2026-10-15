# Session 3 — Effective AI Use

[← AI Fundamentals](../README.md) · [Original slides](../slides/session-03-effective-ai-use.pdf) · [Previous: Understanding Modern AI](session-02-understanding-modern-ai.md) · [Next: AI for Automation](session-04-ai-for-automation.md)

This session turns the earlier model knowledge into working habits: give clear instructions, provide relevant evidence, assess the response and take responsibility for how it is used. The practical exercise is a team briefing prepared from supplied project information.

A polished prompt helps, but reliability also depends on the information available, the chosen tool and the checks applied afterwards.

## Behavioural traits to recognise

The slides discuss three behaviours that can make an AI assistant seem more reliable than it is.

| Trait | What it means in practice | Example | How to respond |
| --- | --- | --- | --- |
| **Sycophancy** | Agreeing with or flattering the user's position too readily. | Endorsing a weak project proposal because the user calls it excellent. | Ask for counter-evidence, weaknesses and alternatives; evaluate the actual evidence. |
| **Recency bias** | Giving disproportionate weight to recent information in a conversation. | Following a later casual suggestion while missing an earlier important requirement. | Keep authoritative constraints explicit and check that the final output satisfies them. |
| **Overconfidence** | Expressing more certainty than the available evidence supports. | Stating an uncertain delivery date as a confirmed commitment. | Request sources and separate facts, assumptions and unresolved questions. |

These are tendencies to watch for, not a claim that every model always behaves this way. Models can be trained to improve helpfulness and confidence calibration, but a confident tone is still not independent evidence.

### Helpful does not always mean accurate

A response can be friendly, relevant-looking and wrong. If I suggest an answer in my question, agreement may reflect the framing rather than a careful assessment of competing evidence.

For example, “This project is clearly on track; write an update” encourages a different response from “Assess the project against the milestones, identify contradictory evidence and state what remains uncertain.” The second prompt makes the checking task explicit, but I still need to review the result.

### Recent information versus authoritative information

A later message is not automatically more authoritative than an approved policy or signed decision. Where sources conflict, consider date, author, status and scope. A recent informal note might identify a new concern without formally changing the agreed deadline.

The slides mention research on calibrating model confidence. The useful learning point is that confidence should align with actual reliability; it is not a guarantee that a particular assistant knows when it is wrong.

## The six-part prompting framework

The complete diagram on PDF page 20 contains four prompt components followed by two review steps.

| Part | Question to answer | Example for a project briefing |
| --- | --- | --- |
| **Persona** | What perspective or role is useful? | A business analyst writing for a project director. |
| **Task** | What specific outcome is required? | Produce a concise meeting brief. |
| **Context** | What information should inform the work? | The project overview, latest status, meeting notes and risk register. |
| **Constraints** | What boundaries and format apply? | One page; identify three key risks; cite sources; do not invent dates. |
| **Evaluate** | Does the output meet the objective? | Check each claim, decision and action against the evidence. |
| **Iterate** | What needs to change? | Correct a misunderstood risk or provide a missing source, then review again. |

A persona sets a perspective or writing style; it does not give the model professional qualifications or access to facts it has not been given. A specific task and usable evidence are usually more valuable than a long role description.

### A basic prompt and a more useful prompt

“Explain recursion” leaves the audience, depth and purpose unspecified. A clearer version is:

```text
Explain recursion to a beginner learning Python.
Use plain language and one small example.
Explain the base case and how each call moves towards it.
Keep the explanation under 200 words.
Finish with one question that checks my understanding.
```

This is an illustrative prompt, not an instruction to execute an exercise here. The evaluation should check the substance: a recursive example without a valid stopping condition is still poor even if it follows the requested word count.

## From prompt engineering to context engineering

**Prompt engineering** concerns the instructions and examples used to guide a model. **Context engineering** concerns the wider information environment made available for the task.

The slides show a progression:

1. **Prompt crafting:** state the task, audience, examples and constraints.
2. **Iteration:** inspect the response and refine what is missing or wrong.
3. **Prompt chaining:** split a complex task into stages with intermediate outputs.
4. **Context engineering:** deliberately select and manage documents, tools, history, rules and other relevant information.

These approaches work together. A stronger information environment does not remove the need for clear instructions, and multiple prompts are not automatically better than one well-scoped request.

### What belongs in context?

For a client reply, useful context might include the original email, relevant previous correspondence, approved project facts and the organisation's tone guidance. Unrelated emails, private personnel information and old drafts can add noise or unnecessary exposure.

| Context choice | Why it helps |
| --- | --- |
| Use the relevant approved version | Reduces accidental reliance on an obsolete document. |
| Label sources with names, dates and status | Makes conflicting claims easier to investigate. |
| Include the passages needed for the question | Keeps the task focused and reduces irrelevant material. |
| Keep source content distinct from instructions | Prevents a quoted document from silently changing the task. |
| Specify what to do when evidence is absent | Encourages an explicit gap instead of an invented answer. |

For a long or complex task, check intermediate outputs before building on them. If a first-stage extraction invents a milestone, later drafting can make that mistake more polished without making it more accurate.

## Team exercise: a project briefing

The course exercise allows about 20 minutes for preparation, followed by demonstration and review. The task is to brief a meeting using the supplied project information. The slide example includes milestones, three major risks, decisions needed and matters requiring escalation.

The project pack itself is not among the supplied files, so these notes provide a method and prompt template rather than fabricated project facts or a completed briefing.

### Suggested working method

1. Read the task and identify the intended audience and decision.
2. Select the project overview, latest status, relevant meeting notes and risk register.
3. Check dates and source authority; mark conflicts or missing information.
4. Request a concise brief with references beside important claims.
5. Compare the result with the source material and correct unsupported statements.
6. Prepare to explain why the chosen context was sufficient and what was deliberately excluded.

### Reusable briefing prompt

```text
Act as a business analyst preparing a briefing for a project director.

Task:
Draft a one-page brief for the next project meeting.
Include current status, key milestones, the three most important risks,
decisions required, and actions with owners and dates where supplied.

Sources:
Use only the attached project overview, status report, meeting notes
and risk register. Identify the source and date for important claims.

Constraints:
Separate confirmed facts, assumptions and unresolved questions.
When sources disagree, describe the conflict and their dates/status.
Do not invent a deadline, owner, decision or risk rating.
Mark absent information as "not provided".
Exclude personal or confidential details unnecessary for this audience.

Output:
Use short sections that a director can scan before the meeting.
Finish with the questions that need human clarification.
```

### How to evaluate the brief

Check factual correctness before tone. For each risk, confirm the event, consequence and current status. For each action, check the owner and deadline. A proposed action should not be presented as already agreed.

Then assess whether the brief helps the meeting: are the decisions clear, is the most important uncertainty visible, and can the reader follow the references? A shorter answer is not better if it removes a crucial qualification.

## Responsible use in everyday work

### Personal data and confidentiality

Use tools approved for the task and information involved. Share only the information needed, and consider who can access it, how it is retained and whether organisational or client requirements allow that use.

Paying for a product or seeing “enterprise” in its name does not by itself authorise uploading confidential material. A promise that inputs are not used for model training is also different from a promise of no storage, no logging or no access by others.

Removing names may reduce exposure but does not always remove identifying information. A combination of role, location and incident details can still identify someone. Use synthetic examples when real records are unnecessary, and follow the organisation's handling process for actual sensitive material.

Confidentiality includes more than personal data: internal plans, client information, source code, credentials and commercially sensitive documents also need appropriate handling.

### Environmental impact

AI training and inference use computing resources and electricity. Data-centre operation can involve cooling water, and electricity generation can have additional environmental effects. The impact varies by infrastructure, location, model and workload.

The slides discuss forecasts and provider initiatives. Those are time-sensitive examples, not universal per-request measurements. Practical habits include choosing a proportionate tool, avoiding unnecessary large generations and reusing useful outputs rather than repeatedly producing material with no purpose.

### Human-in-the-loop oversight

**Human-in-the-loop** means a person has a meaningful role in reviewing or deciding at an appropriate point. Merely being present while a system runs is not enough.

For a client email, review can occur before sending. For an extraction task, a person may examine ambiguous records. The reviewer needs the source evidence, enough time and authority to reject or correct the result.

Review during day-to-day operation is distinct from human feedback used to train a model. They address different parts of the system.

## Choosing a model or tool

The slides compare products across several tasks. The transferable skill is matching capabilities to needs, rather than memorising which provider appears next to each task.

| Task | Capability to prioritise | Verification to retain |
| --- | --- | --- |
| Draft a routine email | Appropriate tone, concise instructions and approved data handling. | Check names, facts, commitments and recipients before sending. |
| Brainstorm slogans | Variation and suitability for the audience. | Review originality, meaning and brand fit. |
| Summarise a transcript | Sufficient context and reliable source extraction. | Check decisions, speaker attribution, actions and omissions. |
| Prepare a project brief | Ability to combine and distinguish multiple sources. | Trace status, dates and risks to the source pack. |
| Analyse a complex specialist document | Appropriate domain support and handling of long evidence. | Qualified human review of consequential interpretations. |
| Work on a codebase | Repository access, tool support and executable feedback. | Review changes and run meaningful tests. |
| Answer questions over documents | Good retrieval, permissions and source references. | Confirm that the cited passages support the answer. |

Consider accuracy on representative tasks, latency, privacy requirements, cost and the effort of checking and correcting the result. A larger model is not automatically the best choice, and a cheaper response is not economical if it creates substantial rework.

## The AI Fluency 4Ds

The course uses **Delegation, Description, Discernment and Diligence**. They connect choosing the work, specifying it, evaluating it and taking responsibility. See the [AI Fluency terminology guide](https://www-cdn.anthropic.com/4396730ed190e691a3712cf2fd6bfe35509deca2.pdf).

| Competency | Question to ask | Project-briefing example |
| --- | --- | --- |
| **Delegation** | Which work is suitable for AI, and which decisions stay with me? | Delegate drafting; retain judgement about escalation. |
| **Description** | Have I explained the desired result, context and boundaries? | Specify audience, sources, sections and missing-data handling. |
| **Discernment** | Is the output useful, supported and appropriate? | Check every milestone and risk against the pack. |
| **Diligence** | Am I using the system responsibly and owning the result? | Protect information, disclose AI involvement where required and stand behind the final brief. |

Submitting an unread AI report fails responsible ownership even if the prompt was excellent. Brainstorming with AI and choosing, checking and developing the final idea can be an appropriate division of work.

## Coursework and questions to check understanding

The team briefing is reviewed against relevance, verification, proportionate context and exclusion of sensitive information. Retain the briefing and a short account of how it was checked; these notes do not record a completed submission.

1. Which two parts of the six-part framework happen after generating a response?
2. Why is adding every available document not automatically better context?
3. What is the difference between discernment and diligence?
4. Does a newer source always override an older one?
5. What would meaningful human review of a client email involve?

**Suggested answers:** 1. Evaluate and iterate. 2. Irrelevance, conflicts and unnecessary sensitive details can make the task worse. 3. Discernment assesses the output; diligence concerns responsible practice and ownership. 4. No; authority, approval status and scope also matter. 5. Checking evidence, commitments and recipients, with the ability to amend or stop sending.

## Source guide

- [Session 3 slides](../slides/session-03-effective-ai-use.pdf): PDF pages 4–9 for behavioural traits; 11–28 for prompting and context; 29–35 for the briefing exercise; 36–42 for responsible use; 43–61 for tool selection; 62–68 for the 4Ds and scenarios.
- [Course specification](../course-specification.pdf): PDF page 6.
