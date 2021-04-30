from nltk import CFG
from nltk.parse import RecursiveDescentParser


def tree_gen_draw(grammar,sentence):
    recursive_parser = RecursiveDescentParser(grammar)
    treegen = recursive_parser.parse(sentence)
    for t in treegen: print(t)
    draw_tree = recursive_parser.parse(sentence)
    trees = [t for t in draw_tree]
    for i in range(len(trees)):
        trees[i].draw()


grammar1 = CFG.fromstring("""
S -> NP VP
VP -> V NP | V NP PP
PP -> P NP
NP -> 'John' | 'Mary' | 'Bob' | Det N | Det N PP
V -> 'saw' | 'ate' | 'walked'
Det -> 'a' | 'an' | 'the' | 'my'
N -> 'man' | 'dog' | 'cat' | 'telescope' | 'park'
P -> 'in' | 'on' | 'by' | 'with'
""")

grammar2 = CFG.fromstring("""
S -> NP VP
NP -> Det Nom | PropN
Nom -> Adj Nom | N
VP -> V Adj | V NP | V S | V NP PP
PP -> P NP
PropN -> 'Buster' | 'Chatterer' | 'Joe'
Det -> 'the' | 'a'
N -> 'bear' | 'squirrel' | 'tree' | 'fish'
Adj -> 'angry' | 'frightened' | 'little' | 'tall'
V -> 'chased' | 'said' | 'thought' | 'was' | 'put'
P -> 'on'
""")


#Grammar 1 sentences :

sentence1_g1 = 'John saw Mary in the park'.split()
sentence2_g1 = 'Mary saw a cat with the telescope'.split()

tree_gen_draw(grammar1, sentence1_g1)
tree_gen_draw(grammar1,sentence2_g1)


Sentence_1_g2= 'the angry bear chased the frightened little squirrel'.split()
Sentence_2_g2= 'Joe thought Buster said the fish was little'.split()
tree_gen_draw(grammar2, Sentence_1_g2)
tree_gen_draw(grammar2, Sentence_2_g2)













