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

