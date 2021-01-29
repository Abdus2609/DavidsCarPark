ENGINEER_CODE = "eng123"


# takes the name of the user
def ask_name():
    name = str(input("Please enter your first name: "))
    name = name.capitalize()

    return name


# takes the registration number and duration of stay of the user
def take_info(name):
    regNum = str(input("Please enter your registration number: "))
    regNum = regNum.upper()
    duration = int(
        input("Please enter the number of minutes stayed in the car park: "))

    return regNum, duration


# calculates the user's parking fee
def calculate_fee(name, regNum, duration):
    fee = 2.50
    extraTime = duration - 60
    while extraTime > 0:
        fee += 1.80
        extraTime -= 30
    fee = "{:.2f}".format(fee)
    print(name + ", your parking fee is: £" + fee)
    return fee


# prints a ticket showing the user's information
def print_ticket(name, regNum, duration, fee):
    print("\n")
    print("*" * 40)
    print("               Name:", name)
    print("Registration number:", regNum)
    print("   Duration of stay:", duration, "minutes")
    print("        Parking fee:", fee)
    print("*" * 40)
    print("\n")


# tells the user their data is being saved and saves reg number and fee to external text file
def save_data(regNum, fee):
    print("Saving data...")
    file = open("park_details.txt", "a")
    output_data = regNum + "," + fee + "\n"
    file.write(output_data)
    file.close()


# welcomes engineer to Engineer Mode and asks user to choose summary or registration report
def engineer_mode():
    print("Welcome to Engineer Mode.")
    dataBase = load_data()
    mode = input(
        "Type S for a Summary Report and R for a Registration Report: ")
    mode = mode.upper()
    if mode == "S":
        summary_report(dataBase)
    elif mode == "R":
        reg_report(dataBase)
    else:
        print("Invalid input. Goodbye.")
        exit()


# loads the data from the text file and stores it in a database for the information to be extracted later
def load_data():
    print("\n")
    print("Loading data...")
    dataBase = []
    file = open("park_details.txt", "r")
    line = file.readline().rstrip()
    while line != "":
        regNum, fee = line.split(",")
        record = []
        record.extend((regNum, fee))
        dataBase.append(record)
        line = file.readline().rstrip()
    file.close()
    print("\n")

    return dataBase


# produces a summary report returning total number of cars parked and total profit
def summary_report(dataBase):
    print("\n")
    print("This is the Summary Report:")
    num_cars = 0
    profit = 0
    for record in dataBase:
        num_cars += 1
        profit += float(record[1])
    print("The total number of cars parked here today is:", num_cars)
    print("The total profit for today is: £" + "{:.2f}".format(profit))
    print("\n")


# produces a report of reg numbers and their fees matching the search term
def reg_report(dataBase):
    search_term = input("What is the reg number of the car: ")
    search_term = search_term.upper()
    for record in dataBase:
        if not(search_term in record[0]):
            dataBase.remove(record)
    print("This is the Registration report:")
    print("There are ", len(dataBase), "matches to your search.")
    for record in dataBase:
        print(record)
    print("\n")


print("Welcome to David's Car Park.")
name = ask_name()

if name.upper() == "ENGINEER":
    code = input("Passcode: ")
    i = 0
    while code != ENGINEER_CODE:  # gives an engineer five tries to enter correct password if password entered was wrong
        if i == 5:
            print("You have locked the system. Goodbye!")
            exit()
        else:
            print("Incorrect code. You have",
                  (5 - i), "tries left. Try again.")
            code = input("Passcode: ")
            i += 1
    engineer_mode()
    print("Thank you for visiting this car park. Goodbye!")
    print("\n")
    print("*" * 40)
    print("\n")
    exit()

regNum, duration = take_info(name)
fee = calculate_fee(name, regNum, duration)
print_ticket(name, regNum, duration, fee)
save_data(regNum, fee)

print("\n")
print("Thank you for visiting this car park. Goodbye!")
print("\n")
print("*" * 40)
print("\n")
