def creeaza_tranzactie(ziua,suma,tip):
    '''
    creeaza o lista de tupluri pentru o tranzactie
    :param ziua: ziua in care s a facut tranzactia
    :param suma: suma tranzactiei
    :param tip: tipul : iesire sau intrare
    :return:o lista de tupluri care retine o tranzactie
    '''

    return{
        "ziua": ziua,
        "suma": suma,
        "tip": tip
    }

def get_ziua(tranzactie):
    '''
    da ziua in care s a efectuat tranzactia
    :param tranzactie: un dictionar de tip tranzactie
    :return: ziua efectuarii tranzactiei
    '''

    return tranzactie["ziua"]

def get_suma(tranzactie):
    '''
    da suma tranzactiei
    :param tranzactie: un dict de tip tranzactie
    :return: suma tranzactiei
    '''

    return tranzactie["suma"]

def get_tip(tranzactie):
    '''
    da tipul tranzactiei de intrare sau iesire
    :param tranzactie: un dict de tip tranzactie
    :return: tipul tranzactiei(intrare sau iesire)
    '''

    return tranzactie["tip"]

def set_ziua(tranzactie,ziua):
    tranzactie["ziua"]=ziua

def set_suma(tranzactie,suma):
    tranzactie["suma"]=suma

def set_tip(tranzactie,tip):
    tranzactie["tip"]=tip

def toString(tranzactie):
    return "ziua: " + str(get_ziua(tranzactie)) +  ", suma: " + str(get_suma(tranzactie)) + ", tip: " + get_tip(tranzactie)