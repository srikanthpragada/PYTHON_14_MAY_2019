p = n = z = 0
for i in range(1,6):
    num = int(input("Enter a number :"))
    if  num > 0:
        p += 1
    elif num < 0:
        n +=1
    else:
        z +=1

print(f"Positives : {p}, Negatives : {n}, Zeros : {z}")
