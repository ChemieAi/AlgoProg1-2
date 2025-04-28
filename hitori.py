import copy
def liste_al():
    hitori = open("hitori_bulmaca.txt","r+")
    liste = []
    satir = hitori.readline()
    satir_say = 0
    while satir != "" :
        ara_liste = []
        for sayilar in satir.rsplit():
            ara_liste.append("-")
            ara_liste.append(sayilar)
        liste.append(ara_liste)
        satir = hitori.readline()
        satir_say += 1
    sifirlama_listesi = copy.deepcopy(liste)  #bidaha for açmaya üşendim  offff...
    ters_liste = []
    for i in range(satir_say):
        ters_liste.append([0] * satir_say)
    tablo_ciz(liste,satir_say)
    degisiklik(liste,sifirlama_listesi,ters_liste,satir_say)
    hitori.close()

def tablo_ciz(liste,satir_say):
    print(end="  ")
    for satir in range(satir_say):
        print(end=" ")
        print(satir+1,end=" ")
    print()
    for satir in range(satir_say):
        print(satir+1,end=" ")
        for sutun in range(satir_say):
            if liste[satir][2 * sutun] == "-":
                print("-",liste[satir][2 * sutun + 1],"-",sep="",end="")
            else:
                print("(", liste[satir][2 * sutun + 1], ")", sep="", end="")
        print()

def degisiklik(liste,sifirlama_listesi,ters_liste,satir_say):
    try:
        yapilacak_degisiklik = input("satır,sütun,işlem")
        degisiklik_listesi = yapilacak_degisiklik.rsplit()
        while int(degisiklik_listesi[0])<0 or int(degisiklik_listesi[0])>satir_say or int(degisiklik_listesi[1])<0 or int(degisiklik_listesi[1])>satir_say or not(degisiklik_listesi[2] in ["B","b","D","d","N","n"]):
            yapilacak_degisiklik = input("satır,sütun,işlem hatalı girdiniz!")
            degisiklik_listesi = yapilacak_degisiklik.rsplit()
        satir = int(degisiklik_listesi[0])
        sutun = int(degisiklik_listesi[1])
        islem = degisiklik_listesi[2]
    except ValueError or UnboundLocalError:
        yapilacak_degisiklik = input("satır,sütun,işlem hatalı girdiniz!")
        degisiklik_listesi = yapilacak_degisiklik.rsplit()
    if islem == "B" or islem == "b":
        liste[satir - 1][2 * sutun - 2] = "-"
        liste[satir-1][2 * sutun -1] = "X"
    elif islem == "D" or islem == "d":
        liste[satir - 1][2 * sutun - 2] = "("
    else:
        liste[satir - 1][2 * sutun - 2] = "-"
        liste[satir - 1][2 * sutun - 1] = sifirlama_listesi[satir - 1][2 * sutun -1]
    tablo_ciz(liste,satir_say)
    kontrol(liste,sifirlama_listesi,ters_liste,satir_say)


def butunluk_kontrolu(liste, adres_listesi, satir_say, satir=0, sutun=0):
    if satir == 0 and sutun == 0 and liste[satir][sutun] == "X":
        butunluk_kontrolu(liste, adres_listesi, satir_say, satir, sutun + 1)
    if satir_say - 1 > satir > 0 and satir_say - 1 > sutun > 0 and liste[satir][sutun] != "X" and not (str(satir) + str(sutun) in adres_listesi):
        adres_listesi[str(satir) + str(sutun)] = 1
        butunluk_kontrolu(liste, adres_listesi, satir_say, satir, sutun + 1)  # sağını
        butunluk_kontrolu(liste, adres_listesi, satir_say, satir + 1, sutun)  # aşağısını
        butunluk_kontrolu(liste, adres_listesi, satir_say, satir, sutun - 1)  # solunu
        butunluk_kontrolu(liste, adres_listesi, satir_say, satir - 1, sutun)  # yukarısını

    elif satir == 0 and satir_say - 1 > sutun > 0 and liste[satir][sutun] != "X" and not (str(satir) + str(sutun) in adres_listesi):
        adres_listesi[str(satir) + str(sutun)] = 1
        butunluk_kontrolu(liste, adres_listesi, satir_say, satir, sutun + 1)
        butunluk_kontrolu(liste, adres_listesi, satir_say, satir + 1, sutun)
        butunluk_kontrolu(liste, adres_listesi, satir_say, satir, sutun - 1)

    elif satir_say - 1 > satir > 0 and sutun == satir_say - 1 and liste[satir][sutun] != "X" and not (str(satir) + str(sutun) in adres_listesi):
        adres_listesi[str(satir) + str(sutun)] = 1
        butunluk_kontrolu(liste, adres_listesi, satir_say, satir + 1, sutun)
        butunluk_kontrolu(liste, adres_listesi, satir_say, satir, sutun - 1)
        butunluk_kontrolu(liste, adres_listesi, satir_say, satir - 1, sutun)

    elif satir_say - 1 > satir > 0 and sutun == 0 and liste[satir][sutun] != "X" and not (str(satir) + str(sutun) in adres_listesi):
        adres_listesi[str(satir) + str(sutun)] = 1
        butunluk_kontrolu(liste, adres_listesi, satir_say, satir, sutun + 1)  # sağını
        butunluk_kontrolu(liste, adres_listesi, satir_say, satir + 1, sutun)  # aşağısını
        butunluk_kontrolu(liste, adres_listesi, satir_say, satir - 1, sutun)  # yukarısını

    elif satir == satir_say - 1 and satir_say - 1 > sutun > 0 and liste[satir][sutun] != "X" and not (str(satir) + str(sutun) in adres_listesi):
        adres_listesi[str(satir) + str(sutun)] = 1
        butunluk_kontrolu(liste, adres_listesi, satir_say, satir, sutun + 1)  # sağını
        butunluk_kontrolu(liste, adres_listesi, satir_say, satir, sutun - 1)  # solunu
        butunluk_kontrolu(liste, adres_listesi, satir_say, satir - 1, sutun)  # yukarısını

    elif satir == 0 and sutun == 0 and liste[satir][sutun] != "X" and not (str(satir) + str(sutun) in adres_listesi):
        adres_listesi[str(satir) + str(sutun)] = 1
        butunluk_kontrolu(liste, adres_listesi, satir_say, satir, sutun + 1)
        butunluk_kontrolu(liste, adres_listesi, satir_say, satir + 1, sutun)

    elif satir == 0 and sutun == satir_say - 1 and liste[satir][sutun] != "X" and not (str(satir) + str(sutun) in adres_listesi):
        adres_listesi[str(satir) + str(sutun)] = 1
        butunluk_kontrolu(liste, adres_listesi, satir_say, satir + 1, sutun)  # aşağısını
        butunluk_kontrolu(liste, adres_listesi, satir_say, satir, sutun - 1)  # solunu

    elif satir == satir_say - 1 and sutun == satir_say - 1 and liste[satir][sutun] != "X" and not (str(satir) + str(sutun) in adres_listesi):
        adres_listesi[str(satir) + str(sutun)] = 1
        butunluk_kontrolu(liste, adres_listesi, satir_say, satir, sutun - 1)  # solunu
        butunluk_kontrolu(liste, adres_listesi, satir_say, satir - 1, sutun)  # yukarısını

    elif satir == satir_say - 1 and sutun == 0 and liste[satir][sutun] != "X" and not (str(satir) + str(sutun) in adres_listesi):
        adres_listesi[str(satir) + str(sutun)] = 1
        butunluk_kontrolu(liste, adres_listesi, satir_say, satir, sutun + 1)  # sağını
        butunluk_kontrolu(liste, adres_listesi, satir_say, satir - 1, sutun)  # yukarısını
    return adres_listesi

def kontrol(liste,sifirlama_listesi,ters_liste,satir_say):
    rakam_say=0
    adres_listesi={}
    yatay_ayni_rakam_say = 0
    yan_yana_bosluk = 0
    for satir in range(satir_say):
        for sutun in range(satir_say):
            if liste[satir][2 * sutun + 1]!="X":
                rakam_say+=1
            s1_liste=liste[satir][:2*sutun+1] #s1 ve s2 o an incelenen rakamı içermeyen 2 dilime ayrılmış satır listesinin halleridir
            s2_liste=liste[satir][2*sutun+2:] #s --> slice
            ters_liste[sutun][satir] = liste[satir][2 * sutun + 1]
            rakam = liste[satir][2 * sutun + 1]
            if (rakam in s1_liste or rakam in s2_liste) and rakam != "X":
                yatay_ayni_rakam_say += 1
            if sutun <= satir_say - 2 and yatay_ayni_rakam_say==0:
                if liste[satir][2 * sutun + 1] == liste[satir][2 * (sutun + 1) + 1] and liste[satir][2 * sutun + 1] == "X":
                    yan_yana_bosluk += 1

    dikey_ayni_rakam_say = 0
    ust_uste_bosluk = 0
    if yatay_ayni_rakam_say==0 and yan_yana_bosluk==0:
        for sutun in range(satir_say):
            for satir in range(satir_say):
                rakam = ters_liste[sutun][satir]
                s1_liste = ters_liste[sutun][:satir] #s1 ve s2 o an incelenen rakamı içermeyen 2 dilime ayrılmış satır listesinin halleridir
                s2_liste = ters_liste[sutun][satir+1:]
                if (rakam in s1_liste or rakam in s2_liste) and rakam != "X":
                    dikey_ayni_rakam_say+=1
                if satir <= satir_say - 2:
                    if ters_liste[sutun][satir] == ters_liste[sutun][satir+1] and ters_liste[sutun][satir] == "X":
                        ust_uste_bosluk += 1
    if yatay_ayni_rakam_say==0 and yan_yana_bosluk==0 and dikey_ayni_rakam_say==0 and ust_uste_bosluk==0:
        butunluk_kontrolu(ters_liste,adres_listesi,satir_say,0,0)
    if ust_uste_bosluk>0 or yan_yana_bosluk>0 or dikey_ayni_rakam_say>0 or yatay_ayni_rakam_say>0:
        degisiklik(liste,sifirlama_listesi,ters_liste,satir_say)
    elif len(adres_listesi)!=rakam_say:
        print(len((adres_listesi)))
        degisiklik(liste, sifirlama_listesi, ters_liste, satir_say)
    else:
        print("helal beee! bitti!!")
        tablo_ciz(liste,satir_say)

liste_al()
