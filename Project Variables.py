name = input("What is your name? ")
birth_year = int(input("When were you born? "))
current_year = int(input("What Year is it currently? "))
age = current_year - birth_year


if birth_year > current_year:
    print("You haven't been born yet!")
    exit()
else:
    print (f"Your name is {name} and you were born in {birth_year}.")
    print (f"I predict you are {age} years old")
if age < 13:
    print("You are a kid.")
elif age >= 13 and age < 18:
    print ("You are a teenager")
else:
    print ("You are an adult!")