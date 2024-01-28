print("Welcome to Love Calculator program!!!")


name_1 = input("Enter your name : ")
name_2 = input("Enter their name : ")

name_1_lower = name_1.lower()
name_2_lower = name_2.lower()

combined_name = name_1_lower + name_2_lower

letter_t = combined_name.count("t")
letter_r = combined_name.count("r")
letter_u = combined_name.count("u")
letter_e = combined_name.count("e")

total_1 = int(letter_t) + int(letter_r) + int(letter_u)+ int(letter_e)

letter_l = combined_name.count("l")
letter_o = combined_name.count("o")
letter_v = combined_name.count("v")
letter_e = combined_name.count("e")

total_2 = int(letter_l) + int(letter_o) + int(letter_v) + int(letter_e)

total = int(str(total_1) + str(total_2))

if total < 10 or total > 90 :
    print(f"Your Love score is : ***{total}***, you go together like coke and mentos.")
elif total > 40 and total < 50 :
    print(f"Your Love score is : ***{total}***, you are alright together.")
else :
    print(f"Your Love score is : {total}.")

