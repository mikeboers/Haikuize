import sys
import urllib

# Grabbed this URL from  http://www.speech.cs.cmu.edu/cgi-bin/cmudict
url = 'http://svn.code.sf.net/p/cmusphinx/code/trunk/cmudict/cmudict.0.7a'

if len(sys.argv) > 1:
    path = sys.argv[1]
    fh = sys.stdin if path == '-' else open(path)
else:
    fh = urllib.urlopen(url)

if len(sys.argv) > 2:
    path = sys.argv[2]
    out_fh = sys.stdout if path == '-' else open(path, 'w')
else:
    out_fh = open('syllable_counts.txt', 'wb')

for line in fh:
    
    if not line or not line[0].isalnum():
        continue

    parts = line.strip().split()
    word = parts[0]
    count = sum(int(x[-1].isdigit()) for x in parts[1:])
    out_fh.write('%s %d\n' % (word, count))

