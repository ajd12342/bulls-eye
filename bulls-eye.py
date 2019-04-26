import re
import itertools
f=open("/usr/share/dict/words")
words=set()
for l in f:
	words.add(l.strip().upper())
centre=input("Enter central letter: ").strip().upper()
letters=re.findall(r"[\w']+", input("Enter comma separated letters: ").strip().upper())
letters.append(centre)
possible=[]
for i in range(4,8):
	possible.extend([_ for _ in list(itertools.combinations(letters,i)) if centre in _])
validWords=[]
for comb in possible:
	validWords.extend([''.join(_) for _ in list(itertools.permutations(comb)) if ''.join(_) in words])
validWords=list(set(validWords))
print(validWords)