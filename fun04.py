def greater(num1,num2,num3):
    if num1>num2 and num3<num1:
        return num1
    elif num2>num1 and num3<num2:
        return num2
    else:
        return num3

big=greater(90,80,97)
print(big)
