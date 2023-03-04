from Domain.tranzactie import creeaza_tranzactie,get_ziua,set_tip,set_suma,get_tip,get_suma,set_ziua

def adaugaTranzactie(ziua,suma,tip,listaTranzactii):
    '''
    adauga o tranzactie in lista
    :param ziua: nr intreg
    :param suma: nr intreg
    :param tip: string
    :param listaTranzactii:lista de dictionare de tipul tranzactie
    :return:
    '''

    tranzactie = creeaza_tranzactie(ziua,suma,tip)
    listaTranzactii.append(tranzactie)

def modificaTranzactie(ziua,sumaNoua,tipNou,listaTranzactii):
    '''
    modifica o tranzactie existenta in lista
    :param ziua:int
    :param sumaNoua: int
    :param tipNou: string
    :param listaTranzactii: lista de dictionare de tip tranzactie
    :return:
    '''
    for tranzactie in listaTranzactii:
        if get_ziua(tranzactie) == ziua:
            set_suma(tranzactie, sumaNoua)
            set_tip(tranzactie, tipNou)

def stergeTranzactie(ziua, listaTranzactii):
    '''
    sterge o tranzactie dupa ziua efectuarii
    :param ziua: nr. intreg
    :param listaTranzactii: lista de dictionare de tipul tranzactii
    :return:
    '''
    for tranzactie in listaTranzactii:
        if get_ziua(tranzactie) == ziua:
            listaTranzactii.remove(tranzactie)
    # list_noua = []
    # for tranzactie in listaTranzactii:
    #     if get_ziua(tranzactie) == ziua:
    #         tranzactie=tranzactie+1
    #     else :
    #         list_noua.append(tranzactie)
    # return list_noua

def stergeTranzactiePerioada(ziua1,ziua2,listaTranzactii):
    '''
    sterge tranzactiile dintr-o perioada data
    :param ziua1: int
    :param ziua2: int
    :param listaTranzactii: lista
    :return:
    '''
    i=0
    while i<len(listaTranzactii):
        if get_ziua(listaTranzactii[i])>=ziua1 and get_ziua(listaTranzactii[i])<=ziua2:
            listaTranzactii.pop(i)
            i=i-1
        i += 1

def stergeTranzactieDupaTip(tip,listaTranzactii):
    '''
    sterge o tranzactie dupa tipul ei
    :param tip: string
    :param listaTranzactii: lista
    :return:
    '''
    i = 0
    while i < len(listaTranzactii):
        if get_tip(listaTranzactii[i]) == tip:
            listaTranzactii.pop(i)
            i = i - 1
        i += 1

def stergeTranzactieDupaTipMaiMicaDecatOSuma(suma,tip,listaTranzactii):
    i=0
    while i< len(listaTranzactii):
        if get_tip(listaTranzactii[i]) == tip:
            if get_suma(listaTranzactii[i])<suma:
                listaTranzactii.pop(i);
                i=i-1
        i+=1


def cautaTranzactieSuma(suma,listaTranzactii):
    '''
    se cauta o tranzactie cu suma mai mare decat o suma data
    :param suma: int
    :param listaTranzactii: lista
    :return:
    '''
    rezultat=[]
    for tranzactie in listaTranzactii:
        if get_suma(tranzactie)>suma:
            rezultat.append(tranzactie)
    return rezultat

def cautaTranzactieZiSuma(ziua,suma,listaTranzactii):
    '''
    se cauta o tranzactie inainte de o zi data si cu suma mai mare decat suma data
    :param ziua: int
    :param suma: int
    :param listaTranzactii: lista
    :return:
    '''
    rezultat=[]
    for tranzactie in listaTranzactii:
        if get_suma(tranzactie)>suma and get_ziua(tranzactie)<ziua:
            rezultat.append(tranzactie)
    return rezultat

def cautaTranzactieTip(tip,listaTranzactii):
    '''
    se cauta o tranzactie in functie de tipul ei
    :param tip: string
    :param listaTranzactii: lista
    :return:
    '''
    rezultat=[]
    for tranzactie in listaTranzactii:
        if get_tip(tranzactie) == tip:
            rezultat.append(tranzactie)
    return rezultat

def sumaPreturiPerTip(listaTranzactii):
    '''
    determina suma tranzactiilor per tip
    :param listaTranzactii: lista de dicitonare de tip tranzactie
    :return: un dicitonar continand drept chei tipul tranzactiei
             si drept valori suma tranzactiilor respective
    '''
    rezultat = {}
    for tranzactie in listaTranzactii:
        tip = get_tip(tranzactie)
        suma = get_suma(tranzactie)
        if tip in rezultat:
            rezultat[tip] += suma
        else:
            rezultat[tip] = suma
    return rezultat

def soldData(ziua,listaTranzactii):
    '''
    determina soldul contului la o data specificata
    :param listaTranzactii: lista de dict de tip tranzactie
    :return: soldul de tip int
    '''
    sold = 0
    for tranzactie in listaTranzactii:
        if get_ziua(tranzactie) <= ziua:
            if get_tip(tranzactie) == "intrare":
                sold = sold + get_suma(tranzactie)
            else:
                sold = sold - get_suma(tranzactie)
    return sold


def ordineTipSuma(listaTranzactii):
    '''
    ordoneaza tranzactiile de un anumit tip dupa suma
    :param listaTranzactii: lista
    :return: doua liste
    '''
    listaSuma = []
    listaSuma2 = []
    for tranzactie in listaTranzactii:
        if get_tip(tranzactie) == "intrare":
            listaSuma.append(tranzactie)
        else:
            listaSuma2.append(tranzactie)


    print(sorted(listaSuma,key=lambda tranzactie: get_suma(tranzactie)))
    print(sorted(listaSuma2,key=lambda tranzactie: get_suma(tranzactie)))


