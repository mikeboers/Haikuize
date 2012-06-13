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
