#def functionWithNoArgLimit(id,names):
    #print(names)
    #print(id)
#functionWithNoArgLimit(10,"Daravuth","Phnom Penh")


def functionWithNoArgLimit(*names):
    for name in names:
        print(name)
functionWithNoArgLimit("Daravuth","Sarapich","Sen")