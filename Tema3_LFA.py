from graphviz import Digraph
import termcolor

class PDA:
    def __init__(self,f):
        self.nr=0
        self.stari=[]
        self.stack=['$']
        self.acceptat=False
        self.explicatii=""
        self.adiacenta={} #citesc de forma a,$->$a (a o sa fie in varf) ->   q0:{ q0:(a,$,$a)}
        self.inceput=0
        self.finale=[]

        #citire
        
        self.nr=int(f.readline())
        self.stari=f.readline().split()
        print(self.stari)
        self.inceput=f.readline().split()[0]
        print(self.inceput)
        self.finale=f.readline().split()
        print(self.finale)
        sir=f.readline()

        while (sir):

            l=sir.split()

            if (self.adiacenta.get(l[0])==None):
                self.adiacenta[l[0]]={}
                self.adiacenta[l[0]][l[4]]=[(l[1],l[2],l[3])]
            else:
                if (self.adiacenta[l[0]].get(l[4])==None):
                    self.adiacenta[l[0]][l[4]]=[(l[1],l[2],l[3])]
                else:
                    self.adiacenta[l[0]][l[4]].append((l[1],l[2],l[3]))

            sir=f.readline()

        print(self.adiacenta)
        cuvant=input()
        self.parcurgere(cuvant,self.inceput,self.stack)

    def parcurgere(self,cuvant,st_actuala,stack):

        if (len(cuvant)==0):
            if (len(stack)==0):
                self.acceptat=True
                self.explicatii="Stiva goala"
            else:
                if (st_actuala in self.finale):
                    self.acceptat=True
                    print(stack)
                    self.explicatii="Stare finala"
                else:
                    if (self.adiacenta.get(st_actuala)!=None):

                        for stare in self.adiacenta[st_actuala]:

                            for tuplu in self.adiacenta[st_actuala][stare]:

                                if (tuplu[0]=="#"):

                                    if (stack[len(stack)-1]==tuplu[1]):

                                        stack = stack[:len(stack) - 1]
                                        if (tuplu[2] == "#"):
                                            pass
                                        else:
                                            for el in tuplu[2]:
                                                stack.append(el)
                                        self.parcurgere(cuvant, stare, stack)


        if (len(cuvant)!=0):
            if (len(stack)!=0):

                if (self.adiacenta.get(st_actuala)!=None):

                    for stare in self.adiacenta[st_actuala]:

                        for tuplu in self.adiacenta[st_actuala][stare]:

                            if (tuplu[0]==cuvant[0]):

                                if (stack[len(stack)-1]==tuplu[1]):
                                    stack=stack[:(len(stack)-1)]
                                    if (tuplu[2]=="#"):
                                        pass
                                    else:
                                        for el in tuplu[2]:
                                            stack.append(el)

                                    self.parcurgere(cuvant[1:],stare,stack)

                            if (tuplu[0]=="#"):

                                if (stack[len(stack)-1]==tuplu[1]):

                                    stack = stack[:len(stack) - 1]
                                    if (tuplu[2] == "#"):
                                        pass
                                    else:
                                        for el in tuplu[2]:
                                            stack.append(el)
                                    self.parcurgere(cuvant, stare, stack)

    def verificare(self):
        if (self.acceptat==True):
            print(termcolor.colored((self.explicatii),color="blue"))
        else:
            print(termcolor.colored("Cuvantul nu a fost acceptat",color="red"))

class Nod:

    def __init__(self, automat, val):
        self.val = val
        if (val in automat.finale):
            self.final = 1  # boolean
        else:
            self.final = 0
        if (val == automat.inceput):
            self.initial = 1
        else:
            self.initial = 0

    def desenare(self, g):
        if (self.final == 1):
            g.attr('node', shape="doublecircle")
        else:
            g.attr('node', shape="circle")

        if (self.initial == 1):
            g.node('', shape='none')
            g.node(self.val)
            g.edge('', self.val, label='START')
        else:
            g.node(self.val)






def main():
    f=open('date.txt')
    a= PDA(f)
    a.verificare()

    #grafica
    g=Digraph(name="Automat",filename="aaassaaaaaaaaaaaaaaa")
    for x in a.stari:
        nod = Nod(a,x)
        nod.desenare(g)
    """
    for nod1 in a.adiacenta.keys():
        for nod2 in a.adiacenta[nod1]:
            for tuplu in a.adiacenta[nod1][nod2]:
                g.attr('edge', color="black")
                g.edge(nod1,nod2,str(tuplu[0])+" "+str(tuplu[1])+"-> "+str(tuplu[2]))"""

    # pentru multe relatii

    for nod1 in a.adiacenta.keys():
        for nod2 in a.adiacenta[nod1]:
            sir=""
            for tuplu in a.adiacenta[nod1][nod2]:
                sir+="\n"+str(tuplu[0])+" "+str(tuplu[1])+" -> "+str(tuplu[2])
            g.attr("node",shape='box')
            g.node(sir)
            g.edge(nod1,sir)
            g.edge(sir,nod2)


    g.view()


if __name__ == "__main__":
     main()

"""formatul fisierului date.txt
3
q0 q1 q2
q0
q2
q0 0 $ $0 q0
q0 1 $ $1 q0
q0 0 0 00 q0
q0 0 1 10 q0
q0 1 0 01 q0
q0 1 1 11 q0
q0 c $ $ q1
q0 c 0 0 q1
q0 c 1 1 q1
q1 0 0 # q1
q1 1 1 # q1
q1 # $ $ q2"""