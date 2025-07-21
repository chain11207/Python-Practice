# Ask for the user's name and birth year
name = input("What is your name? ")
birth_year = int(input("What year were you born? "))

# Ask for the current year so we can figure out how old the user is
current_year = int(input("What is the current year? "))

# Work out the user's age
age = current_year - birth_year

# If the birth year is in the future, the user hasn't been born yet
if birth_year > current_year:
    print("You haven't been born yet!")
else:
    print("Hi", name)
    print("You are", age, "years old")

    # Tell the user what age group they are in
    if age < 13:
        print("You are a kid.")
    elif age < 18:
        print("You are a teenager.")
    else:
        print("You are an adult.")
