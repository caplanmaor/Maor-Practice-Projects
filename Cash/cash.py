from cs50 import get_float

coins = 0

print("Calculate how many coins you need to give back a certain amount of change")

#get a positive valure from the user otherwise keep asking
while True:
    dollars = get_float("Change Ammunt: ")
    if dollars >= 0:
        break

cents = round(dollars * 100)

while cents >= 25:
    cents -= 25
    coins += 1

while cents >= 10:
    cents -= 10
    coins += 1

while cents >= 5:
    cents -= 5
    coins += 1

while cents >= 1:
    cents -= 1
    coins += 1

print(coins)