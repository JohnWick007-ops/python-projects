expenses = []
def add_expenses():
    desc = input("enter the description of expense : ")
    amt = float(input("enter the amount of expense : "))
    date = input("enter the date in form of DD/MM/YYYY : ")
    expenses.append({"description":desc,"amount":amt,"date":date})

def view_expense():
    if not expenses:
        print("no expenses yet")
    else:
        for i, exp in enumerate(expenses,start=1):
            print(f"{i} : {exp["description"]} <--> rupee {exp["amount"]} on data : {exp["date"]}")
        print()
def update_expenses():
    view_expense()
    idx = int(input("which no of expenes you want to update : "))
    if 0 <= idx <= len(expenses) :
        expenses[idx-1]["description"] = input("enter the new description : ")
        expenses[idx-1]["amount"] = input("enter the new amount of expenes : ")
        expenses[idx-1]["date"] = input("enter the date : ")
        print("✅ Expense updated!\n")
    else: 
        print("❌ Invalid index.\n")

    
def delete_expenses():
    view_expense()
    idx = int(input("which no of expenes you want to delete : "))
    if 0 <= idx <= len(expenses) :
        expenses.pop(idx-1)
        print("✅ Expense deleted!\n")
    else: 
        print("❌ Invalid index.\n")         
def total_sum():
    view_expense()
    total_expenses = sum(exp["amount"] for exp in expenses)
def menu():
    while True:
        print("""1.add expenses\n2.view expenses\n3.delete expenses\n4.total expenes5.stop the process""")
        opt = int(input("choose : "))
        if opt == 1:
            add_expenses()
        elif opt ==2:
            view_expense()
        elif opt == 3:
            delete_expenses()
        elif opt ==4 :
            total_sum()    
        elif opt == 5:
            break
        else:
            print("❌ Invalid choice.\n")
menu()