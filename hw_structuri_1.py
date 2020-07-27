
year_of_birth = int(input("Please insert your year of birth: "))
current_year  = 2020
age           = current_year - year_of_birth

if year_of_birth < 1900:
    print("Sorry, you're way too old")
elif year_of_birth > current_year: 
    print("Sorry, you're way too young")

if age < 4:
    print("You're a baby, you have:", age, "Y.O, how did you type this? ")
elif age < 10:
    print("You're a kid, you have:", age, "Y.O, better go and play outside!")
elif age < 16:
    print("You're a teen, you have:", age, "Y.O, I miss those times...")
elif age < 19:
    print("You're young, you have:", age, "Y.O, we can go for a drink )")
elif age < 51:
    print("You're an adult, you have:", age, "Y.O, but you're still young, I know")
else:
    print("You're old, you have:", age, "Y.O, well, that's life...")