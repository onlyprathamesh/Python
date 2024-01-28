student_score = input("Input list of students : ").split(" ")
for n in range (0, len(student_score)) :
    student_score[n] = int(student_score[n])
print(student_score)

num = 0
for score in student_score :
    if num < score :
        num = score

print(f"Highest score in the list is : {num}")