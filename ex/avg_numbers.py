count = 1
sum = 0

while count <= 5:
    try:
        num = int(input("Enter number :"))
        sum += num
        count += 1
    except:
        print("Invalid number. Please try again!")


print(sum / 5)
