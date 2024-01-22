quiz = [["What is the capital of New Zealand?", "Wellington"], 
         ["How many liters is a gallon (with 0,1 precision)?", "4,5"]]

points = 0
for set in quiz:
    print(set[0])
    answer = input("Answer :")
    if answer == set[1]:
        print("That's correct! You win a point!")
        points += 1
    else:
        print("That's wrong! The correct answer was {}".format(set[1]) )
print("Thank you for playing! Your total is {}.".format(points))