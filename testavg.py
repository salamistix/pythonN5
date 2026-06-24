score= int(input("what is your score out of 70? "))
average = score / 70 * 100
pass_score = 70
if average >= pass_score:
    print("you have passed with a score of ", average, "%")
else:
    print("you have failed with a score of ", average, "%")