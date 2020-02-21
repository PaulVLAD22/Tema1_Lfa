import pygame
import math
st_initial=[]
st_final=[]
traducere=[]
adiacenta=[]
n=0
parcurse=[]#nodurile parcurse
def citire():
    global adiacenta,traducere,st_final,st_initial,n
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


def check_input(sir):
    if (sir!="λ"):
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

        if (ex_litere+ex_cifre==1):
            parcurgerea_cuvantului(drum)
        else:
            print("Drumul este gresit")
    else:
        print("Da")
def parcurgerea_cuvantului(drum):
    global adiacenta, traducere, st_final, st_initial,n,parcurse
    print(adiacenta)
    print(st_initial)
    poz = traducere.index(st_initial)

    st_final_numere = []
    for x in st_final:
        st_final_numere.append(traducere.index(x))
    print(st_final_numere)
    log = 0
    for x in drum:
        for k in range(n):
            if (x in adiacenta[poz][k]):
                parcurse.append((poz,k))
                poz = k

                print(poz)
                break
        else:
            log = 1
    if (poz not in st_final_numere):
        log = 1
    if (log == 0):
        print("Da")
    else:
        print("Drumul este gresit")

##programul
citire()
sir=input("Introduceti cuvantul")
check_input(sir)
print(parcurse)

#pygame
pygame.init()
screen = pygame.display.set_mode((800,600))

#Titlu
pygame.display.set_caption("Automatul")

# font
font = pygame.font.Font(None, 20)

# nod
def creare_nod_normal(i,k):
    pygame.draw.circle(screen,(0,0,0),((i+1)*50,300),20,1)
    screen.blit(font.render(str(k), True, (0,0,0)), ((i+1)*50-5,290))
def creare_nod_final(i,k):
    pygame.draw.circle(screen,(0,0,0),((i+1)*50,300),20,1)
    pygame.draw.circle(screen,(0,0,0),((i+1)*50,300),15,1)
    screen.blit(font.render(str(k), True, (0, 0, 0)), ((i+1)* 50-5 , 290))
def creare_arc_neparcurs(i,j):
    if (i!=j):
        if(i<j):
            pygame.draw.arc(screen,(0,0,0),((i+1)*50,130,j+1*50,300),0,math.pi)
            p=1
            for val in adiacenta[i][j]:#nu afiseaza de la q la r
                screen.blit(font.render(str(val), True, (0, 0, 0)), ((i + 1) * 50+20, 150+p))
                p+=30
        else:

            pygame.draw.arc(screen,(0,0,0),((i-1)*50,180,(j+2)*50,270),math.pi,0)
            p = 1

            for val in adiacenta[i][j]:
                screen.blit(font.render(str(val), True, (0, 0, 0)), ((i-j)*50, 400-p))
                p += 30
            #arcul sa fie sub noduri:
    else:
        pygame.draw.arc(screen,(0,0,0),((i+1)*50-10,280,i+1*50-10,50),math.pi*3/2-0.8,math.pi/2)
        p=1
        for val in adiacenta[i][j]:
            screen.blit(font.render(str(val), True, (0, 0, 0)), ((i+1)*50+p+20,300))
            p += 5


def creare_arc_parcurs(i,j):
    if (i!=j):
        if(i<j):
            pygame.draw.arc(screen,(34,139,34),((i+1)*50,130,j+1*50,300),0,math.pi)
            p=1
            for val in adiacenta[i][j]: ##NU AFISEAZA DE LA q la r valoarea arcu
                screen.blit(font.render(str(val), True, (0, 0, 0)), ((i + 1) * 50+20, 150+p))
                p+=30
        else:
            pygame.draw.arc(screen, (34, 139, 34), ((i - 1) * 50, 180, (j + 2) * 50, 270), math.pi, 0)
            p = 1

            for val in adiacenta[i][j]:
                screen.blit(font.render(str(val), True, (0, 0, 0)), ((i - j) * 50, 400 - p))
                p += 30

    else:
        pygame.draw.arc(screen, (34, 139, 34), ((i + 1) * 50 - 10, 280, i + 1 * 50 - 10, 50), math.pi * 3 / 2 - 0.8,
                        math.pi / 2)
        p = 1
        for val in adiacenta[i][j]:
            screen.blit(font.render(str(val), True, (0, 0, 0)), ((i + 1) * 50 + p + 20, 300))
            p += 5




running=True
while (running):
    screen.fill((255,255,255))
    for x in traducere:
        if (x in st_final):
            creare_nod_final(traducere.index(x),x)
        else:
            creare_nod_normal(traducere.index(x),x)
    for i in range(n):
        for j in range(n):
            if (len(adiacenta[i][j])!=0):

                if ((i,j) not in parcurse):
                    creare_arc_neparcurs(i,j)
                else:
                    creare_arc_parcurs(i,j)




    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    pygame.display.update()

