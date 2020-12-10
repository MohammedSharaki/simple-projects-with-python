print("find the\n       1- find Side\n       2- find corner\n please enter number to slove : ")

l=input("enter your problem : ")

if l=="2":

    ab=int(input("enter the  AB : "))

    bc=int(input("enter the  BC : "))

    ac=int(input("enter the  AC : "))

    if (ab*ab + bc*bc) ==ac*ac:
        print("this is Qaemeh Angle in B")

    elif (bc*bc + ac*ac) ==ab*ab:
        print("this is Qaemeh Angle in C")

    elif (ac*ac + ab*ab) ==bc*bc:
        print("this is Qaemeh Angle in A")

    else:

        print("please return")

elif l=="1":

    ab=float(input("enter the frist Side : "))

    bc=float(input("enter the sec Side : "))

    ab1=ab*ab
    bc1=bc*bc

    a=ab1+bc1
    print(a**(1.0/2))
