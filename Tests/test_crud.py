from Domain.tranzactie import get_ziua, get_suma, get_tip
from Logic.CRUD import adaugaTranzactie, stergeTranzactie, modificaTranzactie


def test_adaugare():
    lista = adaugaTranzactie(12,100,"iesire",[])
    # aici verificam cate elem avem in lista
    assert len(lista) == 1
    assert get_ziua(lista[0]) == 12
    assert get_suma(lista[0]) == 100
    assert get_tip(lista[0]) == "iesire"

def test_stergere():
    lista=[]
    lista = adaugaTranzactie(12,100,"iesire",lista)
    lista = adaugaTranzactie(13,35,"intrare",lista)
    lista=stergeTranzactie(12,lista)
    assert len(lista)==1
    #assert get_ziua(12)is None
    #assert get_ziua(13) is not None

def test_modificare():
    lista = []
    lista = adaugaTranzactie(12, 100, "iesire", lista)
    lista = adaugaTranzactie(13, 35, "intrare", lista)

    lista = modificaTranzactie(12, 50,"intrare", lista)
    tranzactie_updatata=get_ziua(12)
    assert get_ziua(tranzactie_updatata) == 12
    assert get_suma(tranzactie_updatata) == 50
    assert get_tip(tranzactie_updatata) == "intrare"

    tranzactie_neupdatata=get_ziua(13)
    assert get_ziua(tranzactie_neupdatata) == 13
    assert get_suma(tranzactie_neupdatata) == 35
    assert get_tip(tranzactie_neupdatata) == "intrare"

