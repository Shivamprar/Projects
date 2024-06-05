from functools import reduce
import math
count=0

tempnumber=0
def armstrong(number):
    global tempnumber
    tempnumber=number

    global count
    lis=[]
    while(number>0):
        n = number % 10
        lis.append(n)

        number=number//10

        count+=+1


    return lis
def checknumber(vlis):
    sum=0
    for i in range(0,len(vlis)):
        d=vlis[i]**count

        sum+=int(d)
    return sum



an=armstrong(153)

h=checknumber(an)

if(h==tempnumber):
    print("no is armstrong")
else:
    print("not armstrong")