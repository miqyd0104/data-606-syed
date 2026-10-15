# Session 1 — Demystifying AI

[← AI Fundamentals](../README.md) · [Original slides](../slides/session-01-demystifying-ai.pdf) · [Next: Understanding Modern AI](session-02-understanding-modern-ai.md)

This session introduces what AI means, how models learn from data and how a trained model makes predictions. The practical walkthrough uses a cat-versus-dog image classifier to connect the terminology to a complete training process.

The main distinction to understand is **training versus inference**: training changes what a model has learned; inference uses the trained model on an input.

## What counts as AI?

Artificial intelligence is the broad field of building systems that perform tasks involving capabilities such as perception, reasoning, learning or acting towards a goal. Examples include recognising objects in photographs, recommending music, detecting unusual transactions and generating text.

AI is broader than chatbots, and it is broader than systems that learn from data. A rule-based expert system can also count as AI. A system does not need human-level understanding to be useful at a specific task.

The terminology diagram on PDF page 11 places machine learning inside AI, deep learning inside machine learning, and the modern generative AI used in the course inside deep learning.

| Term | Meaning | Example |
| --- | --- | --- |
| **Artificial intelligence (AI)** | The broad field of machine capabilities such as reasoning, perception and learning. | An expert system applying specialist rules. |
| **Machine learning (ML)** | Learning patterns from examples instead of manually specifying every decision rule. | Predicting house prices from previous sales. |
| **Deep learning (DL)** | Machine learning using neural networks with multiple layers. | Recognising objects from image pixels. |
| **Generative AI** | Producing new content based on learned patterns. | Drafting text or generating an image from a description. |

The nested diagram is a useful picture of the modern systems covered here. More generally, “generative” describes what a model does; generative statistical models also existed before modern deep learning.

### Classification, prediction and generation

These describe different tasks:

- **Classification:** choose a category, such as cat or dog.
- **Regression:** predict a numerical value, such as a house price.
- **Generation:** produce content, such as a paragraph or image.

A classifier returning the label `cat` has not generated a new photograph of a cat. A chat interface can contain several kinds of capability, so the interface alone does not tell me which task the underlying system performs.

The slides contrast “traditional” task-specific AI with “modern” general-purpose AI. Treat those labels as course shorthand. Specialised models are still useful, and a general-purpose model is not automatically better at every narrow task.

## How machine learning differs from hand-written rules

For a rule-based house-price estimate, a programmer might explicitly add a fixed amount for each bedroom. In supervised machine learning, the developer provides historical house features and sale prices, chooses a model and trains it to reduce prediction error.

Humans still make important choices: the target, features, dataset, model, training procedure and evaluation method. “Learning from data” does not mean there is no programming or human judgement.

The slides introduce decision trees, neural networks and statistical models. These are examples rather than mutually exclusive categories: machine learning itself has strong statistical foundations, and not every ML model is a neural network.

## Neural networks: inputs, layers and weights

A neural network contains connected processing units arranged in layers. A unit combines numerical inputs using learned **weights**, usually adds a bias term, and applies an activation function. The network passes the resulting values through further layers to produce an output.

| Part | Role in an image classifier |
| --- | --- |
| Input | Numerical pixel values from the image. |
| Hidden layers | Transform the input into representations useful for the task. |
| Weights | Learned numerical values controlling how strongly signals contribute. |
| Output | Scores or probabilities for the possible categories. |

The “brain” comparison is an analogy. These systems are mathematical models; describing them as recognising patterns does not establish that they understand or experience the image as a person does.

### Common architectures

| Architecture | Core idea | Typical use discussed in the course |
| --- | --- | --- |
| Feedforward neural network (FNN) | Information moves from input through layers to output without recurrent connections. | Predictions from structured numerical features. |
| Convolutional neural network (CNN) | Filters detect local patterns and build increasingly useful representations. | Image classification. |
| Recurrent neural network (RNN) | A state carries information through a sequence. | Sequential data such as time series or text. |

These are typical uses, not exclusive rules. The best design depends on the data, task, performance requirements and resources. Session 2 introduces transformers, which are central to many language models.

### Architecture versus trained model

An **architecture** is the design: the kinds of layers, their connections and how information flows. A **trained model** combines a design with the parameter values learned during training.

Two models can use the same architecture but behave differently because they were trained on different data, with different objectives or settings. An architecture diagram by itself does not tell me the accuracy of a particular trained model.

## Three approaches to training

### Supervised learning

The training examples include target answers called **labels**. The model predicts an answer, compares it with the target and adjusts its parameters to reduce a loss measuring the error.

For house prices, features might include floor area and bedroom count, with sale price as the target. For the class demonstration, the image is the input and `cat` or `dog` is the target label.

Supervised learning covers both classification and regression. Labels need to be accurate and representative: an incorrectly labelled dog image teaches the wrong association.

### Unsupervised learning

The data does not provide a target label for each example. The model looks for structure, such as groups of similar items.

For example, music tracks can be grouped by their measured characteristics without being given genre labels. A person may then interpret a cluster as containing mostly similar styles. The cluster is not automatically an objectively correct genre classification.

### Reinforcement learning

An agent takes actions and receives rewards or penalties from an environment. The learning process aims to improve behaviour according to that reward signal over time.

The reward encodes what the designer values. If it rewards the wrong proxy, a system can perform well according to the score while failing the intended objective. A numerical reward does not mean the model feels pleased or disappointed.

These approaches can be combined across stages of a system's development; a finished product does not necessarily use only one.

## Training versus inference

| Training | Inference |
| --- | --- |
| Learns or updates parameter values. | Uses the current parameter values. |
| Needs a learning objective and training procedure. | Needs an input and a trained model. |
| Often processes many examples repeatedly. | Produces a prediction or generated response for the supplied input. |
| Example: learn from labelled cat and dog pictures. | Example: classify a new picture. |

An ordinary prediction does not automatically retrain the model. Similarly, putting information into a chatbot conversation can affect that conversation's response without changing the underlying model weights.

If performance becomes poor, first investigate why. Causes can include unsuitable inputs, a shift in real-world data, poor training examples or a task outside the model's scope. Retraining may help, but so might correcting preprocessing, supplying appropriate context or replacing an unsuitable model.

## Walkthrough: a cat-versus-dog classifier

The slides describe a Python demonstration using TensorFlow/Keras. They show the process and possible improvements; the supplied deck does not provide a complete project or measured final results to reproduce here.

### 1. Prepare and label the data

Collect images and associate each with the correct category. Separate cat and dog folders are one way a loading tool can infer labels from directory names.

The dataset should contain meaningful variation: different breeds, backgrounds, poses, lighting and image quality. If all cat pictures have white backgrounds and all dog pictures have grass, the model may learn the background shortcut instead of the animal features.

### 2. Separate learning from evaluation

| Dataset | Purpose |
| --- | --- |
| Training set | Used to update weights. |
| Validation set | Used during development to compare settings and detect problems. |
| Test set | Kept separate for a final evaluation after development decisions. |

The deck illustrates an 80% training split and a smaller held-back validation split. That percentage is an example, not a universal rule. A separate test set is a useful additional distinction because repeatedly choosing settings against validation results also adapts development to those examples.

Avoid **data leakage**: duplicate or near-identical images should not make the evaluation appear independent when they closely match training examples.

### 3. Pass images through the network

The diagram on PDF page 26 illustrates a progression from pixels to simple visual features, then shapes and textures, then larger object features, then cat/dog outputs.

```text
Image pixels
    ↓
Layers learn useful visual representations
    ↓
Output scores for cat and dog
    ↓
Predicted category
```

Labels such as “eyes” and “cat face” explain the intuition. They are not a promise that each hidden layer contains a neatly named, human-readable detector. The drawing is conceptual rather than a full implementation specification.

### 4. Train in batches over epochs

A **batch** is a group of examples processed together. An **epoch** normally means one pass through the training dataset; it contains multiple batches when the dataset is larger than a batch.

For each training batch, the network predicts outputs, computes a loss and updates weights. After suitable intervals, validation measures performance on held-back examples without using those examples to update the weights.

The slide's epoch diagram summarises these activities. Do not interpret it as “one batch equals one epoch” for every dataset.

### 5. Compare training and validation performance

**Accuracy** is the fraction of predictions with the correct label. If 90 of 100 held-back images are classified correctly, accuracy is 90%; this is an illustrative calculation, not the class model's recorded result.

High training accuracy with much lower validation accuracy can indicate **overfitting**: the model fits the training examples better than it generalises to new ones. If both are poor, investigate data quality, preprocessing, model capacity and training setup.

Accuracy alone can hide problems. A dataset with 95 dogs and 5 cats would allow an always-dog predictor to achieve 95% accuracy while recognising no cats. A **confusion matrix** separates correct and incorrect predictions for each category and makes that failure visible.

### 6. Improve and check again

The slides suggest brightness and contrast augmentation. **Data augmentation** creates varied versions of training images so the model is less dependent on incidental visual conditions.

Use changes that preserve the correct label. Augmentation does not repair incorrect labels, guarantee fairness or replace varied real examples. Evaluate improvements on held-back data instead of assuming that more training or more augmentation must help.

## Connection to the Python training

The preparation stage resembles an ETL pipeline: load inputs, transform them into a consistent representation, and pass them to the next stage. The difference is that a learned prediction replaces some explicitly coded decision logic.

I still need ordinary programming skills to handle paths, validate input, report errors and test the surrounding pipeline. A model cannot compensate reliably for loading the wrong file or attaching labels to the wrong records.

## Coursework and revision

The coursework is a **ten-question multiple-choice knowledge check** on terminology, training approaches and model behaviour. The questions and completed answers are not supplied in these slides.

Try answering these before checking the suggested answers:

1. Does every AI system use a neural network?
2. Is predicting a house price classification or regression?
3. What changes during training that normally stays fixed during inference?
4. What does a large gap between training and validation accuracy suggest?
5. Why might a model trained on many pictures still fail on a new background?
6. What is the difference between an epoch and a batch?

**Suggested answers:** 1. No; AI includes other approaches. 2. Regression. 3. Learned parameters such as weights. 4. Possible overfitting, though the data split and preprocessing also need checking. 5. It may have learned a shortcut or lack representative variation. 6. An epoch is a pass through the training set; a batch is a group processed together within that pass.

## Source guide

- [Session 1 slides](../slides/session-01-demystifying-ai.pdf): PDF pages 4–14 for terminology and applications; 15–23 for networks, training and inference; 25–33 for the classifier walkthrough; 34 for the knowledge check.
- [Course specification](../course-specification.pdf): PDF page 4 for the session objectives and assessment.
