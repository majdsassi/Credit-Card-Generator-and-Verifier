def num():
    ok = False
    while not(ok):
        x = int(input('How Many Card You Want To Generate  : '))
        ok = 1 <= x <= 10000
    return x
def month():
    x = randint(1,12)
    if x < 10 :
        x = str(x)
        x = '0'+x
    return str(x)
def year():
    x = randint(2023,2028)
    return str(x)
def ccv():
    ccv = randint(100,999)
    return str(ccv)
def gen() :
    global l
    x= Bin()
    l = []
    l.append('-----------------------------------------Credit Cards-----------------------------------------')
    n = num()
    for i in range(n):
        ok = False
        while not(ok):
            nume = str(x)+str(randint(1000000000,9999999999))
            ok = luhn(nume)==True
        mm = month()
        yy = year()
        Ccv = ccv()
        card = nume+'|'+mm+'|'+yy+'|'+Ccv
        l.append(card)
def Bin() :
    ok = False
    while not(ok):
        x = int(input('Enter Your Bin Code (Example : 459896 / 491653 / 520402 ) : '))
        ok = 400000 <= x <= 599999
    return x
def luhn(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    if (checksum % 10)== 0 :
        return True
    else :
        return False
def save(l):
    today = datetime.now()
    D = str(today.strftime("%m-%d-%y %Hh%Mmin%Ssec"))
    name = "credit cards "+D+'.txt'
    with open(name,"w") as file :
        for line in l :
            file.write(line)
            file.write('\n')
    file.close()
    print("Your Credit Card Are Saved In File Called 'Credit Cards(the current date and time ).txt'")
from random import randint
from datetime import datetime
gen()
l.append('-----------------------------------------Developed By majd sassi-------------------------------------------')
save(l)
