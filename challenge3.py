Challenge 3

Given the dictionary of words:
albums
barely 
befoul
convex 
hereby 
jigsaw 
tailor 
weaver

And this collection of word “pieces”:
al
bums
bar
ely
be
foul
con
vex
here
by
jig
saw
tail
or
we
aver

Find all six letter words from the dictionary using the collection of pieces. In other words, iterate through the pieces to find the wholes:
al + bums => albums
bar + ely => barely
be + foul => befoul
etc …

Print the attempts used to find the whole:
albar != albums
alely != albums
albe != albums
etc …

______________________________________________
Code:

def find_wholes(dictionary, pieces):
    for word1 in pieces:
        for word2 in pieces:
            attempt = word1 + word2
            if attempt in dictionary and len(attempt) == 6:
                print(f"{word1} + {word2} => {attempt}")
            else:
                print(f"{word1} + {word2} != {attempt}")

# Given dictionary of words
dictionary = {'albums', 'barely', 'befoul', 'convex', 'hereby', 'jigsaw', 'tailor', 'weaver'}

# Given collection of word pieces
pieces = ['al', 'bums', 'bar', 'ely', 'be', 'foul', 'con', 'vex', 'here', 'by', 'jig', 'saw', 'tail', 'or', 'we', 'aver']

# Find and print all six-letter words using the given pieces
find_wholes(dictionary, pieces)
