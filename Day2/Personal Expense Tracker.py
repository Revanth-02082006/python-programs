import json

def add_expense(amount, category):
    with open("expenses.json", "a") as file:
        entry = {"amount": amount, "category": category}
        json.dump(entry, file)
        file.write("\n")

def view_expenses():
    with open("expenses.json", "r") as file:
        for line in file:
            print(json.loads(line))

add_expense(500, "Food")
view_expenses()
