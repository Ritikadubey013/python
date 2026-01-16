d={} #empty dictionary
marks={
    "ritika":100,
    "arya":98,       #all indexing has been done
    "jats":99
}
marks={"ritika":98}      #dict is mutable 
print(len(marks))
print(marks,type(marks))
#print(marks[0]) error
print(marks["ritika"])

"""we can also form lists in lists for eg
marks=[["harry",100]]
it wont give 100 as output of harry"""