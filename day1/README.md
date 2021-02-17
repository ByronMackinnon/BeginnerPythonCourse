# Datatypes
## Integer (int)
This would be any full number. From -infinity to +infinity including 0.
- 1
- 2
- 14
- 0
- -23
- -543

## String (str)
This would be any data type held within a variable that is encased in quotations, including numbers. This could be double or single quotes. "Test" would be the same as 'Test'. Quotation types cannot be mismatched however. Ex: "Incorrect' or 'Wrong"
- "Hello"
- "World"
- "True"
- "False"
- "None"
- "123"
- "1"
- "1.23"

## Boolean (bool)
A boolean would simply be a True/False or a Yes/No relationship. A boolean is only able to be 1 of these 2 options.
- True
- False

## Float (float)
A float would be any floating point number. So essentially any number that has a decimal point in it. Positive or Negative.
- 0.123
- -12.3

## Iterables
### List (list)
A list is a mutable iterable. This means it can be changed dynamically. You can change elements, or add to it easily. Denoted using square brackets. **[]**

Ex: `[“Apple”, “Banana”, “Strawberry”, “Grape”]`

### Tuple (tuple)
A tuple is a immutable iterable. Meaning it is as the data type stands. It is unable to be changed dynamically. Denoted using rounded brackets / Parenthesis **()**

Ex: `(“Baseball”, “Basketball”, “Football”,)`

## Variable
A variable would be a name you created to hold ***ANY*** specified data type. This would be done by assigning a name to a data type.

```python
name = "Byron"
age = 24
```

Variables are not able to be named with a number at the beginning, and are limited to alpha-numeric characters. (a-z, 0-9, \_). Captial letters do matter and will create a different variable.

It is common practice for variables to be lowercase and any spaces would be turned into underscores.

```python
date_of_birth = "October 6th, 1996"
```

## Input
An input can be captured if we wanted to get user-defined data from someone using our program.

```python
name = input("Hello, what is your name?")
```

Then when the program is run, the name variable will capture the input, placed in by the user. This will always be captured as a string however.

## Operators
Operators would be in reference to a mathematical operation.

Name | Symbol
---- | -----
Addition | +
Subtraction | -
Multiplication | *
Division | /
Exponent | **
Floor Division | //
Modulus Division | %

## Comparisons

Name | Symbol
---- | ------
Greater Than | >
Greater Than or Equal To | >=
Less Than | <
Less Than or Equal To | <=
Equivalent | ==
Not Equivalent | !=

## Conditions
### if Statements
If statements are used to set conditional code to be executed. You would use this in the event something specific happens.

```python
name = "Byron"
user_name = input("What is your name?")
if name == user_name:
    print("Wow! We have the same name!")
elif user_name == "Daniel":
    print("Cool! That's my middle name. Hello.")
else:
    print("Hello, " + user_name)
```

### While
While loops would be used to continuously execute code until the condition is no longer met.

```python
loop  = True
while  loop:
	name = input(“input something”)
	if  name == “stop”:
		loop  = False
```

### For
For loops would be used in the event you want to iterate through a data type. This will iterate through the entire data type until it is exhausted.

```python
fruits  = [“apple”, “banana”, “pear”, “orange”]
for fruit in fruits:
    print(fruit)
```
