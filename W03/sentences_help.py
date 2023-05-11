import random

# Create a list of strings and assign
# the list to a variable named words.
words = ["boy", "girl", "cat", "dog", "bird", "house"]

# Call the random.choice function which will choose
# one string from the words list. Store the chosen
# string in a variable named word.
word = random.choice(words)

print(word)





given = "Michelle"
middle = "Aya"
surname = "Takechi"

full_name = f"{given} {middle} {surname}"
print(full_name)