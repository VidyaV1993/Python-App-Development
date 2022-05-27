# Get the loan details
money_owed = float(input("Money owed?\n"))
apr = float(input("apr?\n"))
payment = float(input("monthly payment in dollars?\n"))
months = int(input("how many months do you want to see the results for?\n"))

# Calculate the percentage anddivide by 12 to get monthly
monthly_rate = apr/100/12

for i in range(months):
    
    # Add in the interest
    interest_paid = money_owed*monthly_rate
    money_owed+=interest_paid

    if(money_owed-payment<0):
        print("The last payment is", money_owed)
        print("You paid off the loan in", i+1, " months")
        break

    # Make payment
    money_owed-=payment

    # Print the results
    print("Paid", payment, "of which", interest_paid, "was interest.", end=' ')
    print("Now I owe", money_owed)
