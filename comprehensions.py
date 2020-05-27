#hello :)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

#C
your_list = [n for n in nums]
print(your_list)

our_list = []
for n in nums:
    our_list.append(n * n)
print(our_list)

#C
we_list = [n * n for n in nums]
print(we_list)

#Something about maps idk

even_list = []
for n in nums:
    if(n % 2 == 0):
        even_list.append(n)
print(even_list)

#C with if check?
c_even_list = [n for n in nums if (n % 2 == 0)]
print(c_even_list)

#C nested
ex_list = [(letter,num) for letter in "abcd" for num in range(4)]
print(ex_list)

#Dictionary Comprehension
names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

my_dict = {}
for name,hero in zip(names,heros):
    my_dict[name] = hero
print(my_dict)

c_dict = {name:hero for name, hero in zip(names,heros)}
print(c_dict)

d_dict = {name:hero for name, hero in zip(names,heros) if name != 'Peter'}
print(d_dict)


#Set Comprehensions
vals = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9,]
my_set = set()
for n in vals:
    my_set.add(n)
print(my_set)

c_my_set = {n for n in vals}
print(c_my_set)

#Generation expressions???
def gen_func(nums):
    for n in nums:
        yield n*n
my_gen = gen_func(nums)
#print(my_gen)