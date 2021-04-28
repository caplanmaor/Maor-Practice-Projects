from cs50 import get_float

coins_count = 0
coinTypes = [25, 10, 5, 1]

print("Calculate how many coins you need to give back a certain amount of change")

#get a positive value from the user otherwise keep asking
while True:
    dollars = get_float("Change Ammunt: ")
    if dollars >= 0:
        break

#round to solve float point inaccuracy
cents = round(dollars * 100)

#go over each coin type and compare it with how many cents we have left
#take out the amount of coins and add a coin to our count
for currentCoin in coinTypes:
    while cents >= currentCoin:
        cents -= currentCoin
        coins_count += 1

print(coins_count)