# For this exercise I want you guys to imagine there is a roller coaster, and you are only allowed to ride the rollercoaster if you are between 1-2 meters tall.

# You will have to use conditional statements, using if/elif/else statements to determine whether someone can ride on the rollercoaster or not.

# Note: When using the `input()` function, even if you enter a number, it is returned as a STRING. So it will have to be converted into an INTEGER before you can use comparisions on it.

height = input("How tall are you? (in meters) ")
height = int(height)

if height < 1:
    print("You cannot ride, under 1 meter.")

elif height > 2:
    print("You cannot ride, over 2 meters.")

else:
    print("You can ride the rollercoaster.")