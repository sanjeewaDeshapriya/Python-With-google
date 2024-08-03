#string formating 
name = "sanju"
age=24
print("hi {} your age is {}".format(name,age))
print("hi {name} youre age is {age}".format(age=age,name=name))

packet_price=20
count =2.5
print("one get ${:.2f} and full cost is ${:.2f}".format(packet_price,packet_price*count))


def celtofra(c):
    return(c-32)*9/5

for i in range (0,201,10):
    x=celtofra(i)
    print("{:>3}C | {:>6.2f}F ".format(i,x))

def nametag(first_name, last_name):
    return first_name+" {}.".format(last_name[0].upper() )


print(nametag("Jane","Smith")) 
# Should display "Jane S." 
print(nametag("Francesco","Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc","Grand-Pierre")) 
# Should display "Jean-Luc G." 