file = open('./ciphertext.txt','r+')
tester = file.read().replace("\n", " ")
whitelist = set("abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ")
frequency = {
    "E" :11.53,"T" :9.75,"A" :8.46,"O" :8.08,"H" :7.71,"N" :6.73,"R" :6.29,
    "I" :5.84,"S" :5.56,"D" :4.74,"L" :3.92,"W" :3.08,"U" :2.59,"G" :2.48,
    "F" :2.42,"B" :2.19,"M" :2.18,"Y" :2.02,"C" :1.58,"P" :1.08,"K" :0.84,
    "V" :0.59,"Q" :0.17,"J" :0.07,"X" :0.07,"Z" :0.03
    }


def decryptor(s):
    s = ''.join(filter(whitelist.__contains__, s))
    decrypted = {}
    commanality = {}
    length = len(s)
    letters = [letter.upper() for letter in s]
    for i in letters:
        if i in commanality:
            commanality[i] = commanality[i]+1
        else:
            if i != ' ':
                commanality[i] = 1
    sorted_list = [ k for k,v in sorted(commanality.items(),reverse = True, key = lambda item: item[1])]
    frequency_list = ["E","T","A","O","H","N","R","I","S","D","L","W","U","G","F","B" ,"M","Y","C","P","K","V","Q","J","X","Z"]
    for index, i in enumerate(sorted_list):
        decrypted[i] = frequency_list[index]
    response = []
    for j in s:
        if j == ' ':
            response.append(' ')
        else:
            response.append(decrypted[j.upper()])
    return ''.join(response)
print(decryptor('testz'))
print(decryptor(tester))
