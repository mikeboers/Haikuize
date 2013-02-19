import os
import urllib
import json

import haikuize

username = os.environ['USERNAME']
password = os.environ['PASSWORD']

url = 'https://stream.twitter.com/1.1/statuses/sample.json'


class Opener(urllib.FancyURLopener):

    def prompt_user_passwd(self, host, realm):
        return (username, password)


fh = Opener().open(url)
for line in fh:
    data = json.loads(line)
    text = data.get('text')
    if not text:
        continue

    words = text.strip().split()
    words = [x for x in words if not x.startswith('#')]
    words = [haikuize.normalize_word(x) for x in words]

    counts = [haikuize.syllable_count(x) for x in words]
    if any(not x for x in counts):
        continue

    if not sum(counts) == 17:
        continue

    a = haikuize.isolate_syllable_count(5, words)
    b = a and haikuize.isolate_syllable_count(7, words, a)
    if b:
        print ' '.join(x for x in words[0:a]).title()
        print ' '.join(x for x in words[a:b]).title()
        print ' '.join(x for x in words[b:]).title()
        print