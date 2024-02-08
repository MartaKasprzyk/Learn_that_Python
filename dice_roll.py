import random
def dice_roll():
    print("Dear User! To roll the dice, enter a dice code as follows: xDy+z, where\n"
          "x - number of rolls\n"
          "y - dice type e.g. D6 \n"
          "z - modification + or -\n"
          "example: 2D10+10\n")
    user_code = str(input("Choose dice code: "))
    user_code = user_code.upper()
    code_split_by_D = user_code.split("D")
    try:
        if "D" not in user_code:
            return print("Invalid dice")

        # defines how many rolls (x)
        if code_split_by_D[0] != '':
            x = int(code_split_by_D[0])
            code_wo_x = code_split_by_D[1]
        else:
            x = 1
            code_wo_x = code_split_by_D[1]

        if x < 1:
            return print("Can't roll less than 1")

        # defines modification (z) and dice type (y)
        if len(code_wo_x.split("+")) == 2:
            z = int(code_wo_x.split("+")[1])
            y = int(code_wo_x.split("+")[0])
        elif len(code_wo_x.split("-")) == 2:
            z = int(code_wo_x.split("-")[1]) * -1
            y = int(code_wo_x.split("-")[0])
        else:
            z = 0
            y = int(code_wo_x)

        #checks dice type
        dices = [3, 4, 6, 8, 10, 12, 20, 100]
        if y not in dices:
            print("Incorrect dice type")

        #rolls the dice
        list_of_rolls = []
        for i in range(x):
            roll = random.randint(1, y)
            list_of_rolls.append(roll)

        #modifies the rolls and prints result
        result = sum(list_of_rolls) + z
        print(result)

    except ValueError:
        return print("Invalid dice")

dice_roll()