# Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

age = input()

y = 90 - int(age)
w = y * 52

print(f"You have {w} weeks left.")