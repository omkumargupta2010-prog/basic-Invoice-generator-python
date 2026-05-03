print("---- INVOICE GENERATOR ----")

customer_name = input("Enter customer name: ")

total = 0

while True:
    item = input("Enter item name (or 'done' to finish): ")
    if item.lower() == 'done':
        break

    price = float(input(f"Enter price for {item}: "))
    total += price

print("\n------ BILL ------")
print("Customer:", customer_name)
print("Total Amount: ", total)
print("------------------")