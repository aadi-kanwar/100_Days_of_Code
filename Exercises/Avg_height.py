# Write a program that calculates the average student height from a List of heights.
# For loop practice

# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

c = 0
sum = 0
for i in student_heights :
  sum += i
  c += 1
print("total height =",sum)
print("number of students =",c)
avg = round(sum / c)
print("average height =",avg)