
#Sequential Data Lists, 
courses =  ["History", "math", "physics", "Comp Sci"]
print(courses)
print(len(courses))
print(courses[0])
print(courses[3])
print(courses[-1])  #negative goes from the back of the list, length does not matter
print(courses[0:2]) #first included, last not included
print(courses[:2])
print(courses[2:])

#modification
mods = ["History", "math", "physics", "Comp Sci"]
mods.append("Art")
print(mods)
mods.insert(0,"Art")
print(mods)

mods_2 = ["education", "tennis"]
mods.extend(mods_2)
print(mods)

#remove
getRid = ["History", "math", "physics", "Comp Sci"]
getRid.remove("math")
print(getRid)
var = getRid.pop() #returns what is removed
print(getRid)
print(var)

#Sorting
sorts = ["History", "math", "physics", "Comp Sci"]
sorts.reverse()
print(sorts)
sorts.reverse()
sorts.sort()
print(sorts)
nums = [1,5,4,3]   #numbers sorted in ascending order, letters alphebetically
nums.sort()
print(nums)
nums.reverse()
print(nums)
nums.sort()
nums.sort(reverse=True)  #descending order, numerically or alphebetically
print(nums)
sorts =  ["History", "math", "physics", "Comp Sci"]
print(sorts)
print(sorted(sorts)) # returns sorted function

#minmaxsum
print(min(nums))
print(max(nums))
print(sum(nums))


#indexes
spice = ["History", "math", "physics", "Comp Sci"]
print(spice.index("Comp Sci"))
print("math" in spice) #boolean checks if present'
print('art' in spice)

#loops
for item in enumerate(spice, start=1):  #enumerate allows for value and index in loop, starts modifies what index is used as
    print(item)

spice_str = ', '.join(spice) #turn it into a string as well as format it
print(spice_str) 
new_spice = spice_str.split(", ") # same but backwards
print(new_spice)

#tuples, can't modify tuples, immutable
tuple_1 = (1,2,3,4)
print(tuple_1) #can't change it

#sets
testset = {"History", "Math", "Physics", "Comp Sci", "History", "Math", "Physics", "Comp Sci", "Boogaloo"} #get rid of duplicates
arts = {"History", "Math", "Physics", "Comp Sci", "Art", "Design"}
print(testset)
print("Math" in testset) #optimized for searching
print(testset.intersection(arts))#shows what is in common
print(testset.difference(arts))#what is different
print(testset.union(arts))#combine all individual values

#empty lists tuples and sets
empty_list = []
empty_tuple = ()
empty_set = set()