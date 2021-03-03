# Conditions
A condition is simply a boolean (a yes or no relationship).

```py
age = 0 # This is assigning the variable.

print(age == 1) # This is the condition. Age does not currently equal 1, so this is the same as `print(False)`
```

This would print a `False` to the console. If we changed it to say `age == 0` that would be a True statement, so it would print `True` to the console.

This isn't the only example of a condition however. Conditions can be used in a while loop as well.

```py
# We will set the loop to increase a number until it reaches 10, where it will stop.

number = 1

while number < 10:
    print(number)
    number = number + 1

# [OUTPUT]
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
```

This is because the number is less than 10, until it reaches the number 10. Obviously.

## If / Elif / Else
If conditionals are used in specific circumstances where you want specific code, to do specific things.

```py
if condition == True:
    pass #this code will be executed

elif other_condition == True:
    pass #if the first condition isn't true, it will try to do this

elif other_other_condition == True:
    pass #if the 2 other conditions fail, this one will try. You can put as many `elif`s as you need.

else:
    pass #if everything else fails, this will happen no matter what.
```

```py
name = Input("What is your name?")
if name == "Byron":
    print("Hey, we have the same name!")

elif name == "Daniel":
    print("Hey, that's my middle name. Cool!")

else:
    print("Hello " + name)
```

This is also the case for nested if statements. For example.
```py
x = 2
y = 3

if x == 2:
    if y == 3:
        print("x = 2, y = 3")
    else:
        print("x = 2, y != 3")
else:
    print("x != 2")
```

You can also use if statements in conjunction with for loops, or while loops.
```py
#This is just a huge list of fruits, the actual fruits is irrelavent.
fruits = ["Apple", "Apricot", "Avocado", "Banana", "Bilberry", "Blackberry", "Blackcurrant", "Blueberry", "Boysenberry", "Currant", "Cherry", "Cherimoya", "Chico fruit", "Cloudberry", "Coconut", "Cranberry", "Cucumber", "Custard apple", "Damson", "Date", "Dragonfruit", "Durian", "Elderberry", "Feijoa", "Fig", "Goji berry", "Gooseberry", "Grape", "Raisin", "Grapefruit", "Guava", "Honeyberry", "Huckleberry", "Jabuticaba", "Jackfruit", "Jambul", "Jujube", "Juniper berry", "Kiwano", "Kiwifruit", "Kumquat", "Lemon", "Lime", "Loquat", "Longan", "Lychee", "Mango", "Mangosteen", "Marionberry", "Melon", "Cantaloupe", "Honeydew", "Watermelon", "Miracle fruit", "Mulberry", "Nectarine", "Nance", "Olive", "Orange", "Blood orange", "Clementine", "Mandarine", "Tangerine", "Papaya", "Passionfruit", "Peach", "Pear", "Persimmon", "Physalis", "Plantain", "Plum", "Prune", "Pineapple", "Plumcot", "Pomegranate", "Pomelo", "Purple mangosteen", "Quince", "Raspberry", "Salmonberry", "Rambutan", "Redcurrant", "Salal berry", "Salak", "Satsuma", "Soursop", "Star fruit", "Solanum quitoense", "Strawberry", "Tamarillo", "Tamarind", "Ugli fruit", "Yuzu"]

starting_letter = input("Enter a letter. I will return all fruits that start with that letter! ")

custom_fruits = []

for fruit in fruits: #this is go through the entire list, fruit by fruit.
    if fruit.startswith(starting_letter):
        custom_fruits.append(fruit)

# Now, if you enter I, O, V, W, X, or Z, there will be no fruits found. 
# Since none of the fruits in the list start with those letters. 
# We will be printing an empty list. 
# We can use this to our advantage by using another if statement.

if custom_fruits == []: # This is stating, if our variable is still an empty list (no fruits were found), then do x
    print("No fruits were found starting with the letter " + starting_letter)

else:
    print(custom_fruits)
```
