#Hello:)

#Positive index refers to 0 - 9
#Negative index starts at back goes from -1 to -10
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]


print(my_list)
print(my_list[-1])
print(my_list[-10])

#slicing, list[start:end:step]
print(my_list[0:6])
print(my_list[3:8])
print(my_list[-7:-2])
print(my_list[1:-2])
print(my_list[1:])
print(my_list[:-1])
print(my_list[:])

#step allows to skip values
print(my_list[2:-1:2]) #skips every 2nd value

#how to print backwards, reverse it man
print(my_list[-1:2:-1])
print(my_list[-2:1:-1])

print( my_list[::-1])

#Strings
sample = 'http://coreyms.com'
print(sample)
print(sample[::-1]) #Reverse string
print(sample[-4:])
print(sample[7:])
print(sample[7:-4])