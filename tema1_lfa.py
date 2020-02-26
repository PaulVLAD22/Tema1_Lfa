from graphviz import Digraph
class Automat:
    def __init__(self,f):
        self.nr=int(f.readline())
        self.st_initial=f.readline()[0]
        self.st_final=f.readline().split()
        self.parcurse=[]
        traducere=[]#nodurile
        adiacenta={}# legaturile dintre noduri
        sir=f.readline()
        while (sir):
            l = sir.split()
            for i in range(2):
                if (l[i] not in traducere):
                    traducere.append(l[i])
            if (adiacenta.get(l[0]) == None):
                adiacenta[l[0]] = {}
                adiacenta[l[0]][l[1]] = [l[2]]
            else:
                if (adiacenta[l[0]].get(l[1]) == None):
                    adiacenta[l[0]][l[1]] = [l[2]]
                else:
                    adiacenta[l[0]][l[1]].append(l[2])
            sir = f.readline()
        self.adiacenta=adiacenta
        self.traducere=traducere
        print(adiacenta)
    def check_input(self):
        cuvant=input("Introduceti cuvantul in automat")
        if (cuvant==""):
            if(self.st_initial in self.st_final):
                print("CORECT")
            else:
                print("GRESIT")
        else:
            ex_litere=0
            ex_cifre=0
            drum=[]
            for x in cuvant:
                drum.append(x)
                if (x.isdecimal()):
                    ex_cifre=1
                elif(x in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYZ"):
                    ex_litere=1
                else:
                    ex_cifre=2 #date gresite
            if (ex_litere+ex_cifre==1):
                return drum
            else:
                print("GRESIT")
        return 0
    def parcurgerea_cuvantului(self,drum):
        poz=self.st_initial
        log=0
        for x in drum:
            for k in self.adiacenta[poz].keys():
                if(x in self.adiacenta[poz][k]):
                    self.parcurse.append((poz,k))
                    poz=k
                    break
                    print(poz)
            else:
                log=1
        if (poz not in self.st_final):
            log=1
        if (log==0):
            print("Da")
        else:
            print("Drumul este gresit")

class Nod:
    def __init__(self,automat,val):
        self.val=val
        if (val in automat.st_final):
            self.final=1 #boolean
        else:
            self.final=0
        if (val==automat.st_initial):
            self.initial=1
        else:
            self.initial=0
    def desenare(self,g):
        if (self.final==1):
            g.attr('node',shape="doublecircle")
        else:
            g.attr('node',shape="circle")
        if (self.initial==1):
            g.node('', shape='none')
            g.node(self.val)
            g.edge('', self.val, label='START')
        else:
            g.node(self.val)




#programul
f=open("date.txt") #fisier de forma: nr noduri/ st_init/ st_finala/ legatura1 / legatura2/...
a=Automat(f)
drum=a.check_input()
if (drum!=0):
    a.parcurgerea_cuvantului(drum)
print(a.parcurse)


#grafica
g=Digraph(name="Automat",filename="fisier.pdf")
for x in a.traducere:
    nod=Nod(a,x)
    nod.desenare(g)
for x in a.adiacenta.keys():
    for k in a.adiacenta[x].keys():
        if (a.adiacenta[x][k]!=[]):
            if ((x,k) in a.parcurse):
                g.attr('edge',color='green')
                g.edge(x,k)
            else:
                g.attr('edge',color='black')
                g.edge(x,k)
g.view()
