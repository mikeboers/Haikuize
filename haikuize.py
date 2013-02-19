import os
import sys
import re
from optparse import OptionParser


_syllable_counts = {}


def syllable_count(word):
    """Estimate number of syllables in a given word.

    Returns None if it cannot tell.

    """

    if not _syllable_counts:
        for line in open('syllable_counts.txt'):
            word, count = line.strip().split()
            _syllable_counts[word] = int(count)

    return _syllable_counts.get(word.upper())


def isolate_syllable_count(count, words, start=0):
    """Return end index to slice given words so they sum to the given count.

    Returns False or an integer, where sum(syllable_count(x) for x in words[:end]) == count.

    """

    total = 0
    for i in xrange(start, len(words)):
        
        word = words[i]
        total += syllable_count(word)

        if total == count:
            return i + 1

        if total > count:
            return False

    return False


def normalize_word(word):
    word = re.sub(r'^\W+', '', word)
    word = re.sub(r'\W+$', '', word)
    return word


if __name__ == '__main__':

    option_parser = OptionParser(usage='%prog [options]')
    option_parser.add_option('-s', '--match-start', action='store_true')
    option_parser.add_option('-e', '--match-end', action='store_true')
    opts, args = option_parser.parse_args()

    if not args:
        files = [sys.stdin]
    else:
        files = [open(x) for x in args]

    def corpus_iter():
        for fh in files:
            for line in fh:
                for word in line.strip().split():
                    yield word

                    if opts.match_end and '.' in word:
                        yield None

            yield None


    corpus = corpus_iter()
        

    words = []
    while True:
        
        while len(words) < 17:

            word = next(corpus)
            if not word:
                words = []
                continue

            word = normalize_word(word)
            n = syllable_count(word)
            if not n:
                words = []
                continue
            words.append(word)
        
        while opts.match_end and word:
            word = next(corpus)

        a = isolate_syllable_count(5, words, 0)
        b = a and isolate_syllable_count(7, words, a)
        c = b and isolate_syllable_count(5, words, b)
        
        if c:
            print ' '.join(x for x in words[0:a]).title()
            print ' '.join(x for x in words[a:b]).title()
            print ' '.join(x for x in words[b:c]).title()
            print
        
        if opts.match_start:
            words = []
        else:
            words.pop(0)
