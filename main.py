# Write a Python program to calculate a dog's age in dog's years. Note: For the 
# first two years, a dog year is equal to 10.5 human years. After that, each dog 
# year equals 4 human years. 
# Expected Output: 
# Input a dog's age in human years: 15 
# The dog's age in dog's years is 73

dogsAgeHumanYears = int(input("Input a dog's age in human years: "))

while dogsAgeHumanYears <= 0:
    dogsAgeHumanYears = int(input("Input a dog's age in human years that is greater than 0: "))

if dogsAgeHumanYears <= 1:
    dogsAgeDogYears = (dogsAgeHumanYears * 10.5)
    print("The dog's age in dog's years is", (dogsAgeDogYears))
elif dogsAgeHumanYears == 2:
    dogsAgeDogYears = (dogsAgeHumanYears * 10.5)
    print("The dog's age in dog's years is", (int(dogsAgeDogYears)))
else:
    dogsAgeDogYears = ((dogsAgeHumanYears - 2) * 4) + (2 * 10.5)
    print("The dog's age in dog's years is", (int(dogsAgeDogYears)))
