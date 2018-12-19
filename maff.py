
import random

names=["Natali", "Juri","Dimi", "Ana", "Den", "Sveta", "Sergei", "Allan", "Kate", "Sun"]
gorod=[] ## SPisok goroda, zivii ljudi
podoz=[] ## Spisok vistavlenih na golosovanie(nado dobavit po dnjam istoriju i obnuljat spisok v konze dnja)
mafki=[] ## psisok mafok

class Player():
    def __init__(self, name):
        self.name = name ## imja igroka
        self.maf = 'civ' ## po defoltu mirnii
        self.alive =  True ## status zivoi mjortvii, ne zadeistvovan, poskolku zivii nahodjatsja v spiske gorod
        self.vote = 0 ## kolichestvo nabranih golosov, nado obnuljat v konze, dnja i rezultati dobovljat v istoriju
        self.voted = False ## golosoval ili net, obnuljat v konze dnja
        self.golosa = [] ## spisok teh kto golosoval za tebja, obnuljat v konze dnja i v istoriju
    def __repr__(self):
        return "<%s>" % self.name ## dlja debuga, pri print vidajot imena objektov po imenam igrokov

################funkzija razdachi imen i sozdanija spiska gorod s igrokami### peremeshivaet spisok i vidergivaet po odnomu poka ne zakonchitsja spisok

def pikname(names):
    if len(names) > 0:
        for i in names:
            num = len(names) - 1
            index = random.randint(0, num)
            win = names.pop(index)
            i = Player(win)
            ###print(i.name)
            gorod.append(i)
        else:
            pass
        
while len(names) > 0:
    pikname(names)
#print(len(gorod))




role = ['maf', 'maf', 'maf', 'civ', 'civ', 'civ', 'civ', 'civ', 'civ', 'civ'] ### spisok rolei,(est' nad chem podumat)


    
######################funkzija razdachi rolei ### kidaet randomno roli na igrokov iz spiska gorod, esli igrokov budet ne 10 ne vse roli raspredeljatsja
def pik(role):
    
    if len(role) > 0:
        for i in range(len(gorod)):
            num = len(role) - 1
            index = random.randint(0, num)
            win = role.pop(index)
            gorod[i].maf = win
            if win == 'maf':
                mafki.append(gorod[i])
            
    else:
        print("there is nothing to receive")
        
#sama razdacha
while len(role) > 0:
    pik(role)
    
#for a in range(len(gorod)): ### zdes vidajot spisok po imenam i roljam, dlja debuga
    #print(gorod[a].name, gorod[a].maf)

while len(gorod) > len(mafki):
    print("spisok zivih mafov: " + str(mafki))


    ################## Den, vistavlenie kandidatur(Logika vistavlenie bred 0 - 50) ISPRAVIT
    
    def pod(suspect):
        for i in range(len(gorod)):
            if suspect != gorod[i] and (suspect != "maf" and gorod[i] != "maf"):
                win = random.randint(0, 50)
                if  win == 1:
                    print(gorod[i].name, "vistavljaet igroka ", suspect.name)
                    if suspect not in podoz:
                        podoz.append(suspect)
                    else:
                        pass
                
            elif suspect == gorod[i]:
                #print(gorod[i].name, "ne mozet golosovat za sebja")
                pass
            else:
                #print(gorod[i].name, "uze golosoval")
                pass
    
    for i in range(len(gorod)):    ## sama prozedura vistavlenja        
        pod(gorod[i])
    print(podoz)
    ############################################
        
    ################## Golosovalka, (mafi ne golosujut drug protiv druga, sam za zebja toze net) ISPRAVIT!
    
    def prov(suspect):
        for i in range(len(gorod)):
            if suspect != gorod[i] and (suspect != "maf" and gorod[i] != "maf") and gorod[i].voted == False:
                win = random.randint(0, 1)
                if  win == 1:
                    gorod[i].voted = True
                    suspect.golosa.append(gorod[i].name)
                    #print(gorod[i].name, "golosuet za ", suspect.name)
                    suspect.vote += win
                
                
            elif suspect == gorod[i]:
                #print(gorod[i].name, "ne mozet golosovat za sebja")
                pass
            else:
                #print(gorod[i].name, "uze golosoval")
                pass
    
    #### golusuem iz spiska vistavlenih, esli vistavlen odin, vse golosa letjajt v nego. mafi ne golosujut protiv drug druga esli est v vistavlenih civ.
    for i in range(len(podoz)):
        if len(podoz)>1:
            prov(podoz[i])
            #print(gorod[i].name, gorod[i].vote)
        elif len(podoz)==1:
            if podoz[0].maf == "maf":
                print(podoz[0].name, " kaznjon s ", len(gorod)-1, " golosov, on bil ", podoz[0].maf)
                mafki.remove(podoz[0])
                gorod.remove(podoz[0])
            else:
                print(podoz[0].name, " kaznjon s ", len(gorod)-1, " golosov on bil", podoz[0].maf)
                gorod.remove(podoz[0])
        else:
            print("Gorod uhodit v noch!")
            
    #print(gorod[2].golosa)
    
    ############################################ Itogi golosovanija
    # sortiruet spisok gorod a po golosam, v sluchae ravnogo kolichestva golosov rabotaet figova
    def takeSecond(elem):
        return elem.vote
    
    # sort list with key naibolsheee kol.golosov
    podoz.sort(key=takeSecond, reverse=True)
    
    # print list 
    if len(podoz)>1:
        for i in range(len(podoz)):
            print(podoz[i].name, podoz[i].vote)
    else:
        pass
    ### posadka nabravshego bolshinstvo golosov, ne rabotaet esli ravnoe kolichestvo golosov
    if len(podoz)>=2:
        if podoz[0].vote == podoz[1].vote: ### esli minimum 2 chelovka odinakova golosov, gorod uhodit v noch
            print("gorod ne opredelilsja")
        if podoz[0].maf == "maf":
            print(podoz[0].name, " kaznjon s ", len(gorod)-1, " golosov, on bil ", podoz[0].maf)
            mafki.remove(podoz[0])
            gorod.remove(podoz[0])
        else:
            print(podoz[0].name + " bil kaznjon gorodom " + " on bil " + podoz[0].maf)
            gorod.remove(podoz[0])
            
    print(gorod)
    podoz.clear() ### obnulenie spiska podozrevaemih
    
    ############### Sheriff proverjaet!! i ubivaet esli maff!
    def sheriff(suspect):
        if suspect.maf == 'maf':
            print("Sheriff ubivaet mafioze, ", suspect.name)
            gorod.remove(suspect)
            mafki.remove(suspect)
        else:
            print(suspect.name, "mirnii zitel")
    
    if len(gorod) > len(mafki) and len(mafki) != 0: ### proverka na konez igri
        sheriff(gorod[0]) ### sama proverka sheriffom, vmesto ukazanogo objekta, ukazivaet polzovatel cherez input()
    elif len(mafki) == 0:
        print("Igra okonchena. Mirnii pobedil")
        break
    else:
        print("Igra okonchena. Mafija pobedila")
        break
    
    
    ########################################################## Vistrel mafii!!! randomnii chelovek iz goroda, esli on maff to snova viberaem randoma.
    
    def maff():
        x = random.randint(0, (len(gorod)-1))
        if gorod[x].maf != 'maf': #### esli ne maff , to ubivaem
            print("Maffija ubivaet zitelja, ", gorod[x].name)
            gorod.remove(gorod[x])
            if len(gorod)< len(mafki):
                print("Igra okonchena, mafija pobedila")
            
        
        else:
            maff()
    
    maff() ### sam vistrelov maffov
    print("Gorod na konez dnja ", gorod)
    
    if len(mafki)>= len(gorod):
        print("Mafija pobedila!")
        break
    
    for i in range(len(gorod)-1):
        gorod[i].voted = False
    for i in range(len(gorod)-1):
        gorod[i].vote = 0