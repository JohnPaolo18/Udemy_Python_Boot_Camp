#Even 2 4 6 8 10
#Odd 1 3 5 7 9

user_input = input("Please enter a number:")
integer_num = int(user_input)

divided_number = (integer_num % 2)

if divided_number == 0:
    print("Even")
else:
    print("Odd")