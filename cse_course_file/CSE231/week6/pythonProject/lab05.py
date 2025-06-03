file_name = input("Input a file: ")

while True:
    try:
        with open(file_name, 'r') as file:
            file_object = file.read()
        print()
        print(f"{'Name':20s}{'Exam1':>6s}{'Exam2':>6s}{'Exam3':>6s}{'Exam4':>6s}{'Mean':>10s}")
        break
    except FileNotFoundError:
        print("\nFile does not exist.")
        file_name = input("Input a file: ")

from operator import itemgetter
file_org = 'scores.txt'
file_object = open(file_org, 'r')
sum1 = 0
sum2 = 0
sum3 = 0
sum4 = 0
student_data_indi = []
student_data = []

for line in file_object:
    word = line.split()
    name = word[0] + ' ' + word[1]
    exam1 = word[2]
    exam2 = word[3]
    exam3 = word[4]
    exam4 = word[5]
    mean = (int(exam1) + int(exam2) + int(exam3) +int(exam4)) / 4
    sum1 += int(exam1)
    sum2 += int(exam2)
    sum3 += int(exam3)
    sum4 += int(exam4)

    student_data_indi = [name, exam1, exam2, exam3, exam4, mean]
    student_data.append(student_data_indi)

student_data_sorted = sorted(student_data, key = itemgetter(0))
for i in range(0, len(student_data_sorted)):
    print(f"{student_data_sorted[i][0]:20s}{student_data_sorted[i][1]:>6s}{student_data_sorted[i][2]:>6s}{student_data_sorted[i][3]:>6s}{student_data_sorted[i][4]:>6s}{student_data_sorted[i][5]:>10.2f}")

avg1 = round((sum1 / 5),1)
avg2 = round((sum2 / 5),1)
avg3 = round((sum3 / 5),1)
avg4 = round((sum4 / 5),1)
print(f"{'Exam Mean':20s}{str(avg1):>6s}{str(avg2):>6s}{str(avg3):>6s}{str(avg4):>6s}")
file_object.close()





