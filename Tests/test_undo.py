from Logic.CRUD import adaugaTranzactie
from UI.consola import undoCommand


def test_undo():
    # 1 lista goala
    lista = []
    history = []
    lista = adaugaTranzactie(12, 100, "iesire", [])
    history.append([])
    for tranzactie in lista:
        history[-1].append(tranzactie.copy())
    lista = adaugaTranzactie(13, 35, "intrare", lista)
    history.append([])
    for tranzactie in lista:
        history[-1].append(tranzactie.copy())
    assert len(lista) == 2
    lista = undoCommand(history)
    assert len(lista) == 1