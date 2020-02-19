f=open('date.in')# fisier de forma: nr noduri \n starea initiala\n starea finala\ {nod1,nod2,arc}...
n=int(f.readline())
st_initial=f.readline()[0]
sir=f.readline()
st_final=sir.split()
adiacenta=[[[] for i in range (n)]for j in range (n)]
sir=f.readline()
traducere=[]
print(adiacenta)
while (sir):
    l=sir.split()
    for i in range(2):
        if(l[i] not in traducere):
            traducere.append(l[i])
    adiacenta[traducere.index(l[0])][traducere.index(l[1])].append(l[2])
    sir=f.readline()
print(adiacenta)
sir=input("Introduceti cuvantul")
ex_litere=0
ex_cifre=0
drum=[]
for x in sir:
    drum.append(x)
    if(x.isdecimal()):
        ex_cifre=1
    elif (x in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYZ"):
        ex_litere=1
    else:
        ex_cifre=2
print(st_initial)
print(st_final)
print(traducere)
if (ex_litere+ex_cifre==1):
    print(st_initial)
    poz=traducere.index(st_initial)
    st_final_numere=[]
    for x in st_final:
        st_final_numere.append(traducere.index(x))
    print(st_final_numere)
    log=0
    for x in drum:
        for k in range(n):
            if (x in adiacenta[poz][k]):
                poz=k
                print(poz)
                break
        else:
            log=1
    if(poz not in st_final_numere):
        log=1
    if (log==0):
        print("Da")
    else:
        print("Drumul este gresit")
else:
    print("Drumul este gresit")
