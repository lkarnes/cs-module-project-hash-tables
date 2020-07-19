with open("robin.txt") as f:
    words = f.read()
    # words = ''.join(filter(whitelist.__contains__, words))
whitelist = set("abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def count_words(w):
    histo = {}
    w = w.lower()
    w = ''.join(filter(whitelist.__contains__, w))
    w = w.split(' ')
    for i in w:
        if i not in histo:
            histo[i] = '#' 
        else:
            histo[i] = histo[i] + '#'   
    res = [f"{k}: {v}" for k,v in sorted(histo.items(),reverse = True, key = lambda item: item[1])]
    for j in res:
        print(j)
count_words(words) 