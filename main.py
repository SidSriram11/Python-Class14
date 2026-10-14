def greet_customer():
    print("Welcome to the LEMONADE STAND")
    print("Fresh LEMONADE made JUST FOR YOU")

greet_customer()

price_per_cup = float(input("What is the price per cup in $ : "))
number_sold = int(input("How many cups were sold ? : "))

def calculatetotal(p , n):
    total_cost = p*n
    return total_cost

total = calculatetotal(price_per_cup , number_sold)
rounded_total = round(total , 2)
print(f"Total cost = {rounded_total}")

total_paid = float(input("How much has the customer paid : "))

def change(t , r):
    pay_back = t - r
    return pay_back

extra = change(total_paid , rounded_total)

print(f"The customer's change is {extra}.")

def thankyou(cups):
    if cups > 5:
        return "WOW, BIG ORDER THANK YOU FOR YOU SUPPORTING SID'S LEMONADE STAND"

    else:
        return "Thanks for stepping by."

message = thankyou(number_sold)
print(message)

print("----------------------------------------")
print("LEMONADE STAND RECIEPT")
print(f"Price per cup : {price_per_cup}")
print(f"Total cups sold : {number_sold}")
print(f"Total proce : {rounded_total}")
print(f"Amount paid by the customer : {total_paid}")
print(f"Change the customer recieved : {extra}")
print("----------------------------------------")