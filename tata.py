def check_file(input_file_name):
    try:
        input_file = open(input_file_name,"r")
        file_header= input_file.readline()[:-1].split(",")
        zivotinje = []
        for linija in input_file:
            zivotinja=linija.split(",")
            for kolona in range(2, len(zivotinja)):
                zivotinja[kolona]=int(zivotinja[kolona])
            zivotinje.append(zivotinja)
        input_file.close
        return zivotinje, file_header
    except:
        print ("Nesto nije uredu sa ulaznim fajlom!\n")


def ispitaj_uslov(uslov,file_header):
    uslov_split = uslov.split(" ")
    try: 
        uslov_split[2]=int(uslov_split[2])
    except:
        print("Vrednost mora biti broj.")
    if (len(uslov_split) != 3 )  or uslov_split[0] not in file_header or uslov_split[1] not in ("=","<",">") or  type(uslov_split[2]) != int :
        print ("Uslov nije dobar. Ocekivani ulaz je tipa: \"hair < 3 \" ili \"milk = 2\".  Unesite ponovo.")
        return False
    else: 
        return True

def ucitaj_uslove(file_header):
    uslovi=[]
    unesi_sledeci_uslov=True
    while (unesi_sledeci_uslov):
        uslov=input()
        if (uslov==''):
            unesi_sledeci_uslov=False
        else:
            if (ispitaj_uslov(uslov,file_header)):
                uslovi.append(uslov)
    return uslovi


def filtriraj_po_uslovima(zivotinje,file_header,uslovi):
    filt_zivotinje=zivotinje[:]
    i=len(zivotinje)-1
    while i >= 0 : 
        zivotinja=zivotinje[i]
        for uslov in uslovi:
            uslov=uslov.split()
            kolona_index=file_header.index(uslov[0])
            match uslov[1]:
                case "=":
                    if(zivotinja[kolona_index] == int(uslov[2])):
                        pass
                    else:
                        filt_zivotinje.pop(i)
                case "<":
                    if(zivotinja[kolona_index] < int(uslov[2])):
                        pass
                    else:
                        filt_zivotinje.pop(i)
                case ">":
                    if(zivotinja[kolona_index] > int(uslov[2])):
                        pass
                    else:
                        filt_zivotinje.pop(i)
        i-=1
    print(filt_zivotinje)

#input_file_name = input("Unesi fajl koji ce se koristiti kao ulaz.\n")
input_file_name="in"
zivotinje, file_header = check_file(input_file_name)
#print("Ovo su header kolone:\n", file_header[:])
#print ("A ovo su zivotinje: \n", zivotinje[:])    
uslovi = ucitaj_uslove(file_header)
#print (uslovi[:])
filtriraj_po_uslovima(zivotinje,file_header,uslovi)
