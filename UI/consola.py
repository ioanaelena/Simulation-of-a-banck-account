from Domain.tranzactie import toString
from Logic.CRUD import adaugaTranzactie, modificaTranzactie, stergeTranzactie, stergeTranzactiePerioada, \
    stergeTranzactieDupaTip, cautaTranzactieSuma, cautaTranzactieZiSuma, cautaTranzactieTip, soldData, \
    stergeTranzactieDupaTipMaiMicaDecatOSuma


def printMenu():
    print("1. Adauga tranzactie")
    print("a.Afiseaza toate tranzactiile")
    print("2. Modifica tranzactie")
    print("3. Sterge tranzactiile dintr-o zi")
    print("4. Sterge tranzactiile dintr-o perioada specificata")
    print("5. Sterge tranzactiile de un anumit tip")
    print("6. Afiseaza tranzactiile cu suma mai mare decat o suma data ")
    print("7.Afiseaza tranzactiile efectuate inainte de o zi si mai mari decat o suma:")
    print("8.Afiseaza tranzactiile de un anumit tip")
    print("9.Afiseaza suma totala a tranzactiilor de un anumit tip")
    print("10.Afiseaza soldul contului pana la o anumita data")
    print("11.Afiseaza tranzactiile de un anumit tip ordonate dupa suma")
    print("12.Elimina tranzactiile de un anumit tip cu o suma mai mica decat o suma data ")
    print("u.Undo")
   # print("r.Redo")
    print("x. Iesire")

def uiadaugaTranzactie(listaTranz):
    ziua = int(input("Dati ziua efectuarii tranzactiei:"))
    suma = int(input("Dati suma tranzactiei:"))
    tip = str(input("Dati tipul tranzactiei: de iesire sau intrare"))
    adaugaTranzactie(ziua,suma,tip,listaTranz)


def printTranzactie(listaTranz):
    for tranzactie in listaTranz:
        print(toString(tranzactie))

def uimodificareTranzactie(listaTranz):
    ziua = int(input("Dati ziua modificarii: "))
    suma = int(input("Dati noua suma a tranzactiei: "))
    tip = str(input("Dati noul tip: "))
    modificaTranzactie(ziua,suma,tip,listaTranz)


def uistergeTranzactie(listaTranz):
    ziua = int(input("Dati ziua de la care se vor sterge toate tranzactiile:"))
    stergeTranzactie(ziua,listaTranz)


def uistergeTranzactiePerioada(listaTranz):
    ziua1=int(input("Dati prima zi din perioada dorita:"))
    ziua2=int(input("Dati ultima zi din perioada dorita:"))
    stergeTranzactiePerioada(ziua1,ziua2,listaTranz)


def uistergeTranzactieDupaTip(listaTranz):
    tip=str(input("Dati tipul tranzactiilor care vor fi sterse :"))
    stergeTranzactieDupaTip(tip,listaTranz)

def uistergeTranzactieDupaTipMaiMicaDecatOSuma(listaTranz):
    tip = str(input("Dati tipul tranzactiilor care vor fi sterse :"))
    suma = int(input("Dati suma pentru care suma tranzactiei sa fie mai mica:"))
    stergeTranzactieDupaTipMaiMicaDecatOSuma(suma,tip,listaTranz)

def uicautaTranzSuma(listaTranz):
    suma = int(input("Dati valoarea sumei pe care o doriti:"))
    return cautaTranzactieSuma(suma,listaTranz)

def uicautaTranzZiSuma(listaTranz):
    ziua = int(input("Dati ziua pentru tranzactiile dorite:"))
    suma = int(input("Dati suma tranzactiilor dorite:"))
    return cautaTranzactieZiSuma(ziua,suma,listaTranz)

def uicautaTranzTip(listaTranz):
    tip = str(input("Dati tipul tranzactiilor cautate:"))
    return cautaTranzactieTip(tip,listaTranz)

def uisoldData(listaTranz):
    ziua = int(input("Dati ziua la care vreti sa stiti soldul :"))
    return soldData(ziua,listaTranz)

def undoCommand(history):
    new_list = history.pop(-1)
    return new_list

def redoCommand(history):
    new_list = history.append(-1)
    return new_list


# def undo(listaTranz, undo_list, redo_list): #intra mereu pe else
#     if len(undo_list) > 0:
#         redo_list.append(listaTranz)
#         listaTranz = undo_list.pop()  # .pop() scoate si ia  ultima valoare din lista
#     else:
#         print("Nu se poate face undo!")
#     return listaTranz

# def main():
#     listaTranz = []
#     while True:
#         printMenu()
#         optiune = input("Dati optiunea: ")
#         if optiune == "1":
#             uiadaugaTranzactie(listaTranz)
#         elif optiune =="a":
#             printTranzactie(listaTranz)
#         elif optiune == "2":
#             uimodificareTranzactie(listaTranz)
#         elif optiune == "3":
#             uistergeTranzactie(listaTranz)
#         elif optiune == "4":
#             uistergeTranzactiePerioada(listaTranz)
#         elif optiune == "5":
#             uistergeTranzactieDupaTip(listaTranz)
#         elif optiune == "6":
#             printTranzactie(uicautaTranzSuma(listaTranz))
#         elif optiune == "7":
#             printTranzactie(uicautaTranzZiSuma(listaTranz))
#         elif optiune =="8":
#             printTranzactie(uicautaTranzTip(listaTranz))
#         elif optiune == "x":
#             break
#         else:
#             print("Optiune gresita! Reincercati")
#
# main()