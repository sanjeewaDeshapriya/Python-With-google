name = "Sanjeewa deshapriya"

#String slicing

print(name)
print(name[0:4])
print(name[:4])
print(name[4:])
print(name[-1:5])

#string indexing

print(name.index("e"))
print(name.index("jeewa"))
print(name.index("hap"))

#string item count

print(name.count("e"))
print(name.count("esh"))

#is in in string 

print("San" in name)
print("Sanjeewa" in name)

animals = "lions tigers and bears"
print("tigers" in animals)

#variabale case
print(name.upper())
print(name.lower())

#strip remove spaces and the make shorter and clean 
print(" yes")
print(" yes".strip())
verb =" cat     "
print(verb.lstrip())
print(verb.rstrip())

#split and joiun the strings 

name="Hi my name is sanjeewa deshappriya"
namesplit=name.split()
print(namesplit)
print("_".join(namesplit))

#isnumeric to find the valus is numeric or not 
age="12"
print(name.isnumeric())
print(age.isnumeric())