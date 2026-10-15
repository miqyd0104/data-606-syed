# Session 2 — Understanding Modern AI

[← AI Fundamentals](../README.md) · [Original slides](../slides/session-02-understanding-modern-ai.pdf) · [Previous: Demystifying AI](session-01-demystifying-ai.md) · [Next: Effective AI Use](session-03-effective-ai-use.md)

This session explains how large language models generate responses, how inference settings change their behaviour and why their output needs checking. It also introduces retrieval-augmented generation, or RAG, as a way to give a model relevant evidence at the time of a request.

The central idea is that **generating plausible language and establishing truth are different tasks**. A clear, confident answer may still contain a wrong calculation, invented source or unsupported conclusion.

## What is a large language model?

A **large language model (LLM)** is a language model trained at substantial scale to model patterns in token sequences. “Large” concerns model scale as well as training data; it does not simply mean a large collection of stored documents.

LLMs can draft, summarise, translate, explain and generate code. They can also produce useful factual answers, but that does not make every answer a verified retrieval from an authoritative database.

The training-data illustration includes books, websites, code and other sources. Actual training mixtures vary, and a diagram of possible sources does not establish exactly what a particular model was trained on.

### Text models and multimodal models

A text model works with text representations. A **multimodal** model can process more than one kind of input or output, such as text, images or audio.

Input and output support are separate questions. A model that accepts an image and describes it in text does not necessarily generate images. Check the capability needed for the task rather than assuming “multimodal” means every format is supported.

## From a prompt to a response

The slides present the following simplified path:

```text
Prompt and available context
    ↓ tokenisation
Token IDs
    ↓ embeddings and positional information
Numerical representations
    ↓ transformer layers
Context-sensitive representations
    ↓ output scores and decoding
Next token
    ↓ repeat with the generated token included
Response
```

This explains autoregressive text generation, the main process used in the walkthrough. It is a teaching model, not a specification of every possible AI architecture.

### 1. Tokenisation

A **token** is a unit used by a model's tokenizer. It might represent a whole word, part of a word, punctuation or another piece of text. Tokenisation depends on the tokenizer, so one word is not always one token and the same text can be split differently by different models.

For example, a prompt about the capital of France is converted to a sequence of token identifiers. The identifiers are lookup numbers, not definitions of the words. The token splits in the slides are illustrations rather than a universal tokenizer output.

Tokenisation helps explain why a language model may struggle with exact character operations. “Business” contains three `s` characters, but the model may represent the word as larger pieces rather than inspecting each letter. Asking it to spell the word out can help; using an actual character-counting operation is more dependable for an exact count.

### 2. Embeddings

An **embedding** is a numerical vector representing a token or other item. Learned representations allow relationships to be processed mathematically.

The small example vectors in the slides are illustrative. Real embeddings have many dimensions, and individual dimensions are not generally simple labels such as “country” or “capital”. Positional information also matters because word order changes meaning.

### 3. Transformer layers

**Attention** lets the model combine information from relevant positions in the sequence. For example, the representation of a pronoun can be influenced by the noun it refers to. This is more general than spotting keywords.

Feedforward components apply learned transformations to the representations. They do not literally rewrite the prompt into a clearer English sentence. Repeated layers build contextual information used to predict what comes next. The original [Transformer paper](https://arxiv.org/abs/1706.03762) explains attention and position-wise feedforward layers as the core components.

### 4. Next-token probabilities and decoding

The model produces scores for possible next tokens. A decoding procedure turns those scores into a choice. With **greedy decoding**, the highest-probability token is selected at each step; with sampling, a token is selected from a probability distribution.

The selected token becomes part of the context for the next step. This repeats until a stopping condition or output limit is reached.

The capital-of-France and “Sparta. Think…” examples illustrate this loop. Their percentages are teaching examples, not measured probabilities for a named deployed model.

A high probability for a token means the continuation fits the model's learned distribution in that context. It is not a certified probability that the whole answer is factually correct.

## Four inference parameters

These settings affect generation during inference; they do not retrain the model. Support and allowed ranges vary by model and service, and some interfaces do not expose them.

| Parameter | What it changes | Practical effect | What it does not guarantee |
| --- | --- | --- | --- |
| **Temperature** | How concentrated the token probability distribution is before sampling. | Lower values usually make common continuations more dominant; higher values allow more variation. | Truth, originality or reproducibility in every deployment. |
| **Top-k** | Restricts consideration to the highest-scoring `k` token candidates. | Limits how many candidates remain available. | That the retained candidates are factually valid. |
| **Top-p** | Keeps a set of likely tokens whose cumulative probability reaches a chosen threshold. | The number of eligible candidates adapts to the distribution. | A fixed number of candidates. |
| **Presence penalty** | Penalises tokens that have already appeared, where supported. | Can discourage repetition and encourage different wording. | A reliable understanding of whether an idea has been repeated. |

### Worked sampling example

Suppose the next-token probabilities are A: 0.50, B: 0.30, C: 0.15 and D: 0.05.

- With **top-k = 2**, A and B remain.
- With **top-p = 0.80**, A and B reach the threshold together.
- With **top-p = 0.90**, C is also needed, taking the cumulative probability to 0.95.

This is a simplified illustration; the retained distribution is normally renormalised for sampling. Combining settings can complicate interpretation, which is why a learning experiment should change one setting at a time.

For a structured extraction task, variation may be undesirable. For brainstorming, varied candidates may be useful. Neither preference removes the need to evaluate the output. A low-temperature model can consistently give the same wrong answer.

## Open and closed models

The slides compare how much control different model arrangements expose. Keep these distinctions separate:

- **Open weights:** model parameter files are available under stated terms.
- **Open source:** a broader licensing and openness question; available weights alone do not establish that all code, training data or usage rights are open.
- **Hosted API:** a service provides model access without necessarily exposing weights.
- **Self-hosting:** an organisation operates the model on its own infrastructure.

Open weights can enable more operational control, but running the model adds hardware and maintenance responsibilities. A closed model service can still expose inference settings or some customisation. Inspect the actual service and licence rather than assuming all open or closed systems behave alike.

## Common failure modes and what to do about them

| Failure mode | What it can look like | Useful response |
| --- | --- | --- |
| **Hallucination** | Invented facts, references, quotes or URLs. | Check material claims against original evidence; allow “not found” instead of demanding an answer. |
| **Poor or outdated information** | An old policy presented as current. | Supply authoritative current material and check dates and scope. |
| **Bias** | Uneven or stereotyped responses across groups or circumstances. | Review representative examples, question assumptions and assess the actual impact. |
| **Entity confusion** | Facts about one person or organisation assigned to another with a similar name. | Verify identity using multiple distinguishing details and primary sources. |
| **Tokenisation limitations** | Wrong letter counts or unreliable exact string manipulation. | Use deterministic tools for counting, comparison and calculation. |
| **Context limitations** | Earlier requirements missed or relevant evidence omitted. | Select and organise relevant material; restate key constraints and check coverage. |
| **Model collapse during training** | Loss of quality or diversity under certain repeated synthetic-data training setups. | Manage training-data provenance, diversity, quality and evaluation. |

Risk is not confined to open models. Training data, the prompt, retrieved documents and the surrounding application can all introduce mistakes.

### A fabricated citation can look convincing

A plausible title, author and web address can be generated from patterns. Verification means opening the source, checking that it exists and confirming that it supports the specific claim. A real page can still be irrelevant or contradict the summary.

For high-impact decisions, the amount and independence of checking should match the consequences. Asking the same model “are you sure?” is a weak substitute for external evidence.

### Context windows

The **context window** is a model's limit on the token sequence it can process. Instructions, conversation history, supplied material and tool results can occupy context; input/output allocation depends on the model and service.

More capacity does not guarantee that every detail will be used correctly. A large pile of irrelevant files can obscure the few facts that matter. Keep source names, dates and authority clear, and separate a task instruction from text quoted inside a source document.

### Model collapse: a specific research concern

The deck describes model collapse as hypothetical. Research has demonstrated degradation in particular settings where models are repeatedly trained on recursively generated data, including loss of parts of the original distribution. This does **not** establish that all synthetic data is harmful or that every deployed model is collapsing. See [Shumailov and colleagues' Nature paper](https://www.nature.com/articles/s41586-024-07566-y).

The “dead internet” idea mentioned alongside it is a separate, much broader claim. It is not evidence of the behaviour of a specific model or website.

## Retrieval-augmented generation (RAG)

RAG supplies relevant retrieved material as context for a generated answer. It separates obtaining evidence from writing a response using that evidence. The original [RAG paper](https://arxiv.org/abs/2005.11401) combines a learned generative model with external retrieval.

```text
Question
    ↓
Retrieve relevant authorised documents or passages
    ↓
Provide the question and retrieved evidence to the model
    ↓
Generate an answer grounded in that evidence
    ↓
Check the answer and its source references
```

For example, a staff-policy assistant could retrieve the relevant passage from the current approved policy before answering. This can provide information absent from the model's training and make claims easier to trace.

RAG does not normally update the model's weights. It can fail if retrieval misses the right passage, finds an obsolete version or provides material the model misinterprets. Access controls still matter, and a document's contents should be treated as evidence rather than authority to change the user's instructions.

### Choose a mitigation for the actual problem

If the problem is an outdated policy, good retrieval may help. If the task is exact arithmetic, a calculator is more appropriate. If the task is ambiguous, clarification may be needed. Changing temperature is not a universal solution to these different problems.

## Coursework: choose one route

The supplied materials offer **either** a documented inference-parameter experiment **or** a written case analysis of a real AI failure.

### Option A — Parameter experiment

The slide specifically asks for modifying and testing inference parameters using an **OpenAI API key**, documenting each change with comments and supplying a sample output showing its effect. Record the model/interface, prompt, settings changed and actual outputs. Compare the effect of each change. A useful experimental structure is:

1. Choose a fixed prompt and baseline settings.
2. Change one supported parameter while holding other conditions steady.
3. Run repeated trials to distinguish a pattern from a single chance output.
4. Save the responses and evaluate variation, relevance, repetition and correctness.
5. State what the small experiment can and cannot establish.

The slides include a temperature demonstration using an API client. They do not provide actual results for these notes, so no experiment is claimed as completed. Keep any credentials outside saved notebooks, screenshots and repository files.

### Option B — AI failure analysis

Choose a documented real-world incident and explain what went wrong, the cause, the harm and a suitable mitigation. The slide specifies at least four sentences. Use sources to distinguish established facts from possible explanations, and avoid inventing an incident to satisfy the format.

## Questions to check understanding

1. Is a token always a whole word?
2. Does a low temperature make an answer true?
3. How does top-p differ from top-k?
4. Does RAG retrain the model every time a document is retrieved?
5. Why can an answer with a genuine URL still be unreliable?
6. Which tool would best check an exact character count?

**Suggested answers:** 1. No. 2. No; it changes sampling behaviour. 3. Top-p uses cumulative probability, while top-k fixes the number of candidates. 4. Normally no; it supplies context. 5. The source might not support the claim or might be outdated. 6. A deterministic string operation or equivalent counting tool.

## Source guide

- [Session 2 slides](../slides/session-02-understanding-modern-ai.pdf): PDF pages 4–29 for LLMs and generation; 31–40 for inference settings and the demo; 44–63 for limitations and mitigations; 64 for coursework.
- [Course specification](../course-specification.pdf): PDF page 5.
- External links beside the relevant explanations clarify transformers, RAG and the research status of model collapse.
