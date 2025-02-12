import random
available_option = ["s",'w','g']
random_choice = random.choice(available_option)
print("----------Snake-Water-Gun-Game----------")
print("Enter your choice:\n1.s->snake\n2.w->water\n3.g->gun")
user_choice = input()

print(f"Computer choice:{random_choice}\nYour choice:{user_choice}")

if random_choice==user_choice:
    print("Draw")
elif random_choice=="s":
    if user_choice=="w":
        print("Computer wins!")
    else:
        print("You win!")
elif random_choice=="w":
    if user_choice=="g":
        print("Computer wins!")
    else:
        print("You win!")
elif random_choice=="g":
    if user_choice=="s":
        print("Computer wins!")
    else:
        print("You win!")
else:
    print("Enter correct input.")

