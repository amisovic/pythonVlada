zivotinje=[]
atributi=[]
uslovi=[]
filt_zivotinje=[]

def check_file(input_file_name):
    try:
        global zivotinje, atributi
        input_file = open(input_file_name,"r")
        atributi = input_file.readline()[:-1].split(",")
        for red in input_file:
            zivotinja=red.split(",")
            for kolona in range(2, len(zivotinja)):
                zivotinja[kolona]=int(zivotinja[kolona])
            zivotinje.append(zivotinja)
        input_file.close
    except:
        print ("Nesto nije uredu sa ulaznim fajlom!\n")

def ispitaj_uslov(uslov):
    uslov_split = uslov.split(" ")
    try: 
        uslov_split[2]=int(uslov_split[2])
    except:
        print("Vrednost mora biti broj.")
    if (len(uslov_split) != 3 )  or uslov_split[0] not in atributi or uslov_split[1] not in ("=","<",">") or  type(uslov_split[2]) != int :
        print ("Uslov nije dobar. Ocekivani ulaz je tipa: \"hair < 3 \" ili \"milk = 2\".  Unesite ponovo.")
        return False
    else: 
        return True

def ucitaj_uslove():
    unesi_sledeci_uslov=True
    while (unesi_sledeci_uslov):
        uslov=input()
        if (uslov==''):
            unesi_sledeci_uslov=False
        else:
            if (ispitaj_uslov(uslov)):
                uslovi.append(uslov)


def filtriraj_zivotinje():
    global filt_zivotinje
    filt_zivotinje=zivotinje[:]
    i=len(filt_zivotinje)-1
    while i >= 0 : 
        zivotinja=filt_zivotinje[i]
        brisanje=False
        for uslov in uslovi:
            uslov=uslov.split()
            kolona_index=atributi.index(uslov[0])
            match uslov[1]:
                case "=":
                    if(zivotinja[kolona_index] == int(uslov[2])):
                        pass
                    else: 
                        brisanje=True
                case "<":
                    if(zivotinja[kolona_index] < int(uslov[2])):
                        pass
                    else:
                        brisanje=True
                case ">":
                    if(zivotinja[kolona_index] > int(uslov[2])):
                        pass
                    else:
                        brisanje=True
        if brisanje: 
            filt_zivotinje.pop(i)
        i-=1

def print_list(lista):
    i = 0
    while i < len(lista):
        print (lista[i])
        i +=1
    print ()

def print_formated():
    i = 0
    while i < len(filt_zivotinje):
        print (filt_zivotinje[i][1], " - ", filt_zivotinje[i][0])
        i +=1
    print ()

# take second element for sort
def DrugiClan(element):
    return element[1]

#input_file_name = input("Unesi fajl koji ce se koristiti kao ulaz.\n")
#input_file_name="inPublic.csv"
input_file_name="in"
check_file(input_file_name)
#print("Ovo su atributi - kolone:\n", atributi[:])
#print ("A ovo su zivotinje: \n", zivotinje[:])    
ucitaj_uslove()
#print (uslovi[:])
filtriraj_zivotinje()
print_list(filt_zivotinje)

filt_zivotinje.sort(key=DrugiClan)
#print_list(filt_zivotinje)
print_formated()