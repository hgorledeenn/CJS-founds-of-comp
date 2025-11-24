## Holden Green
## 11-01-2025
## Homework 2

## Ask for input and define user age variable

current_year = 2025
holden_age = 22
user_age = int(input("How old are you?"))


if user_age < 0:
    user_age = int(input("Try again. How old are you really?"))
else:
    print("Thank you! One more question.")

birthday_question = int(input("Has your birthday occurred yet this year? If no type 0; if yes type 1."))


## 1. Print the age
print("1. You are", user_age, "years old.")

## 2. Print the # of times users heart has beaten (assuming 80bpm avg heartrate, according to American Heart Association)
user_heartbeats = user_age * (80 * 60 * 24 * 365)
print("2. Your heart has beaten approximately", format(user_heartbeats, ","), "times in your life.")

## 3. Print the # of times a blue whale's heart has beaten in that time (assuming 15bpm avg heartrate, according to whalescientists.com)
whale_heartbeats = user_age * (15 * 60 * 24 * 365)
print("3. A blue whale's heart would have beaten approximately", format(whale_heartbeats, ","), "times in your life.")

## 4. Print the # of times a rabbit's heart has beaten in that time (assuming 160bpm avg heartrate, according to rabbit.org)
rabbit_heartbeats = user_age * (160 * 60 * 24 * 365)

if rabbit_heartbeats >= 1000000000:
    print(f"4. A rabbit's heart would have beaten approximately {round((rabbit_heartbeats/1000000000),2)} billion times in your life.")
else:
    print(f"4. A rabbit's heart would have beaten approximately {format(rabbit_heartbeats, ",")} times in your life.")

## 5. Redo a previous question with a different format
# I chose to redo question 3 (blue whale heartbeats) with another method:
whale_heartbeats_2 = str(whale_heartbeats)
print("5. Using string addition, a blue whale's heart would have beaten approximately " + whale_heartbeats_2 + " times in your life.")

## 6. Return whether they are the same age as me, or older or younger than me and if they were born in an even or odd year
# Same age/older/younger?
if user_age == holden_age:
    print("You are the same age as Holden.")
elif user_age > holden_age:
    print("You are older than Holden. Please share your wisdom.")
else:
    print("You are younger than Holden. Seek out his wisdom.")

# Born in even or odd year?
# First I use the earlier prompted answer to birthday_question to figure out the user's correct birth year
if birthday_question == 1:
    user_birth_year = (current_year - user_age)
else:
    user_birth_year = (current_year - user_age - 1)
# Then I use modulo to determine whether the user's birth year was even or odd
if (user_birth_year % 2) == 0:
    print(f"You were born in {user_birth_year}, an even year")
else:
    print(f"You were born in {user_birth_year}, an odd year")

## 7. Return the # of Democratic US presidents in their lifetime (since 1980, includes a president who left office on Jan. 20 of a given year in that year's count)
if user_birth_year < 1980:
    print("There have been at least 4 US Presidents from the Democratic party in your lifetime.")
elif 1980 < user_birth_year <= 1981:
    print("There have been 4 US Presidents from the Democratic party in your lifetime.")
elif 1981 < user_birth_year <= 2001:
    print("There have been 3 US Presidents from the Democratic party in your lifetime.")
elif 2001 < user_birth_year <= 2017:
    print("There have been 2 US Presidents from the Democratic party in your lifetime.")
elif 2017 < user_birth_year <= 2025:
    print("There has been 1 US President from the Democratic party in your lifetime.")
else:
    print("How did you find this error? Maybe try again.")

## 8. Return the President in their birth year (if birth year is an inauguration year, I returned the newly inaugurated president)
if user_birth_year <= 1976:
    print("I don't think our records go back far enough to know who was president when you were born.")
elif 1976 < user_birth_year <= 1980:
    print("When you were born, the president was Jimmy Carter, a Democrat.")
elif 1980 < user_birth_year <= 1988:
    print("When you were born, the president was Ronald Reagan, a Republican.")
elif 1988 < user_birth_year <= 1992:
    print("When you were born, the president was George H. W. Bush, a Republican.")
elif 1992 < user_birth_year <= 2000:
    print("When you were born, the president was Bill Clinton, a Democrat.")
elif 2000 < user_birth_year <= 2008:
    print("When you were born, the president was George W. Bush, a Republican.")
elif 2008 < user_birth_year <= 2016:
    print("When you were born, the president was Barack Obama, a Democrat.")
elif 2016 < user_birth_year <= 2020:
    print("When you were born, the president was Donald Trump, a Republican.")
elif 2020 < user_birth_year <= 2024:
    print("When you were born, the president was Joe Biden, a Democrat.")
elif 2024 < user_birth_year <= 2028:
    print("When you were born, the president was Donald Trump, a Republican.")

## 9. Another approach to #8:

# I'm not necessarily sure if I have the skills to do this yet, but if there were a source online or a csv with all the presidents listed, I could have a program that reads that and then uses if/else statements to return the same information. The benefit of that would be that I don't have to manually research all the presidents and input their names and party affiliations manually. And, if this were a project with a larger scope or that I wanted to continue working without having to update it for many years, it would help to only rely on a list that auto updated. However, like you said in class, we are lazy and writing all that code to find a relevant list and then input it and run logic tests on it sounds like a lot of work. My method might be out of date in 3 years, but it took me like 10 minutes to write.

## 10. Re-ask age if age is negative
# I included this code at the top, just below where I define the variable user_age. The code I used is below as well:
# if user_age < 0:
#     user_age = int(input("Try again. How old are you really?"))
# else:
#     print("Thank you! One more question.")