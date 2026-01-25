n=int(input("enter your num :"))

for i in range(2,n):
    if(n%i==0):
        print("number is not prime")
        break

    else:
        print("num is prime")