''' write a py function to remove a given word from a list 
ad strip it at same time'''

def rem(l,word):
    n=[]

    for item in l:
        if not(item == word):
            n.append(item.strip(word))
            return n
l=["ritika","arya","an","rohan"]

print(rem(l,"an"))
