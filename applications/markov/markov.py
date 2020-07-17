import random
whitelist = set("abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
combos = {}

# TODO: analyze which words can follow other words
# Your code here
def deconstruct(w):
    w = w.replace('\n', ' ')
    w = w.replace('\r', '')
    w = w.replace('\t', '')
    w = ''.join(filter(whitelist.__contains__, w))
    w = w.split(' ')
    for i in range(len(w)-1):
        pos = w[i].lower()
        if w[i+1] != '':
            follower = w[i+1].lower()
            if pos in combos:
                if not combos[pos].__contains__(follower):
                    combos[pos].append(follower)
            else:
                combos[pos] = [follower]

def construct(first):
    arr = []
    length = 0
    while first in combos and length < 3000:
        length = length + 1
        arr.append(first)
        first = combos[first][random.randint(0, len(combos[first])-1)]
    arr.append(first)
    return ' '.join(arr)


deconstruct(words)
print(construct('one'))
