def money_buckets():
    blow = income * 0.6
    d_expense = blow * 0.6
    splurge = blow * 0.6
    smile = blow * 0.6
    extinguisher = blow * 0.2
    grow = income * 0.2
    mojo = income * 0.6
    headers = ["Blow", "Daily Expense", "Splurge", "Smile", "Fire Extinguisher", "Grow", "Mojo"]
    amounts = [f"${round(blow, 3)}", f"${round(d_expense, 3)}", f"${round(splurge, 3)}", f"${round(smile, 3)}", f"${round(extinguisher, 3)}", f"${round(grow, 3)}", f"${round(mojo, 3)}"]

    if len(str(income)) <= 4:
        row_format = "{:<22}" * len(headers)
    elif len(str(income)) <= 6:
        row_format = "{:<20}" * len(headers)
    elif len(str(income)) <= 8:
        row_format = "{:<19}" * len(headers)
    else:
        row_format = "{:<18}" * len(headers)
        
    print(row_format.format(*headers))
    print(row_format.format(*amounts))

 
def compound_interest():
    print("Age | Investment")
    while age < 61:
        counter = 1
        amount = investment
        amount = investment * (1 + rate/100)
        age = age + counter
        print(f"{str(age)} | {str(round(amount, 3))}")
         
 
 
print("What can I help you with?")
choice = input(print("Select one, money buckets or compound interest. (m or c). "))
choice_counter = 0
while choice_counter == 0:
    if choice.lower() == "m" or "money buckets" or "money_buckets":
        choice_counter = 1
        income = int(input("What is your income? $"))
        while len(str(income)) > 10:
            print("You don't earn that much money!")
            income = int(input("What is your income? "))
        money_buckets()
    elif choice.lower() == "c" or "compound" or "compound interest" or "compound_interest":
        choice_counter = 1
        age = int(input("How old are you currently?"))
        rate = int(round(input("What is the return rate, in a percentage."), 0))
        investment = int(input("How much are you investing per year?"))
    else:
        choice_counter = 0
        print("Didn't quite catch that.")
        choice = input("What can I help you with?")