import re
import itertools
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--minLetters", type=int, default=4)
parser.add_argument("--repeat", action='store_true')

args = parser.parse_args()

with open("/usr/share/dict/words", "r") as f:
    words=set()
    for l in f:
    	words.add(l.strip().upper())
centre=input("Enter central letter: ").strip().upper()
letters=re.findall(r"[\w']+", input("Enter comma separated letters: ").strip().upper())
letters.append(centre)

for word in words:
    if len(word) >= args.minLetters and centre in word and all(letter in letters for letter in word):
        if args.repeat:
            print(word)
        elif len(set(word)) == len(word):
            print(word)


# i = args.minLetters
# while True:
#     if args.repeat:
#         possible = [_ for _ in list(itertools.combinations_with_replacement(letters,i)) if centre in _]
#     else:
#         possible = [_ for _ in list(itertools.combinations(letters,i)) if centre in _]
#     localValidWords = []
#     for comb in possible:
#         localValidWords.extend([''.join(_) for _ in list(itertools.permutations(comb)) if ''.join(_) in words])
#     localValidWords = list(set(localValidWords))
#     localValidWords.sort()
#     localValidWords=[_.lower() if len(_)!=len(letters) else _ for _ in localValidWords]
#     print(localValidWords)
#     input()
#     i += 1
# validWords=[]
# for comb in possible:
# 	validWords.extend([''.join(_) for _ in list(itertools.permutations(comb)) if ''.join(_) in words])
# validWords=list(set(validWords))
# validWords.sort()
# validWords=[_.lower() if len(_)!=len(letters) else _ for _ in validWords]
# print(validWords)
# print("No of words: ",len(validWords))