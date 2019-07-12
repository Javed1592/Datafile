z = (1 + 2 + 3/
     4 + 5 + 6/
     7 + 8 + 9)
print(z)
a = b = c = 4
print(id(c))  # a --> 2000120944
                # if it is a string value then the address to every variable will differ


a = 1+2j
print(type(a))
print(isinstance(a,complex))


s = '''I am shaik javed'''

print(s[4:])
print(s[4:10])
print(s[4:18:2])

#List
a = [1, 2.5, 'Javed']
a[1] = 4
print(a)

#Tuple
b = (1, 3.4, 'ML')
print(b)

#Set
c = {10,10,10,20,30,20,30}
print(c)

#Dictionaries

d = {'a': 'Aunty', 'u': 'Uncle'}
print(d['u'])


#Datatype conversion

print(float(6))
print(int(4.5))
s =list("Javed")
print(s)
l = ['a','ab','abc']
print(type(l))
sl =set(l)
print(sl)
print(type(sl))


##Basic Input and Output in python


a = 10 ; b = 20
print("The value of a is {} and b is {}".format(a,b))

print("The value of a is {1} and b is {0}".format(a,b))

print("Welcome {Name} {Greetings}".format(Name="Javed",Greetings="Good Morning!!"))

print("This is {0} and I belongs to {1} and {other}".format("Javed","CenturyLink",other="India"))


a = input("Enter the value of a : ")
print(a)

