
s = input("Enter a number :")
try:
    num = int(s)
    print(100/num)
except ValueError:
    print("Sorry! Invalid number. Please try again!")
else:
    print("Done")
finally:
    print("Over")


print("The End")




