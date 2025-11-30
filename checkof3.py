a=int(input("enter 1st no:"))
b=int(input("enter 2nd no:"))
c=int(input("enter 3rd no:"))

if a>b and a>c:
    print(a,"is larger");
elif b>a and b>c:
    print(b," is larger")
else:
    print(c," is larger")