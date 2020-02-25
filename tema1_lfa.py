from graphviz import Digraph
#programul normal

#variabilele
st_initial=0
st_final=[]
adiacenta={}
n=0
parcurse=[]
traducere=[]
def citire():
    global adiacenta,st_final,st_initial,traducere
    f=open("date.in")
    n=int(f.readline())
    st_initial=f.readline()[0]
    sir=f.readline()
    st_final=sir.split()
    sir=f.readline()
    while (sir):
        l=sir.split()
        for i in range(2):
            if (l[i] not in traducere):
                traducere.append(l[i])
        if (adiacenta.get(l[0])==None):
            adiacenta[l[0]]={}
            adiacenta[l[0]][l[1]]=[l[2]]
        else:
            if(adiacenta[l[0]].get(l[1])==None):
                adiacenta[l[0]][l[1]]=[l[2]]
            else:
                adiacenta[l[0]][l[1]].append(l[2])
        sir=f.readline()

#verificarea inputului

def check_input(sir):
    if (sir!="" and sir!="λ"):
        ex_litere=0
        ex_cifre=0
        drum=[]
        for x in sir:
            drum.append(x)
            if (x.isdecimal()):
                ex_cifre=1
            elif (x in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYZ"):
                ex_litere=1
            else:
                ex_cifre=2 # datele sunt gresite
        if (ex_cifre+ex_litere==1):
            parcurgerea_cuvantului(drum)
        else:
            print("Drumul este gresit")
    else:
        if (st_initial in st_final):
            print("Da")
        else:
            print("Drumul e gresit")

#parcurgerea cuvantului

def parcurgerea_cuvantului(drum):
    global adiacenta,st_final,st_initial,n,parcurse
    poz=st_initial
    log=0
    for x in drum:
        for k in adiacenta[poz].keys():
            if (x in adiacenta[poz][k]):
                parcurse.append((poz,k))
                poz=k
                break
        else:
            log=1
    if (poz not in st_final):
        log=1
    if (log==0):
        print("Da")
    else:
        print("Drumul este gresit")

citire()
cuvant=input("Introduceti cuvantul")
check_input(cuvant)
print(adiacenta)
print(parcurse)
print(traducere)
#grafica
nod_desenat=[0]*n
g=Digraph(name="Automat",filename="fisier.pdf")
g.attr('node',shape='doublecircle')
for x in st_final:
    g.node(x)
g.attr('node',shape='circle')
for x in traducere:
    if (x not in st_final):
        g.node(x)
for x in adiacenta.keys():
    for k in adiacenta[x].keys():
        if (adiacenta[x][k]!=[]):
            for v in adiacenta[x][k]:
                if ((x,v) in traducere):
                    g.attr('edge',color='green')
                    g.edge(x,k,v)
                else:
                    g.attr('edge',color='black')
                    g.edge(x,k,v)
g.view()
