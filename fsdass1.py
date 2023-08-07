
def sum_digits(num):
    sum = 0
    while(num > 0):
        rem = num % 10
        sum = sum + rem
        num = num // 10
    return sum


inp = [120, 20, 42, 212, 802, 139, 175, 802, 468]
print("Input List = ", inp)
print("Maximum Value in the List = ", max(inp, key = sum_digits))
