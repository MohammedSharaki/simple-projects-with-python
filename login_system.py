name=input("enter your name : ")
age=int(input("enter your age : "))
print(f"hello {name} ")
print("_"*20)
gmail=input("enter the gmail : ")
password=input("enter the password : ")
print("_"*20)
gmail1=input("enter the gmail again to singin : ")
password1=input("enter the gamil to sign in : ")
print("_"*20)
if gmail == gmail1 and password == password1 :
    print(f"hello {name}")
else:
    chek_gmail=input("enter the gmail again : ")
    trying=5
    while chek_gmail !=gmail:
            trying-=1
            print(f"wong gmail {trying} try left ")
            inputpass=input("enter the gmail :")
            if inputpass == gmail:
                print(f"hello {name}")
                chek_password=input("please enter the password to login : ")
                if chek_password==password:
                    print(f"hello {name} again ")
                    break
                else:
                    print("enter again letar . ")
                    break
            if trying ==0 :
                break
         