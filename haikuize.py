import os
import sys
import re
import curses
from curses.ascii import isdigit

import nltk.corpus

cmudict = nltk.corpus.cmudict.dict() 

def nsyl(word):
    key = cmudict.get(word.lower())
    if not key:
        return
    return len([1 for x in key[0] if x[-1].isdigit()])

def corpus_iter():
    for line in sys.stdin:
        for word in line.strip().split():
            yield word

def find_nsyl(count, words, start=0):
    total = 0
    for i in xrange(start, len(words)):
        word, n = words[i]
        total += n
        if total == count:
            return i + 1
        if total > count:
            return False
    return False

corpus = corpus_iter()
    
words = []
while True:
    
    while len(words) < 17:
        word = next(corpus)
        word = re.sub(r'^\W+', '', word)
        word = re.sub(r'\W+$', '', word)
        n = nsyl(word)
        if not n:
            words = []
            continue
        words.append((word, n))
    
    a = find_nsyl(5, words, 0)
    b = a and find_nsyl(7, words, a)
    c = a and b and find_nsyl(5, words, b)
    
    if a and b and c:
        print ' '.join(x[0] for x in words[0:a]).title()
        print ' '.join(x[0] for x in words[a:b]).title()
        print ' '.join(x[0] for x in words[b:c]).title()
        print
    
    words.pop(0)



