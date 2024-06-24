name=input("Enter your name:?")
print(f"Welcome to the game {name}")

answer=input("you are on a dirty road,it has come to an end and you can left and right.which way would u like to choose left/right:?").lower()

if answer=="left":
    answer=input("you come to a river, you can walk around it or swim across walk/swim:?").lower()
    if answer=="swim":
        print("You swam across and were eaten by aligator")
    elif answer=="walk":
        print("You walked for mile,ran out of waterand u lost the game ")
    else:
        print("not a valid option,you loose")
if answer=="right":
    answer=input("You come to bridge back/cross?:").lower()
    if answer=="back":
        print("you go back and loose")
    elif answer=="cross":
        answer=input("do u want to talk to starnger yes/no:?")
        if answer=="yes":
            print("you found a tressure,YOU WIN!")
        elif answer=="no":
            print("you loose")
        else:
            print("invalid option")

else:
    print("Its not a valid option")
            
            
    