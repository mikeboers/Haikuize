# Haikuize

> Key Insights Is That <br>
> Code Is Read Much More Often <br>
> Than It Is Written <br>
> &mdash; <cite>[PEP 8](http://www.python.org/dev/peps/pep-0008/)</cite>

A Python toolkit for extracting Haikus from existing text sources. Currently only implements a simple form of extracting Haikus by looking for a series of words with the Haiku format.

Uses the [CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict) to determine syllable counts.

First, you must download and preprocess the CMU dictionary:

    python prepare_corpus.py

Basic usage:

    python haikuize.py < input_corpus.txt


