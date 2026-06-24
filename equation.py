one = print("1. calculate speed = distance/time")
two = print("2. calculate distance = speed * time")
three = print("3. calculate time = distance/speed")
if input("please select an equation to solve from below: ") == "1":
    distance = float(input("what is the distance travelled? "))
    time = float(input("what is the time taken? "))
    speed = distance / time
    print("the speed is: ", speed)
    if input("do you want to calculate another equation? (yes/no) ") == "yes":
        exec(open("equation.py").read())
if input("please select an equation to solve from below: ") == "2":
    speed = float(input("what is the speed? "))
    time = float(input("what is the time taken? "))
    distance = speed * time
    print("the distance is: ", distance)
    if input("do you want to calculate another equation? (yes/no) ") == "yes":
        exec(open("equation.py").read())
        if input("please select an equation to solve from below: ") == "3":
            distance = float(input("what is the distance travelled? "))
            speed = float(input("what is the speed? "))
            time = distance / speed
            print("the time taken is: ", time)

            