"""
Ohjelma on 3x3 ristinollasovellus, jossa vuoro vaihtuu automaattisesti kun
yksi pelaaja on painanut/merkannut jonkin ruudun painamalla sitä. Oikealla
näkyy vuorossa olevan pelaajan numero ja molempien pelaajien voittamien
pelien lukumäärät.
Pelin voi aloittaa alusta painamalla keltaista Uusi peli-nappia ja lopettaa
punaista Lopeta-nappia painamalla. Aloittava pelaaja vaihtuu automaattisesti
kun painetaan Uusi peli-nappia.
"""
from tkinter import *

MERKIT = ["X", "O"]

class gui:
    def __init__(self):
        self.__MainWindow = Tk()

        self.__ristikko = []
        self.__pelaaja = 0
        self.__aloittaja = 0
        self.__pelaajavoitot = [0, 0]
        self.__peliOhi = 0

        for i in range(3):
            tmp = []
            for j in range(3):
                nappi = Button(self.__MainWindow, text = "", height = 2, width = 5)
                nappi.grid(row = i, column = j, sticky = "EW")
                pos = [i, j]
                nappi["command"] = lambda pos=pos: self.aseta(pos)
                tmp.append(nappi)
            self.__ristikko.append(tmp)



        self.__clearnappi = Button(self.__MainWindow, text = "Uusi peli", command = self.clear, bg = 'yellow')
        self.__clearnappi.grid(row = 3, columnspan = 3)

        self.__lopetusnappi = Button(self.__MainWindow, text = "Lopeta", command = self.exit, bg = 'red')
        self.__lopetusnappi.grid(row = 4, columnspan = 3)

        self.__vuorolabel = Label(text = "Pelaajan {} vuoro".format(self.__pelaaja+1), width = 30)
        self.__vuorolabel.grid(row = 0, column = 3)

        self.__p1voittolabel = Label(text = "Pelaaja 1 voittanut {} kertaa".format(self.__pelaajavoitot[0]))
        self.__p1voittolabel.grid(row = 1, column = 3)

        self.__p2voittolabel = Label(text = "Pelaaja 2 voittanut {} kertaa".format(self.__pelaajavoitot[1]))
        self.__p2voittolabel.grid(row = 2, column = 3)

        self.__MainWindow.mainloop()

    def aseta(self, rowcol):
        """
        Asettaa ruudulle joko Xn tai On riippuen siitä, kumman pelaajan
        vuoro on ja vaihtaa vuoron toiselle pelaajalle jos kyseinen ruutu
        on tyhjä
        :param rowcol: lista, jossa on rivi- ja sarakenumerot
        :return:
        """
        row = rowcol[0]
        col = rowcol[1]
        nappi = self.__ristikko[row][col]
        if nappi["text"] == "" and not self.__peliOhi:
            nappi["text"] = MERKIT[self.__pelaaja]
            self.__pelaaja = invert(self.__pelaaja)
            self.__vuorolabel["text"] = "Pelaajan {} vuoro".format(self.__pelaaja+1)
            if self.voittiko(row, col):
                self.__pelaajavoitot[invert(self.__pelaaja)] += 1
                self.__peliOhi = 1
                self.__vuorolabel["text"] = "Pelaaja {} voitti! Aloita uusi peli".format(invert(self.__pelaaja)+1)

                self.__p1voittolabel = Label(text = "Pelaaja 1 voittanut {} kertaa".format(self.__pelaajavoitot[0]))
                self.__p1voittolabel.grid(row = 1, column = 3)

                self.__p2voittolabel = Label(text = "Pelaaja 2 voittanut {} kertaa".format(self.__pelaajavoitot[1]))
                self.__p2voittolabel.grid(row = 2, column = 3)

    def voittiko(self, row, col):
        """
        Tarkistaa onko taululla kolmen suoraa, palauttaa True jos on,
        False jos ei
        :param row: Edellisen painalluksen rivi
        :param col: Edellisen painalluksen sarake
        :return: True jos on kolmen rivi, False jos ei
        """
        taulu = []
        for i in self.__ristikko:
            tmp = []
            for j in i:
                tmp.append(j["text"])
            taulu.append(tmp)

        if taulu[0][col] == taulu[1][col] == taulu[2][col] != "":
            return True
        elif taulu[row][0] == taulu[row][1] == taulu[row][2] != "":
            return True
        elif taulu[0][0] == taulu[1][1] == taulu[2][2] != "":
            return True
        elif taulu[0][2] == taulu[1][1] == taulu[2][0] != "":
            return True
        else:
            return False

    def clear(self):
        """
        Tyhjentää taulun, palauttaa alkuarvot ja vaihtaa aloittavaa
        pelaajaa
        :return:
        """
        for i in self.__ristikko:
            for j in i:
                j["text"] = ""
        self.__pelaaja = invert(self.__aloittaja)
        self.__aloittaja = invert(self.__aloittaja)
        self.__peliOhi = 0

        self.__vuorolabel = Label(text = "Pelaajan {} vuoro".format(self.__pelaaja+1), width = 30)
        self.__vuorolabel.grid(row = 0, column = 3)

    def exit(self):
        """
        Sulkee ikkunan
        :return:
        """
        self.__MainWindow.destroy()

def invert(i):
    """
    Kääntää ykkösen nollaksi ja toisin päin
    :param i: Käännettävä luku
    :return: Käännetty luku
    """
    if i == 0:
        return 1
    else:
        return 0

def main():
    kali = gui()

main()