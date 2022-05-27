expenses = [10, 20, 30, 40, 50, 60, 70]
sum1 = 0
total = sum(expenses)

for x in expenses:
    sum1 += x

print("You spent $", sum1, " on lunch this week.", sep='')
print("You spent $", total, " on lunch this week.", sep='')