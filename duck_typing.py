#hello :)

#pythonic following conventions
#duck typing, ask forgivness not permission

class Duck:

    def quack(self):
        print('Quack,Quack')
    def fly(self):
        print('Flap,Flap')

class Person:

    def quack(self):
        print('I\'m qucking like a duck!')
    def fly(self):
        print('I\'m flapping my arms!')


def quack_and_fly(thing): #what object it is does not matter only if it can do what it is told
    if isinstance(thing,Duck):
        thing.quack()
        thing.fly()
    else:
        print('This had to be a duck')
    print()


def quacks(thing): #runs, if it doesn't work handle the error(ask for forgivness)
    try:
        thing.quack()
        thing.fly()
    except AttributeError as e:
        print(e)

d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)