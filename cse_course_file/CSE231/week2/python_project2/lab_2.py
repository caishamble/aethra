

odd_sum = 0
even_sum = 0
odd_count = 0
even_count = 0
positive_int_count = 0


while True:
    n = int(input("\nInput an integer (0 terminates): "))
    if n == 0:
        break
    else:
        if n > 0:
            positive_int_count += 1
        if n %2 ==0 and n >0:
            even_sum += n
            even_count += 1
            continue
        elif n %2 !=0 and n >0:
            odd_sum += n
            odd_count += 1
            continue


#Do not change the following lines of code
print("\n")
print("sum of odds:", odd_sum)
print("sum of evens:", even_sum)
print("odd count:", odd_count)
print("even count:", even_count)
print("total positive int count:", positive_int_count)