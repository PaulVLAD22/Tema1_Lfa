from graphviz import Digraph
import termcolor


class Automat:
    def __init__(self, f):

        self.nr = int(f.readline())
        self.st_initial = f.readline()[0]
        self.st_final = f.readline().split()
        self.parcurse = []
        val_arc = []  # nodurile
        adiacenta_adn = {}  # legaturile dintre noduri
        sir = f.readline()

        while (sir):

            l = sir.split()
            for i in range(2):
                if (l[2] not in val_arc):
                    val_arc.append(l[2])

            if (adiacenta_adn.get((l[0])) == None):
                adiacenta_adn[(l[0])] = {}
                adiacenta_adn[(l[0])][l[2]] = [l[1]]  # format [1]: a:[2]
            else:
                if (adiacenta_adn[(l[0])].get((l[2])) == None):
                    adiacenta_adn[(l[0])][(l[2])] = [l[1]]
                else:
                    adiacenta_adn[(l[0])][(l[2])].append(l[1])

            sir = f.readline()
        print(adiacenta_adn)

        for k in adiacenta_adn.keys():

            for val in adiacenta_adn[k].values():

                val.sort()

        # Transformare in ADF
        a_aparut_stare_noua = 1

        while (a_aparut_stare_noua == 1):

            a_aparut_stare_noua = 0

            for k in list(adiacenta_adn.keys()):

                for subl in list(adiacenta_adn[k].values()):

                    if (tuple(subl) not in list(adiacenta_adn.keys())):

                        log = 0
                        if (log == 0):
                            tuplul = subl[:]
                            tuplul.sort()  # ca sa nu faca diferenta intre (3,5,4) si (4,5,3)
                            adiacenta_adn[tuple(tuplul)] = {}
                            a_aparut_stare_noua = 1

                            for x in tuple(tuplul):

                                if (x in list(adiacenta_adn.keys())):

                                    for p in list(adiacenta_adn[x].keys()):

                                        NODURI_NOI = adiacenta_adn[x][p][:]
                                        NODURI_NOI.sort()
                                        print(adiacenta_adn)

                                        if (adiacenta_adn[tuple(tuplul)].get(p) == None):
                                            adiacenta_adn[tuple(tuplul)][p] = NODURI_NOI
                                        else:
                                            for el in NODURI_NOI:

                                                if (el not in adiacenta_adn[tuple(tuplul)][p]):
                                                    adiacenta_adn[tuple(tuplul)][p].append(el)

                                            adiacenta_adn[tuple(tuplul)][p].sort()

        print(adiacenta_adn)  # era diferenta intre (3,5,4) si (4,3,5)

        self.adiacenta = adiacenta_adn
        self.val_arc = val_arc
        print(val_arc)
        print("DEASUPRA MEA")
        print(self.adiacenta)

    def check_input(self):

        cuvant = input("Introduceti cuvantul in automat")
        if (cuvant == ""):
            if (self.st_initial in self.st_final):
                print("Corect, st_initiala se afla in st_finala")
            else:
                self.bun = 0
                print("Nodul initial nu se afla in starile finale")
        else:
            ex_litere = 0
            ex_cifre = 0
            drum = []

            for x in cuvant:

                drum.append(x)
                if (x.isdecimal()):
                    ex_cifre = 1
                elif (x in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWYZ"):
                    ex_litere = 1
                else:
                    ex_cifre = 2  # date gresite, exista altceava in afara de cifre si litere

            if (ex_litere + ex_cifre == 1):
                elementele_sunt_in_alfabet = 1

                for x in cuvant:

                    if (x not in self.val_arc):
                        elementele_sunt_in_alfabet = 0

                if (elementele_sunt_in_alfabet == 1):
                    return drum
                else:
                    print(
                        termcolor.colored("Cuvantul de intrare contine elemente ce nu se afla in alfabet", color="red"))
            else:
                self.bun = 0
                print(termcolor.colored("Cuvantul de Intrare este gresit", color="red"))

        return 0

    def parcurgerea_cuvantului(self, drum):

        poz = self.st_initial
        log = 0
        print(poz)

        for x in drum:

            if (self.adiacenta.get(poz) != None):
                if (self.adiacenta[poz].get(x) != None):
                    self.parcurse.append((poz, x, self.adiacenta[poz][x]))
                    poz = tuple(self.adiacenta[poz][x])
                    if (len(poz) == 1):
                        poz = poz[0]
                    print(poz)
                else:
                    log = 1  # nu are unde avansa de pe nodul poz
                    break
            else:
                log = 1  # nu are unde avansa de pe nodul poz
                break

        if (log == 1):

            try:
                print(termcolor.colored("Nu are unde avansa de pe nodul " + str(poz), color="red"))
            except:
                sir = str(poz[0])
                for i in range(1, len(poz)):
                    sir += ',' + poz[i]

                print(termcolor.colored("Nu are unde avansa de pe nodul " + sir, color="red"))

        else:
            for x in poz:

                if (x in self.st_final):
                    break

            else:
                print(termcolor.colored("Nodul in care se termina cuvantul nu este final", color="red"))
                return 0  # ca sa se opreasca

        if (log == 0):
            print(termcolor.colored("Da,a ajuns pe stare finala", color="blue"))


def desen(poz, a):

    global Noduri_desen
    toate_au_fost_parcurse = 1

    if (a.adiacenta.get(poz) != None):

        for k in a.adiacenta[poz].values():

            if (k not in Noduri_desen):
                if (len(k) == 1):
                    if (k[0] not in Noduri_desen):
                        toate_au_fost_parcurse = 0
                        Noduri_desen.append(k[0])  # adaug nodurile prin care s a trecut
                else:
                    if (tuple(k) not in Noduri_desen):
                        toate_au_fost_parcurse = 0
                        Noduri_desen.append(tuple(k))  # adaug nodurile prin care s a trecut

        if (toate_au_fost_parcurse == 0):
            print(Noduri_desen)

            for k in a.adiacenta[poz].values():
                if (len(k) == 1):
                    desen(k[0], a)
                else:
                    desen(tuple(k), a)


class Nod:
    def __init__(self, automat, val):

        self.val = val
        self.final = 0

        for x in val:
            if x in automat.st_final:
                self.final = 1

        if (val == automat.st_initial):
            self.initial = 1
        else:
            self.initial = 0

    def desenare(self, g):

        self.val = tuple(self.val)

        if (self.final == 1):
            g.attr('node', shape="doublecircle")
        else:
            g.attr('node', shape="circle")

        if (self.initial == 1):
            g.node('', shape='none')
            sir = ''

            for i in range(len(self.val)):

                if (i != 0):
                    sir += ',' + self.val[i]
                else:
                    sir += self.val[i]

            g.node(sir)
            g.edge('', sir, label="START")
        else:
            sir = ''

            for i in range(len(self.val)):
                if (i != 0):
                    sir += ',' + self.val[i]
                else:
                    sir += self.val[i]

            g.node(sir)


def main():
    f = open('date.txt')
    a = Automat(f)
    drum = a.check_input()

    if (drum != 0):
        a.parcurgerea_cuvantului(drum)

    print(a.parcurse)
    global Noduri_desen
    Noduri_desen = [a.st_initial]

    poz = a.st_initial
    i = 0
    desen(poz, a)

    print(Noduri_desen, "AICI E NODURI DESEN")
    # grafica
    g = Digraph(name="AutomatulFD", filename="AutomatulEXEMPLU1TEst5")
    arce = []

    for k in Noduri_desen:

        nod = Nod(a, k)
        nod.desenare(g)

    for k in Noduri_desen:

        if (a.adiacenta.get(k)):

            for vec in a.adiacenta[k].keys():

                if ((k, vec, a.adiacenta[k][vec]) in a.parcurse):
                    g.attr('edge', color="green")

                    if ((k, vec, a.adiacenta[k][vec]) not in arce):
                        v1 = tuple(k)
                        v2 = tuple(a.adiacenta[k][vec])
                        sir1 = str(v1[0])

                        for i in range(1, len(v1)):
                            sir1 += ',' + v1[i]

                        sir2 = str(v2[0])

                        for i in range(1, len(v2)):
                            sir2 += ',' + v2[i]

                        print(sir1, sir2)
                        # pt verificare
                        print((sir1, sir2,), "AICI")
                        g.edge(sir1, sir2, vec)
                        arce.append((k, vec, a.adiacenta[k][vec]))
                else:
                    g.attr('edge', color="black")

                    if ((k, vec, a.adiacenta[k][vec]) not in arce):
                        v1 = tuple(k)
                        v2 = tuple(a.adiacenta[k][vec])
                        sir1 = str(v1[0])

                        for i in range(1, len(v1)):
                            sir1 += ',' + v1[i]

                        sir2 = str(v2[0])

                        for i in range(1, len(v2)):
                            sir2 += ',' + v2[i]

                        print(sir1, sir2)
                        # pt verificare
                        print((sir1, sir2,), "AICI")
                        g.edge(sir1, sir2, vec)
                        arce.append((k, vec, a.adiacenta[k][vec]))

    print(arce)
    g.view()


if __name__ == "__main__":
    main()
