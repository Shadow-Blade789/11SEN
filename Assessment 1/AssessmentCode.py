def money_buckets():
    blow = income * 0.6 #Calculate the amount in each bucket
    d_expense = blow * 0.6
    splurge = blow * 0.6
    smile = blow * 0.6
    extinguisher = blow * 0.2
    grow = income * 0.2
    mojo = income * 0.6
    headers = ["Blow", "Daily Expense", "Splurge", "Smile", "Fire Extinguisher", "Grow", "Mojo"]
    amounts = [f"${round(blow, 3)}", f"${round(d_expense, 3)}", f"${round(splurge, 3)}", f"${round(smile, 3)}", f"${round(extinguisher, 3)}", f"${round(grow, 3)}", f"${round(mojo, 3)}"]
    c = 0
    print("\n\nBucket | Amount\n---------------------------------") #Set up the table
    for h in headers: #Every bucket can be in a different row
        space = (19 - len(headers[c])) * " "
        space2 = (12 - len(amounts[c])) * " "
        print(f"{h}{space}| {amounts[c]}{space2}") #Print the bucket up to in the list
        print("---------------------------------")
        c = c + 1
    


def compound_interest(age, investment):
    print("-----------------\nAge | Investment\n-----------------")
    amount = 0
    print(f"{str(age)}  | ${str(round(investment, 2))}") #Set up the table format
    while age < 60:
        counter = 1
        amount = investment * (1 + rate/100) #Calculate interest
        age = age + counter
        print(f"{str(age)}  | ${str(round(amount, 2))}") #Print the interest in the format
        investment = amount
    print("-----------------")
         
 
age = 0
print("What can I help you with?")
choice = input("Select one, money buckets or compound interest. (mb or ci). ") #Ask users which function they want
if "mb" == choice.lower():
    income = int(input("What is your income? $"))
    while len(str(income)) > 10: #Make sure that income is less than 10 digits
        print("You don't earn that much money!")
        income = int(input("What is your income? "))
    money_buckets()
elif "ci" == choice.lower():
    age = int(input("How old are you currently? "))
    while age > 60: #Ensure age is les than 60
        print("Unfortunately, it is a bit late to start now, but educate someone else so they do not miss the opportunity.")
        age = int(input("How old are you currently?"))
    rate = float(input("What is the return rate, in a percentage. "))
    investment = int(input("How much are you investing per year? "))
    compound_interest(age, investment)
else:
    print("Didn't quite catch that.")
    choice = input("What can I help you with?")