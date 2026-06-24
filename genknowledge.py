question1 = input("what is the capital of france? ")
if question1 == "paris":
    print("correct")
else:
    print("incorrect") 
question2 = input("what is the capital of spain? ")
if question2 == "madrid":
    print("correct")
else:
    print("incorrect")
question3 = input("what is the capital of italy? ")
if question3 == "rome":
    print("correct")
else:
    print("incorrect")
question4 = input("what is the capital of germany? ")
if question4 == "berlin":
    print("correct")
else:
    print("incorrect")
question5 = input("what is the capital of portugal? ")
if question5 == "lisbon":
    print("correct")   
else:
    print("incorrect")
question6 = input("what is the capital of belgium? ")
if question6 == "brussels":
    print("correct")
else:
    print("incorrect")
question7 = input("what is the capital of netherlands? ")
if question7 == "amsterdam":
    print("correct")
else:
    print("incorrect")
question8 = input("what is the capital of austria? ")
if question8 == "vienna":
    print("correct")
else:
    print("incorrect")
question9 = input("what is the capital of switzerland? ")
if question9 == "bern":
    print("correct")
else:
    print("incorrect")
question10 = input("what is the capital of norway? ")
if question10 == "oslo":
    print("correct")
else:
    print("incorrect")
total_correct = 0
if question1 == "paris":
    total_correct += 1
if question2 == "madrid":
    total_correct += 1
if question3 == "rome":
    total_correct += 1
if question4 == "berlin":
    total_correct += 1
if question5 == "lisbon":
    total_correct += 1
if question6 == "brussels":
    total_correct += 1
if question7 == "amsterdam":
    total_correct += 1
if question8 == "vienna":
    total_correct += 1
if question9 == "bern":
    total_correct += 1
if question10 == "oslo":
    total_correct += 1

print(f"you got {total_correct} out of 10 questions correct.")  