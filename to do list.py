#  كشف هل يوجد اي تاسكات
# انشاء تاسكات ودخلها الي الليست
# طباعه كل التاسكات 
# when click any hthing not addd resent print

to_do_list=[]    
name=input("enter your name : ")
want=input("wat are you wont :")
def chek_to_do_list():
    if want == "show":
          if to_do_list==[]:
              print("not found")
          else:
              for j in to_do_list:
                print(j)
chek_to_do_list()
def add_to_do_list():
  count=0
  if want== "add":
    add=input("enter to add to do : ")
    while want == "add":
        count+=1
        want_add=input(f"enter the to do again {count} : ")        
        to_do_list.append(add)
        to_do_list.append(want_add)
        if want_add=="show":

          for n in to_do_list:
            print(n)
          
          again=input("did you add some task : ")
          if again =="yes":
            while again=="yes":
                two_task=input("enter the match task here this lastet of append : ")
                to_do_list.append(two_task)
                if two_task=="break":
                    print( to_do_list)

                    break
            break
          else:
            print( to_do_list)
              
            break                 


add_to_do_list()

