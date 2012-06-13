- website which takes a corpus and generates lots of haikus
- people can assist with
	- calculation of syllables
	- selection of proper grammer
	- selection of style
- turn this into a mechanical turk job

- track how far into the document it comes from
- haiku_id is the hash of the normalized haiku

- score the haikus
	- "the" "and" and other such words at the end of sections are bad
	- perhaps prefer longer words (add the squares of syllable counts)
	- commas or periods at the end of lines are perhaps better
	
- automatically open/close quotes if we start/end within one

- convert numbers into words
	e.g. 23 -> twenty three (3 syllables)

- markov generation
	- find all 5 and 7 syllable sections and remember the word or two (up to 5 or
	  7 syllables) that lead into or out of that section, and then align the
	  sections

- write a Reddit and/or Twitter bot
	- scan new tweets or comments searching for posts which are haikus
		- look for existing bots that already do this
			- see: https://github.com/larryng/reddit-iama-bot
			- see: https://gist.github.com/e17ba08727519dcc3f0c
			- see: https://gist.github.com/e796b65bf9d657cc6f3d
		- connect to the twitter public sample stream to look at
	- only post replies for those that do not match a normalized format
		- lowercase
		- no punctuation
		- don't convert numbers
		- single spaces bettween words
		- single newlines bettween lines
	- post a link to example.com/reddit/$ID
		- have feedback machanisms for determining if this is a good haiku
		- http://haikuize.com/
		- http://haikuresearch.com/
	- present this as a research tool for developing scoring functions for
	  evaluating quality of haikus