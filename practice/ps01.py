a=32
print(type(a))
c="34"
print(type(c))

num = int(input("Enter a number: "))

count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        count += 1
        num //= 10

print("Total digits:", count)

