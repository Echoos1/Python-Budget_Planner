import datetime

hours = float(input("Enter Weekly Paid Hours: "))
payrate = float(input("Enter Hourly Payrate: $"))
taxes = float(input("Enter Tax Rate (Typically ~0.20): "))

grossearnings = hours * payrate
incomeweekly = grossearnings * (1 - taxes)


weeklyexpenses = float(input("Enter Weekly Expenses: $"))
monthlyexpenses = float(input("Enter Monthly Expenses: $"))
yearlyexpenses = float(input("Enter Annual Expenses: $"))

totalexpensesweekly = weeklyexpenses + ((7 * monthlyexpenses) / 30.417) + (yearlyexpenses / 52.143)


currentsavings = float(input("Enter Amount Currently Saved Up: $"))
goal = float(input("Enter Savings Goal: $"))

weeklysavings = incomeweekly - totalexpensesweekly
monthlysavings = ((30.417 * weeklysavings) / 7)
monthstogoal = (goal - currentsavings) / monthlysavings
weekstogoal = (goal - currentsavings) / weeklysavings
daystogoal = weekstogoal * 7

now = datetime.datetime.now()
finish = now + datetime.timedelta(days=daystogoal)
finishdate = finish.strftime('%B %d, %Y')

yesnodeadline = input("Is There A Deadline to Reach The Goal? (y/n) ")
yesdeadlineoptions = ["Y", "YES"]
nodeadlineoptions = ["N", "NO"]

if yesnodeadline.upper() in yesdeadlineoptions:

    timetogoal = input("Enter Date of Goal Deadline (mm/dd/yyyy)")
    dateofgoal = datetime.datetime.strptime(timetogoal, '%m/%d/%Y')

    timeleft = dateofgoal - now
    days = timeleft.days + 1
    weeks = days / 7

    moneyatdeadline = (weeklysavings * weeks) + currentsavings
    remainder = -1 * (goal - moneyatdeadline)

    maxspendingmoney = remainder / weeks
    recommendedspendingmoney = maxspendingmoney * 0.2

    moneyperweek = (goal - currentsavings) / weeks

    results = f'\n----------------------------------------------------------------------' \
              f'\n\nTypical Take-home Amount: ${"{:.2f}".format(incomeweekly)}' \
              f'\nTotal Expenses Averaged per Week: ${"{:.2f}".format(totalexpensesweekly)}' \
              f'\nWeekly Savings: ${"{:.2f}".format(weeklysavings)}' \
              f'\n\nSavings Goal Will Be Met On {finishdate}' \
              f'\n\nGoal: ${"{:.2f}".format(goal)}' \
              f'\nDays Left to Deadline: {days}' \
              f'\nWeeks Left to Deadline: {weeks}' \
              f'\n\nAmount Saved At Goal Deadline: ${"{:.2f}".format(moneyatdeadline)}' \
              f'\nMoney Left After Deadline: ${"{:.2f}".format(remainder)}' \
              f'\n\nYou Would Have to Save ${"{:.2f}".format(moneyperweek)} Per Week To Hit The Goal On The Deadline' \
              f'\n\n Max Spending Money: ${"{:.2f}".format(maxspendingmoney)} Per Week' \
              f'\nRecommended Spending Money: ${"{:.2f}".format(recommendedspendingmoney)} Per Week' \
              f'\nMoney Left After Deadline With Using Recommended Spending ${"{:.2f}".format(remainder * 0.8)}'

    print(results)
else:
    results = f'\n----------------------------------------------------------------------' \
              f'\n\nTypical Take-home Amount: ${"{:.2f}".format(incomeweekly)}' \
              f'\nTotal Expenses Averaged per Week: ${"{:.2f}".format(totalexpensesweekly)}' \
              f'\nWeekly Savings: ${"{:.2f}".format(weeklysavings)}' \
              f'\n\nSavings Goal Will Be Met On {finishdate}' \
              f'\n\nGoal: ${"{:.2f}".format(goal)}' \

    print(results)

input("\nPress Any Key to Exit... ")
