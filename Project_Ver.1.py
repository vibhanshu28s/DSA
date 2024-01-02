def take():
    global jumble_word
    jumble_word = input("Enter Jumbled Word: ")
    jumble_word=jumble_word.upper()



def combi():
    import itertools
    global jumble
    global l_jumble
    permutations = itertools.permutations(jumble_word)
    jumble = [''.join(permutation) for permutation in permutations]
    l_jumble=len(jumble)
    #print(jumble)
    #print(l_jumble)





def read():
    global sp
    global l
    data=open("/Users/Vibhanshu/Desktop/Project1 Anagram/words.txt","r")
    f=data.read()
    sp=f.split()
    l=len(sp)

def list_format():
    global upper_dict
    upper_dict=[]
    for i in range(l):
        up=sp[i].upper()
        upper_dict.append(up)


def compare():
    for i in range(l_jumble):

        for j in range(l):

            if(jumble[i]==upper_dict[j]):

                print(upper_dict[j])
                break


take()
combi()
read()
list_format()
compare()
