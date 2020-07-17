with open("robin.txt") as f:
    words = f.read()
    # words = ''.join(filter(whitelist.__contains__, words))
whitelist = set("abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def count_words(w):
    graph = {}