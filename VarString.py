
#spaces represented by _, aslo use descriptive names
message  = "Hello World"

print("Hello \" World")
print(message)

test_message = """Bobby\'s world was a good
cartoon in the world"""

print(test_message)

#len function
print(len(message))
print(message[0] + message[10])
print(message[0:5])
print(message[:5])
print(message[6:])
print(message[6:11])

#string function
print(message.lower())
print(message.upper())

#Count shows all instances of the argument
print(message.count("Hello"))
print(message.count("l"))

#find gives index, gives first instance of
print(message.find("World"))
print(message.find("l"))

#replace returns a new string with modification in place, replaces all instances of first argument with second  (you can set it equal to itself)
replaceMessage = message.replace("World", "Universe")
print(replaceMessage)

#Concatenation + format
a_message = "Hello"
b_message = "World C"
# c_message = a_message + " " + b_message + ". Go away plz"
# c_message = "{}, {}. go away plz ,,,, \"'    ".format(a_message,b_message)
c_message = f"{a_message}, {b_message.upper()}. please go away my dude"
print(c_message)

#print(dir(message)) gives methods for variable type, too see morea bout methods use help function,  print(help(str)), print(help(str.lower))
