print("**********************************")
print("============Calculator============")
print("**********************************")

# this function adds two numbers


def add(x, y):
    return x + y

# this function subtracts two numbers


def sub(x, y):
    return x - y

# this fnction divides two numbers


def div(x, y):
    return x / y

# this function multiplies two numbers


def mul(x, y):
    return x * y

# this function remainder two numbers


def mod(x, y):
    return x % y


print("1.Addition")
print("2.Subraction")
print("3.Division")
print("4.Multiplication")
print("5.Remainder")

while True:

    # take input from the user
    choice = input("Enter your choice : ")

    # Check choice is one of the five options
    if choice in ('1', '2', '3', '4', '5'):
        x = float(input("Enter value of x : "))
        y = float(input("Enter value of y : "))

    else:
        print("Invalid Choice!!!")
        continue

    if choice == '1':
        print("Addition = ", x, "+ ", y, " = ", x+y)
    if choice == '2':
        print("Subtraction = ", x, "- ", y, " = ", x-y)
    if choice == '3':
        print("Division = ", x, "/ ", y, " = ", x/y)
    if choice == '4':
        print("Multiplication = ", x, "* ", y, " = ", x*y)
    if choice == '5':
        print("Remainder = ", x, "% ", y, " = ", x % y)

    # Check user wants another calculation or not
    # if answer is no then break the loop

    next_calcu = input("Let's do next calculation??? (yes/no) : ")
    if next_calcu == 'no':
        break
