from Logic.CRUD import sumaPreturiPerTip, ordineTipSuma
from Tests.test_all import run_all_tests
from UI.consola import printMenu, uiadaugaTranzactie, printTranzactie, uimodificareTranzactie, uistergeTranzactie, \
    uistergeTranzactiePerioada, uistergeTranzactieDupaTip, uicautaTranzSuma, uicautaTranzZiSuma, uicautaTranzTip, \
    uisoldData, undoCommand, uistergeTranzactieDupaTipMaiMicaDecatOSuma, redoCommand


def main():
    #run_all_tests()
    redo_list = []
    history=[]
    listaTranz = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            history.append([])
            for tranzactie in listaTranz:
                history[-1].append(tranzactie.copy())
            uiadaugaTranzactie(listaTranz)
        elif optiune =="a":
            printTranzactie(listaTranz)
        elif optiune == "2":
            history.append([])
            for tranzactie in listaTranz:
                history[-1].append(tranzactie.copy())
            uimodificareTranzactie(listaTranz)
        elif optiune == "3":
            history.append([])
            for tranzactie in listaTranz:
                history[-1].append(tranzactie.copy())
            uistergeTranzactie(listaTranz)
        elif optiune == "4":
            history.append([])
            for tranzactie in listaTranz:
                history[-1].append(tranzactie.copy())
            uistergeTranzactiePerioada(listaTranz)
        elif optiune == "5":
            history.append([])
            for tranzactie in listaTranz:
                history[-1].append(tranzactie.copy())
            uistergeTranzactieDupaTip(listaTranz)
        elif optiune == "6":
            printTranzactie(uicautaTranzSuma(listaTranz))
        elif optiune == "7":
            printTranzactie(uicautaTranzZiSuma(listaTranz))
        elif optiune =="8":
            printTranzactie(uicautaTranzTip(listaTranz))
        elif optiune =="9":
            print(sumaPreturiPerTip(listaTranz))
        elif optiune =="10":
            print(uisoldData(listaTranz))
        elif optiune == "11":
            ordineTipSuma(listaTranz)
        elif optiune == "12":
            history.append([])
            for tranzactie in listaTranz:
                history[-1].append(tranzactie.copy())
            uistergeTranzactieDupaTipMaiMicaDecatOSuma(listaTranz)
        elif optiune == "u":
            if len(history) == 0:
                print('Nu mai sunt operatii Undo de efectuat.')
            else:
                new_list = undoCommand(history)
                listaTranz = new_list.copy()
        elif optiune =="r":
            if len(history) == 0:
                print("Nu sunt operatii de redo de efectuat")
            else:
                new_list = redoCommand(history)
                listaTranz = new_list.copy()
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati")

main()
