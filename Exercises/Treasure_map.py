# Marking an 'X' on the map.

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

a = position[0]
if a == 'A':
  x = 0
elif a == 'B':
  x = 1
elif a == 'C':
  x = 2

b = int(position[1])

map[b-1][x] = 'X'

print(f"{line1}\n{line2}\n{line3}")