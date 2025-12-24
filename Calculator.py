print("Welcome To This Calculator")
start = input("Do You Want To Do Some Math Today? : ")
if start == "yes":
    print("What Type of Math Are We Going To Do Today")
else:
    print("Okay See You Later")
    exit()
while True:

    first_number = float(input("What is your First Number?: "))
    equation = input("What Equation +, -, *, /: ")
    second_number = float(input("What is your Second Number?: "))

    if equation == "+":
        result = first_number + second_number  
    elif equation == "-":
        result = first_number - second_number
    elif equation == "*":
        result = first_number * second_number
    elif equation == "/":
        if second_number == "0":
            print("You Can't Divide By 0")
            continue
        result = first_number / second_number
    else:
        print("Try Again")
        continue

    print("The Answer is: ", result)

    again = input("Do You Want To Do More Math?: ")
    if again == "yes":
        continue
    else:
        print("Okay See You Later")
        break