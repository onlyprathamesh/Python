print("Average height calcualtor!")

student_heights = input("Input names of students : ").split(" ")

for n in range (0, len(student_heights)) :
    student_heights[n] = int(student_heights[n])
print(student_heights)

height = 0
for n in student_heights :
    height += n

num = 0
for x in student_heights :
    num += 1

averange_height = round(height / num)
print(f"Average height of students in class is : {averange_height}")