sub1=int(input("enter bio marks:"))
sub2=int(input("enter eng marks:"))
sub3=int(input("enter cse marks:"))

#check for total percentage

total_percentage= (100*(sub1+sub2+sub3))/300

if(total_percentage>=40 and sub1>33 and sub2>33 and sub3>33):
    print("you are pass",total_percentage)

else:
    print("you are failed, try again next year:",total_percentage)