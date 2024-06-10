# write a program that calculates the highest score from a List of scores, without using max() function.

# Input a list of student scores
student_scores = input().split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

m = 0
for i in student_scores :
  if i > m :
    m = i

print("The highest score in the class is:",m)