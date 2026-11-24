import funkcje.2d as pl
import funkcje.warunki_tr as tr
import funkcje.bryly as br 


def legenda()->None:
    print("a - bryly")
    print("b - plaskie")
    print("c - warunki dla trojkata")
    print("e -porzuc program")

def main()->None:
    while True:
        legenda()
        inp = input().lower().strip()
        if inp == "a":
            br.bryly()
        elif inp == "b":
            pl.plaskie()
        elif inp == "c":
            tr.trojkaty()
        elif inp == "e":
            print("Program zkonczyl dzialanie")
            break
        else:
            "Nie ma takiej komendy"

# --------------------------------------------------------------------------
main()