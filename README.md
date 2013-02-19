# Haikuize

> Key Insights Is That <br>
> Code Is Read Much More Often <br>
> Than It Is Written <br>
> &mdash; <cite>[PEP 8](http://www.python.org/dev/peps/pep-0008/)</cite>

A Python toolkit for extracting Haikus from existing text sources. Currently only implements a simple form of extracting Haikus by looking for a series of words with the Haiku format.

Uses the [CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict) to determine syllable counts.


## Installation and Usage

From a terminal:

    # Clone the repo.
    git clone git://github.com/mikeboers/Haikuize.git
    cd Haikuize

    # Download and preprocess CMU dictionary.
    python prepare_corpus.py

    # Filter your text.
    python haikuize.py < /path/to/your/text.txt


## Disclaimer

This library is currently quite unsuitable for usage in another project, as it does not expose any useful API; it only functions as a command to filter input text into a stream of potential haikus.
