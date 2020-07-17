def no_dups(s):
    new_arr = []
    cache = {}    
    s = s.split(' ')
    for index, i in enumerate(s):
        if i in cache:
            s[index] = ''
        else:
            cache[i] = index
            new_arr.append(i)
    print(s)
    return ' '.join(new_arr)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs "))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))