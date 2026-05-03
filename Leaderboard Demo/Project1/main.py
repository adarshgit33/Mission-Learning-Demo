#Expense Tracker Project

expensesList = [] #List of all expenses in form of Dictionaries

print("\nWelcome to Expense Tracker")

while True :
    print("\n1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Exit")

    choice = int(input("\nEnter your choice (1 - 4) :"))


#1. Add Expense
    if (choice == 1):

        date = input("Kis date pe kharcha kiya tha? :")
        category = input("Kis type ka kharcha kiya tha ? (food , travel , makeup , books) : ")
        description = input("Aur details dedo : ")
        amount = float(input("Enter the amound of Kharcha :"))

        expense = {
            "date" : date,
            "category" : category,
            "description" : description,
            "amount" : amount
            }
        expensesList.append(expense)
        print("\nWohooo ! Your Expense is added successfully.")

#View All Expenses
    elif (choice == 2):

        if(len(expensesList) == 0):
            print("Aapne abhi tak koi kharcha nhi kiya hai , jayiye kharcha kijiye pehle")

        else:
            print("=====Ye hai aapka ab tak ka kharcha=====")

            count=1
            for eachKharcha in expensesList:
                print(f"Kharcha no {count} --> {eachKharcha["date"]}, {eachKharcha["category"]}, {eachKharcha["description"]}, {eachKharcha["amount"]} ")
                count=count+1

# View total spending 

    elif (choice == 3):
        total=0
        for eachKharcha in expensesList:
            total=total + eachKharcha["amount"]

        print("\nAb tak ka Total kharcha : ",total)

# Exit

    elif (choice == 4):

        print("Dhanyawaad service use krne k liye, Fir milenge Bye")
        break

    else:
        print("Invalid choice. Try again ")

    



            


