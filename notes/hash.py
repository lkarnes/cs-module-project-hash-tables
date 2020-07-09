my_arr = ["hello", "this", "is", "an ", "array"]
# you can make 0(1) with an array using a hash table
# by creating a hash function
# to hash something is to make a mess of it/or chop it up like with dicts in py

#function
#1 takes a string
#2 gives us back a number

x = 'Hello'
def give_num(word):
    count = 0
    x = word.encode()
    for i in x: 
        count += i
    return count


hello_index = give_num("hello")
my_arr = [None] * 5
hello_index = hello_index % len(my_arr)
my_arr[hello_index] = "hello"
#ASCII: assigns letters to numbers 
# use py ord() to use ASCII
print(x)
#UTF-8
#use .encode for utf-8