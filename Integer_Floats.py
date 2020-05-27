
#intro to floats and integers
num = 3
print(type(num))

print(num + 2)
print(num - 2)
print(num * 2)
print(num / 2)
#floor division, drops decimals
print(num // 2) 
print(num ** 2)
print(num % 2)
print(100 % 50)
print(30 % 4)
print(3 + (2 * 4))


test = 1
test = test + 1
test += 1
test*= 10
print(test)

#absolute value
neg = -3
print(abs(neg))

print(round(3.75))
print(round(3.75,1))

#comparing
high = 3
low = 2
print(high == low)
print(high != low)
print(high > low)
print(high < low)
print(high >= low)
print(high <= low)

#integer to string ish
stringMessage = "100"
stringMessage_2 = "200"

stringMessage = int(stringMessage)
stringMessage_2 = int(stringMessage_2)
print(stringMessage + stringMessage_2)
