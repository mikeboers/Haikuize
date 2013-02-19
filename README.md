# Haikuize

A Python toolkit for extracting Haikus from existing text sources. Currently only implements simplest form of extracting Haikus by looking for a series of words with the Haiku format.

Uses the [CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict) to determine syllable counts.

First, you must download and preprocess the CMU dictionary:

    python prepare_corpus.py

Basic usage:

    python haikuize.py < input_corpus.txt
