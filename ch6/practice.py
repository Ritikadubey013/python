marks=int(input("enter your marks:"))

if(marks<=100 and marks>=90):
    Grade="ex"

elif(marks<90 and marks>=80):
    Grade="a"

elif(marks<80 and marks>=70 ):
    Grade="b"

elif(marks<70 and marks>=60 ):
    Grade="c"

elif(marks<60 and marks>=50 ):
    Grade="d"

elif(marks<50):
    Grade="f"
    
print("your grade is  ",Grade)