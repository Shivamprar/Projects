import string,random
def hello():
    plen=int(input("enter the lenght u want to generate for the password can't be more than 30"))
    s1=string.ascii_lowercase
    c,d,e,f="","","",""
    a=""
    for i in range(0,10):
        c+=random.choice(s1)
    s2=string.ascii_uppercase
    for i in range(0, 15):
        d += random.choice(s2)
    s3=string.digits
    for i in range(0, 5):
        e += random.choice(s3)
    s4=string.punctuation
    for i in range(0, 5):
        f += random.choice(s4)
    a += c + d + e + f
    g = random.sample(a, plen)
#program to see if it exist or not
    if (f not in g) or (e not in g):
        h = random.sample(e, 1)
        v = random.sample(f, 1)
        n = h + v
        g=g[0:len(g)-2]+n
    else:
        g = random.sample(a, plen)
    a=""
    for file in g:
        a+=file
    return a
o=hello()
print(o)

