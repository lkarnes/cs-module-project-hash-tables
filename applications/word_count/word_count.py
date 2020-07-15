whitelist = set("abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ'\r\n\t")
def word_count(s):
    cache = {}
    print(s)
    s.replace("\r",' ')
    s.replace("\t",' ')
    s.replace("\n",' ')
    print(s)
    s = ''.join(filter(whitelist.__contains__, s))
    if s != '':
        arr = s.split(" ")
        for i in arr:
            if i != "":
                if i.lower() in cache:
                    cache[i.lower()] += 1
                else:
                    cache[i.lower()] = 1
    print(cache, s)
    return cache

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))