# Haikuize

A Python toolkit for extracting Haikus from existing text sources. Currently only implements simplest form of extracting Haikus by looking for a series of words with the Haiku format.

Currently depends upon the `nltk cmudict` corpus to determine number of syllables.

Basic usage:

    python haikuize.py < input_corpus.txt
