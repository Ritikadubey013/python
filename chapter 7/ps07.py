'''
for n = 3
  *
 ***
*****

'''
n=int(input("enter your no:"))

for i in range(1,n+1):
    print(" "*( n-i),end="") #this end statement wont add default line 
    print("*" * (2*i-1), end="")
    print(" ")
