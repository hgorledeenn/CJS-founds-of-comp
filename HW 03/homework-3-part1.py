## Holden Green
## 11-04-2025
## Homework 3, Part 1

## SECTION 1.A: Lists
print("SECTION 1.A: Lists")

# Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
numbers = [22, 90, 0, -10, 3, 22, 48]

# Display the number of elements in the list. (and yes, display means print)
print("====== QUESTION 1 ======")
for number in numbers:
    print(number)
# Display the 4th element of this list.
print("====== QUESTION 2 ======")
print(numbers[3])

# Display the sum of the 2nd and 4th element of the list.
print("====== QUESTION 3 ======")
sum_num24 = int(numbers[1]) + int(numbers[3])
print(sum_num24)

# Display the 2nd-largest value in the list.
print("====== QUESTION 4 ======")
numbers_desc = sorted(numbers,reverse=True)
print(numbers_desc[1])

# Display the last element of the original unsorted list
print("====== QUESTION 5 ======")
print(numbers[-1])

# Display the sum of all of the numbers divided by two.
# Source - https://stackoverflow.com/questions/8244915/how-do-you-divide-each-element-in-a-list-by-an-int
print("====== QUESTION 6 ======")
my_int = 2
numbers_div_2 = [x / my_int for x in numbers]
print(sum(numbers_div_2))

# Print whether the median or the mean of the numbers is higher
print("====== QUESTION 7 ======")

length_numbers = len(numbers_desc)

middle_numbers = round((length_numbers/2)-1)
median_numbers = numbers_desc[middle_numbers]
print(f"The median was {median_numbers}")

numbers_sum = sum(numbers)
mean_numbers = numbers_sum/length_numbers
print(f"The mean was {mean_numbers}")

if mean_numbers > median_numbers:
    print(f"The mean, {mean_numbers}, was higher than the median, {median_numbers}.")
elif median_numbers > mean_numbers:
    print(f"The median, {median_numbers}, was higher than the mean, {mean_numbers}.")
elif mean_numbers == median_numbers:
    print(f"The mean, {mean_numbers}, was equal to the median, {median_numbers}.")
else:
    print("There was an error. Sorry. I know you were really excited for this result.")



## SECTION 1.B: Dictionaries
print("===================================")
print("==== SECTION 1.B: Dictionaries ====")
print("===================================")

# Oftentimes dictionaries are used to describe multiple aspects of a single object. Like, say, a movie. Define a dictionary called movie that works with the following code.
# print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])
print("====== QUESTION 1 ======")

movie = {
    'title': "Luca",
    'year': "2021",
    'director': "Enrico Casarosa"
}

print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])



# On the lines after that, add keys to the movie dictionary for budget and revenue (you'll use code like movie['budget'] = 1000), and print out the difference between the two.

## THERE was not a publicly released budget total for Luca, but people on reddit (source below) seemed to guess it was somewhere around $150 million.
# https://www.reddit.com/r/boxoffice/comments/ta0rmv/okay_lets_settle_this_again_what_do_you_think_the/

# revenue from here: https://www.the-numbers.com/movie/Luca-(2021)#tab=summary
print("====== QUESTION 2 ======")
movie['budget'] = 150000000
movie['revenue'] = 51111836

print(f"The movie {movie['title']} had a budget of ${movie["budget"]:,}")
print(f"The movie {movie['title']} generated revenue of ${movie["revenue"]:,}")

# If the movie cost more to make than it made in theaters, print "That was a bad investment". If the film's revenue was more than five times the amount it cost to make, print "That was a great investment." Otherwise print "That was an okay investment."
print("====== QUESTION 3 ======")
if movie['budget'] > movie['revenue']:
    print("That was a bad investment")
elif movie['revenue'] > (5*movie['budget']):
    print("That was a great investment")
else:
    print("That was an okay investment")

# Sometimes dictionaries are used to describe the same aspects of many different objects. Make ONE dictionary that describes the population of the boroughs of NYC. Manhattan has 1.6 million residents, Brooklyn has 2.6m, Bronx has 1.4m, Queens has 2.3m and Staten Island has 470,000. (Tip: keeping it all in either millions or thousands is a good idea)
print("====== QUESTION 4 ======")
populations = {
    "Manhattan": 1.6,
    "Brooklyn": 2.6,
    "Bronx": 1.4,
    "Queens": 2.3,
    "Staten Island": 0.47
}

# Display the population of Brooklyn.
print("====== QUESTION 5 ======")
print(f"{populations["Brooklyn"]} million people")

# Display the combined population of all five boroughs.
print("====== QUESTION 6 ======")
sum_populations = sum(populations.values())
print(f"The combined population of all five boroughs is {sum_populations} million people.")

# Display what percent of NYC's population lives in Manhattan.
print("====== QUESTION 7 ======")
manhattan_pct = populations["Manhattan"]/sum_populations
print(f"Manhattan's population is {manhattan_pct:.2f}% of the population of NYC.")