nums = []
pnum = 0
while True:
    try:
        num = int(input("Enter a number [0 top stop] :"))
    except:
        print("Sorry! Invalid number!")
        continue

    if num == 0:
        break

    if num >=  pnum:
        nums.append(num)
        pnum = num


print(nums)
