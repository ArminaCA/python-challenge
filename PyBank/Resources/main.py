import csv

csvpath = "budget_data.csv"

total_months = 0
net_total = 0
prev_profit_loss = 0
total_profit_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        total_months += 1
        net_total += int(row[1])

        current_profit_loss = int(row[1])
        if total_months > 1:
            profit_change = current_profit_loss - prev_profit_loss
            total_profit_change += profit_change

         
            if profit_change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = profit_change
            if profit_change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = profit_change

        
        prev_profit_loss = current_profit_loss

average_profit_change = total_profit_change / (total_months - 1)

print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_profit_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")