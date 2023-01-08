# stanice = [{"RB": int, "Naziv": str}, ...]
# linije = [{"BROJ": int, "RBstan": int, "Stanica": int}, ...]
stanice=[]
linije=[]

def sortStanice(stanice): return stanice['RB']
def sortLinije1(linije): return linije['BROJ']
def sortLinije2(linije): return linije['RBstan']
def sortLinije(linije): return (linije['BROJ'],linije['RBstan'])

def ucitaj_stanice(fajl_stanice):
    try:
        fajl = open (fajl_stanice,"r")
        for red in fajl:
            polja=red.replace("\n","").split("|")
            #stanica=dict(RB = int(polja[0]), Naziv = polja[1])
            stanica = {'RB': int(polja[0]), 'Naziv': polja[1]}
            stanice.append(stanica)
    except:
        print("Nesto nije uredu sa fajlom za stanice.")
    stanice.sort(key=sortStanice)
    return stanice


def ucitaj_linije(fajl_linije):
    try:
        fajl = open (fajl_linije,"r")
        for red in fajl: 
            polja=red.replace("\n","").split(",")
            linija={'BROJ': int(polja[0]),"RBstan": int(polja[1]),"Stanica": int(polja[2]) }
            linije.append(linija)
    except:
        print ("Nesto nije uredu sa fajlom za LINIJE.")
    #linije.sort(key=sortLinije2)
    #linije.sort(key=sortLinije1)
    linije.sort(key=sortLinije)
    return linije

def print_list(lista):
    for linija in lista:
        print (linija)

def ispitaj_linije():
    BUSEVI=list(set([linija['BROJ'] for linija in linije]))
    for BUS in BUSEVI:
        staniceRB=[]
        for linija in linije:
            if linija['BROJ'] == BUS:
                staniceRB.append(linija['RBstan'])
        print("\n+++++++++++++++++++++++++++++++++++++++++++++")
        print("Provera ispravnosti stanica za Liniju:", BUS)
        print(staniceRB)
        irb=1 
        ilist=0
        while ilist < len(staniceRB):
            if staniceRB[ilist] == irb:
                irb +=1
                ilist +=1
            elif staniceRB[ilist] > irb:
                print("Nedostaje stanica broj:", irb, "u fajlu")
                irb +=1
            else:
                if staniceRB[ilist] < irb:
                    print("Postoji duplikat stanica broj: ", staniceRB[ilist]," u fajlu")
                    ilist +=1

def ispitaj_stanice():
    print("\n+++++++++++++++++++++++++++++++++++++++++++++")
    print("Provera ispravnosti stanica.\n")
    #Provera da li ima duplikata u stanicama.csv
    staniceRB=[]
    for stanica in stanice:
        if stanica["RB"] not in staniceRB:
            staniceRB.append(stanica["RB"])
        else:
            print("Stanica: ", stanica["RB"], " je duplikat.")
    #Provera da li ima neka stanica u fajlu sa linijama a da nije definisana u stanicama.csv
    for linija in linije:
        if linija["Stanica"] not in staniceRB:
            print ("Stanica RB: ", linija["Stanica"], " nije definisana u stanicama.")
    
def print_linije_stanice():
    BUSEVI=list(set([linija['BROJ'] for linija in linije]))
    for BUS in BUSEVI:
        print("=================================")
        print("Linija:", BUS)
        for linija in linije:
            if linija['BROJ'] == BUS:
                for stanica in stanice:
                    if stanica["RB"] == linija["Stanica"]: 
                        stan = stanica
                print(linija["RBstan"]," - ", stan["Naziv"])

def preformatiraj_linije():

# stanice = [{"RB": int, "Naziv": str}, ...]
# linije = [{"BROJ": int, "RBstan": int, "Stanica": int}, ...]


#linije,stanice=input("Unesi fajlove za linije i stanice:").split()
fajl_linije="linije1BAD.csv"
fajl_stanice="stanice1BAD.csv"

ucitaj_stanice(fajl_stanice)
ucitaj_linije(fajl_linije)
ispitaj_linije()
ispitaj_stanice()
print_linije_stanice()
preformatiraj_linije()