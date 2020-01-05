a=int(input("enter the number"))
choice=input("enter operation")
c=int(input("enter the number"))

if choice=="+":
    print("{}  {}".format(a,c))
    print(a + c)
elif choice=='-':
    print("{} - {}".format(a,c))
    print(a - c)
elif choice=='*':
    print("{} * {}".format(a,c))
    print(a * c)
elif choice=='/':
    print("{} / {}".format(a,c))
    print(a / c)
else:
    print("invalid input")