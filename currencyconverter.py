with open ("converter.txt","r") as f:
    lis=[]
    lis1=[]
    dict={}
    lis2=[]
    data=f.read()
    datasplit=data.split("\n")
    for i in range(0,len(datasplit)-1):
        newdatasplits=datasplit[i].split("\t")
        lis1.append(newdatasplits[0])

        lis2.append(newdatasplits[2][:5])
    f.close()
    for j in range(0,len(lis1)):
        dict[lis1[j]]=lis2[j]
    print(dict)
    def hai(a,b):
        c=0
        if a in dict:
            c=dict[a]
            d=float(c)*b
            return d
    a = input("Enter the country")
    b = float(input("Enter the value"))
    f=hai(a,b)
    print(f)






