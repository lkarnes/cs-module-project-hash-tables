whitelist = set("abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'")
def word_count(s):
    cache = {}
    s = s.replace('\n', ' ')
    s = s.replace('\t', ' ')
    s = s.replace('\r', ' ')
    s = ''.join(filter(whitelist.__contains__, s))
    if s != '':
        arr = s.split(" ")
        for i in arr:
            if i != "":
                if i.lower() in cache:
                    cache[i.lower()] += 1
                else:
                    cache[i.lower()] = 1
    return cache

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is\na test of the emergency broadcast network. This is only a test.'))