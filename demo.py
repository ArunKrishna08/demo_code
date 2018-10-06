while True:
    userdata = input("Want to play(y/n): ")
    if userdata == 'y':
        side1 = int(input("Enter side 1: "))**2
        side2 = int(input("Enter side 2: "))**2
        side3 = int(input("Enter side 3: "))**2

        if(side1 + side2 == side3):
            print("Pythagorean Triple")
        elif(side2 + side3 == side1):
            print("Pythagorean Triple")
        elif(side3 + side1 == side2):
            print("Pythagorean Triple")
        else:
            print("Not Pythagorean Triple")

    elif userdata == 'n':
        break
