# Print marks that are > avg. marks
f = open("marks.txt", "rt")
lines = f.readlines()
f.close()
marks = []
for line in lines:
    try:
        num = int(line.strip("\n"))
        if num >= 0 and num <= 100:
            marks.append(num)
    except:
        pass

avg_marks = sum(marks) / len(marks)
print("Average Marks : ", avg_marks)
for m in marks:
    if m > avg_marks:
        print(m, end=" ")
