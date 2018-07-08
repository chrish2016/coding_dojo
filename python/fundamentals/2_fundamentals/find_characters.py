wordlist = ['hello','world','my','name','is','Anna']

def find_char(wordlist, char):
    new_list = []

    for i in range(0, len(wordlist)):
        if wordlist[i].find(char) != -1:
            new_list.append(wordlist[i])

            print(new_list)

find_char(wordlist, 'o')