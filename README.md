# E2-Generating-and-Cleaning-a-Restricted-Context-Free-Grammar

## Description

For this project, i have chose **Latin** as the target language for grammar generation and analysis.

Latin is a classical language belongs to the Italic branch of the Indo-European languages. It was spoken in the Roman Republic and the Roman Empire, and it remains highly influential in modern languages, law, science, and theology. Despite being considered a "dead language" meaning it no longer has native speakers, Latin is still actively seen, studied and used in academic, ecclesiastical, and legal contexts.

For the scope of this project, we will focus on modeling a **subset of Latin phrases** with a simplified structure:
- Basic noun phrases (e.g., *"Puella amat" — "The girl loves"*)
- Simple subject-verb-object constructions
- Consistent use of singular nominative and accusative cases

This restricted subset allows to define a manageable grammar that captures the essence of Latin sentence construction, while remaining simple enough for syntactic analysis, grammar transformations, and parsing tests.

My objective is to develop a formal grammar that can generate and validate simple Latin sentences based on this structure, and progressively refine it to remove ambiguity and left recursion.

## Model of the Solution

The grammar that recognizes the language is the following:

S → NP VP
NP → P
VP → V NP
P → puella | puer | vir | femina
V → amat | videt | audit | laudat
N → librum | puellam | puerum | feminam


Where:

- **S** (Sentence): Represents the entire sentence.
- **NP** (Noun Phrase): Represents the subject or object and consists of a Pronoun.
- **VP** (Verb Phrase): Represents the action performed by the subject over an object and consists of a Verb followed by a Noun Phrase.
- **P** (Pronoun/Noun acting as subject): Includes simple Latin nominative forms.
- **V** (Verb): Includes basic present tense verbs.
- **N** (Noun): Represents the object, in accusative case.

This structure ensures that the grammar is **context-free** and **suitable for LL(1) parsing** after eliminating ambiguity and left recursion.

---

### Example of the syntactic tree for the sentence:

> **"puella amat puerum"**

The corresponding syntactic tree is:
![Syntax Tree Example](Tree.png)

## Elimination of Ambiguity

The grammar I designed for recognizing simple Latin sentences is free of ambiguity. Each sentence structure (subject-verb-object) produces exactly one syntactic tree, ensuring a single clear interpretation.

For example, the sentence **"puella amat puerum"** ("the girl loves the boy") can only be parsed in one way: 
- "puella" is the subject (NP → P).
- "amat" is the verb (V).
- "puerum" is the object (NP → N).

Since there are no alternative ways to group the words, there are no multiple derivations, and thus, no ambiguity is present in the grammar.

---

## Elimination of Left Recursion

The original grammar also did not contain left recursion. In all production rules, the first symbol derived is different from the non-terminal being defined, which prevents left-recursive loops.

For example:
- **S → NP VP** starts with a noun phrase (NP).
- **VP → V NP** starts with a verb (V).
- **NP → P** starts with a pronoun (P).

There is no case where a non-terminal directly calls itself as the first element, ensuring that the grammar is suitable for LL(1) parsing techniques without modifications.

---

## Implementation

For the implementation, I used **Python** and the **Natural Language Toolkit (NLTK)** library to define the grammar and parse Latin sentences.

First, I created a **Context-Free Grammar (CFG)** using `nltk.CFG.fromstring()`. The grammar defines simple Latin sentences with a subject-verb-object structure. Subjects can be pronouns or nouns, verbs are simple present tense actions, and objects are nouns.

Here is the main structure of the grammar:

- **S** → NP VP
- **NP** → P | N
- **VP** → V NP
- **P** → ego | tu | ille | illa | nos | vos | illi
- **V** → edit | bibit | amat | videt
- **N** → puella | puerum | panem | aquam | pila | pelliculam

I used a `ChartParser` from NLTK to parse input sentences based on this grammar.  
The testing function `test_sentence()` takes a sentence as input, splits it into words, and tries to parse it. If the parser produces at least one valid parse tree, the sentence is considered **accepted**; otherwise, it is **rejected**.

---

## Tests

I created two sets of test sentences: **valid sentences** that should be accepted by the grammar, and **invalid sentences** that should be rejected.

### Valid Sentences
These sentences strictly follow the grammar's structure:

- `"ego edit panem"` (I eat bread)
- `"illa videt pelliculam"` (She sees the movie)
- `"puella amat puerum"` (The girl loves the boy)
- `"nos bibit aquam"` (We drink water)

All valid sentences were **accepted** by the parser:

'ego edit panem': Accepted 'illa videt pelliculam': Accepted 'puella amat puerum': Accepted 'nos bibit aquam': Accepted


### Invalid Sentences
These sentences were designed to break the grammar rules, either by incorrect word order or improper structure:

- `"ille panem bibit"`
- `"vos panem edit"`
- `"illi pelliculam videt"`
- `"puella puerum amat"`

All invalid sentences were correctly **rejected**:

'ille panem bibit': Rejected 'vos panem edit': Rejected 'illi pelliculam videt': Rejected 'puella puerum amat': Rejected

## Example of Pushdown Automaton (PDA)

To better illustrate how the grammar recognizes a valid Latin sentence, here is a simplified example of how a Pushdown Automaton (PDA) would parse the sentence **"illa videt pelliculam"**:

### Initial setup:
- The stack initially contains the start symbol `S`.
- The input string is `"illa videt pelliculam"`.

### PDA transitions:

| Step | Stack                | Input                     | Action |
|:----:|:---------------------|:--------------------------|:-------|
| 1    | S                    | illa videt pelliculam     | Expand `S → NP VP` |
| 2    | VP NP                 | illa videt pelliculam     | Expand `NP → P` |
| 3    | VP P                  | illa videt pelliculam     | Match `P → illa` |
| 4    | VP                    | videt pelliculam          | Expand `VP → V NP` |
| 5    | NP V                  | videt pelliculam          | Match `V → videt` |
| 6    | NP                    | pelliculam                | Expand `NP → N` |
| 7    | N                     | pelliculam                | Match `N → pelliculam` |
| 8    | (empty)               | (empty)                   | Accept |

### Explanation:
- At each step, the PDA uses the top of the stack and the current input symbol to decide whether to expand a rule or match a terminal.
- After consuming all input symbols and emptying the stack, the sentence is accepted as valid according to the grammar.

This example confirms that the grammar is suitable for parsing using a context-free automaton like a PDA.



