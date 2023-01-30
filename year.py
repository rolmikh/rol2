leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]
no_leap_year = [31,28,31,30,31,30,31,31,30,31,30,31]
summa = 0
print("Введите год:")
year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    for number in leap_year:
        for number1 in range(0,number + 1,1):
            while (number1 != 0):
                summa = summa + number1 % 10
                number1 = number1 // 10
    print (summa)
else:
    for number in no_leap_year:
        for number1 in range(0,number + 1,1):
            while (number1 != 0):
                summa = summa + number1 % 10
                number1 = number1 // 10
    print (summa)



# 2022 - 2030
# 2020 - 2041
