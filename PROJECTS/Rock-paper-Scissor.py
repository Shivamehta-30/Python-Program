import random
comp_list=['Rock','Paper','Scissor']
computer_guess=comp_list[random.randint(0,2)]
op="yes"
while op=="yes":
    user = input("YOUR TURN:")
    print("YOUR ACTION:", user)
    print("COMPUTER TURN:", computer_guess)
    if user==computer_guess:
        print("MATCH DRAW!!!!")
    elif user=='Rock':
        if computer_guess=='Paper':
            print("YOU WIN")
    elif user=='Paper':
        if computer_guess=='Rock':
            print("YOU WIN")
    elif user=='Rock':
        if computer_guess=='Scissor':
            print("YOU WIN")
    elif user=='Rock':
        if computer_guess=='Scissor':
            print("YOU LOSE")
    elif user=='Paper':
        if computer_guess=='Scissor':
            print("YOU LOSE")
    elif user=='Scissor':
        if computer_guess=='Rock':
            print("YOU LOSE")
    op=input("Do you want to play again ?(yes/no):")
