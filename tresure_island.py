print("welcome to the treasure island.\nyour mission is to find the treasure")
direction=input("which direction do you want to go? L or R;  " ).lower()
if direction == 'l':
    go=input("by what means you want to go? S or W;  ").lower()
    if go == 'w':
        door = input("which door you want to go in? Y ,B ,R;  ").lower()
        if door == 'y':
            print("congratulation! You won")
        else:
            print("loser!")
    else:
        print("loser!")
else:
    print("loser!")