import random

choice = int(input('enter your choice:'))
user_choice = choice


comp_choice = random.randint(1, 3)
print(user_choice)
print(comp_choice)

logic = "TWLLTWWLT"
print(logic[(((user_choice) * 3) + (comp_choice)) ]);



# if (user_choice == 1 and comp_choice == 2) or (comp_choice == 1 and user_choice == 2):
#         result = 2

# elif(user_choice==2 and comp_choice==3) or (comp_choice==2 and user_choice==3):
#         result = 3
        
# elif(user_choice==3 and comp_choice==1) or (comp_choice==3 and user_choice==1):
#         result = 1




        
# if result==comp_choice:
#         print("computer wins")
# elif result==user_choice:
#         print("you won")
# else:
#         print("Tie")



# if (user_choice == comp_choice):
#         print("Tie@@@")
# elif ((user_choice - comp_choice) % 3 == 1):
#         print("You Won@@@")
# else:
#         print("You Lose@@@")