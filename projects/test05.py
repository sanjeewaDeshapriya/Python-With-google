def slice_PNO(pno):
    ccode=pno[:3]
    exchange=pno[3:6]
    tail =pno[-4:]
    return "("+ccode+")"+" "+exchange+" "+ tail


while True:
    print("Input mobie contactg number")
    no = input()
    if no=="e":
        break
    elif len(no)==10:
        print(slice_PNO(no))
    else:
        print("youer enterd  no is incorect pase check that again ")
    
