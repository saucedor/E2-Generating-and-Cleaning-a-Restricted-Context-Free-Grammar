import nltk
from nltk import CFG

# Define grammar in Latin
grammar = CFG.fromstring("""
S -> NP VP
NP -> P | N
VP -> V NP
P -> 'ego' | 'tu' | 'ille' | 'illa' | 'nos' | 'vos' | 'illi'
V -> 'edit' | 'bibit' | 'amat' | 'videt'
N -> 'puella' | 'puerum' | 'panem' | 'aquam' | 'pila' | 'pelliculam'
""")

# Create parser
parser = nltk.ChartParser(grammar)

# Function to test sentences
def test_sentence(sentence):
    words = sentence.split()
    try:
        parses = list(parser.parse(words))
        return len(parses) > 0
    except ValueError:
        return False

# Test cases
valid_sentences = [
    "ego edit panem",
    "illa videt pelliculam",
    "puella amat puerum",
    "nos bibit aquam"
]

invalid_sentences = [
    "ille panem bibit",
    "vos panem edit",
    "illi pelliculam videt",
    "puella puerum amat"  # mal ordenada según esta gramática
]

# Run tests
print("Testing valid sentences:")
for sentence in valid_sentences:
    result = test_sentence(sentence)
    print(f"'{sentence}': {'Accepted' if result else 'Rejected'}")

print("\nTesting invalid sentences:")
for sentence in invalid_sentences:
    result = test_sentence(sentence)
    print(f"'{sentence}': {'Accepted' if result else 'Rejected'}")

# Display parse tree for an example sentence
print("\nExample parse tree for 'puella amat puerum':")
for tree in parser.parse("puella amat puerum".split()):
    tree.pretty_print()
