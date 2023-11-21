def addDigits(num):
    while num >= 10:
        num_str = str(num)
        total = 0
        for digit in num_str:
            total += int(digit)
        num = total
        print(num)
    return num
print(addDigits(199))