- website which takes a corpus and generates lots of haikus
- people can assist with
	- calculation of syllables
	- selection of proper grammer
	- selection of style
- turn this into a mechanical turk job

- track how far into the document it comes from
- haiku_id is the hash of the normalized haiku

- look at http://www.amazon.com/dp/0819522392/?tag=stackoverfl08-20

- score the haikus
	- "the" "and" and other such words at the end of sections are bad
	- perhaps prefer longer words (add the squares of syllable counts)
	- commas or periods at the end of lines are perhaps better, while in the
	  middle is pretty bad. Maybe (syl_pos_in_line - num_syl_in_line - 1).
	- consider having all scoring mechanisms auto balance themselves so that
	  over our test sources all of the scores average to zero
	
- automatically open/close quotes if we start/end within one

- convert numbers into words
	e.g. 23 -> twenty three (3 syllables)

- markov generation
	- find all 5 and 7 syllable sections and remember the word or two (up to 5 or
	  7 syllables) that lead into or out of that section, and then align the
	  sections

- API
	haikuize.match(source, allow_extra=False) -> Haiku
	haikuize.find_all(source) -> iterator yielding (potentially overlapping) Haikus
	haikuize.haiku.Haiku -> the haiku itself
		Haiku.normalized_str() -> a normalized version for comparisons
			- lowercase
			- no punctuation
			- don't convert numbers (?)
			- single spaces bettween words
			- single newlines bettween lines
		Haiku.pretty_str(auto_quote=True, case_lines=True) -> get a nicely formatted string
	haikuize.token.Token -> a single word
		Token.source -> the raw string
		Token.keys -> tuple of normalized words to operate on (lowercase, split
			up hyphenations, convert numbers into words, etc.)
		Token.syllables -> sum of syllables
	haikuize.corpus -> module for syllable couting sources
		- preprocess the nltk corpus into a plan text file with (word, count) pairs
		- hand write some for Reddit: LOL, LMAO, FTFY, etc.
		- implement the rough guessing algoritym; make sure the token knows it is
		  an approximation so this can be displayed to the user
	haikuize.token.Tokenizer -> turns a string into a series of tokens

- write a Reddit and/or Twitter bot
	- scan new tweets or comments searching for posts which are haikus
		- look for existing bots that already do this
			- see: https://github.com/larryng/reddit-iama-bot
			- see: https://gist.github.com/e17ba08727519dcc3f0c
			- see: https://gist.github.com/e796b65bf9d657cc6f3d
		- connect to the twitter public sample stream to look at
	- only post replies for those that do not match the normalized format
	- post a link to example.com/reddit/$ID
		- have feedback machanisms for determining if this is a good haiku
		- http://haikuize.com/
		- http://haikuresearch.com/
		- make a permanent session that attaches to a cookie
		- all feedback attaches to that session
		- you see histogram of replies when you have submitted your own feedback
		- break down types of words in the haiku (noun, verb, etc.)
	- present this as a research tool for developing scoring functions for
	  evaluating quality of haikus