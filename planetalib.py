import matplotlib.pyplot as plt
import math as mat


class Planeta:
    def __init__(self, nazwa_planety, pozycja_planety, orientacja_planety, promien_planety):
        self.nazwa_planety = nazwa_planety
        # współrzędne kartezjańskie środka planety (x, y)
        self.pozycja_planety = pozycja_planety
        # obrót planety względem środka, kąt (w stopniach) liczony od osi pionowej (12 godzina na zegarze)
        self.orientacja_planety = orientacja_planety
        self.promien_planety = promien_planety
        self.kolor_planety = "yellow"
        # cechy atmosfery: grubość (względem średnicy), kolor, przejrzystość (alpha)
        self.atmosfera = (0.5, "deepskyblue", 0.2)
        # pozycja wejścia kąt (w stopniach) między osią pionową (12 godzina na zegarze) a promieniem
        self.wejscie = ()
        self.wyjscie = ((225, 2000), (315, 3000), (45, 2000), (135, 1000))
        # współrzędne biegunowe sąsiednich planet (fi, r):
        # - kąt (w stopniach) między osią pionową (12 godzina na zegarze) a promieniem wodzącym
        # - promień wodzący (łączy środki planet)

    def dodaj_do_mapy(self, mapa):
        # atmosfera
        mapa.add_artist(plt.Circle(self.pozycja_planety, self.promien_planety *
                                   (1 + self.atmosfera[0]), color=self.atmosfera[1], alpha=self.atmosfera[2]))
        # planeta
        mapa.add_artist(plt.Circle(self.pozycja_planety,
                                   self.promien_planety, color=self.kolor_planety))
        # biegun północny
        wspolrzedne_bieguna_polnocnego = (
            self.pozycja_planety[0] + (self.promien_planety - 20) *
            mat.sin(mat.radians(self.orientacja_planety)),  # x wejścia
            self.pozycja_planety[1] + (self.promien_planety - 20) * \
            mat.cos(mat.radians(self.orientacja_planety))   # y wejścia
        )
        mapa.add_artist(plt.Circle(
            wspolrzedne_bieguna_polnocnego, 20, color="white", alpha=0.8))
        # wejścia
        for wejscie in self.wejscie:
            wspolrzedne_wejscia = (
                self.pozycja_planety[0] + (self.promien_planety + 20) * mat.sin(
                    mat.radians(wejscie + self.orientacja_planety)),  # x wejścia
                self.pozycja_planety[1] + (self.promien_planety + 20) * mat.cos(
                    mat.radians(wejscie + self.orientacja_planety))   # y wejścia
            )
            mapa.add_artist(plt.Circle(wspolrzedne_wejscia,
                                       20, color="green", alpha=0.8))
        # wyjścia
        for wyjscie in self.wyjscie:
            wspolrzedne_wyjscia = (
                self.pozycja_planety[0] + (self.promien_planety + 20) * mat.sin(
                    mat.radians(wyjscie[0] + self.orientacja_planety)),  # x wyjścia
                self.pozycja_planety[1] + (self.promien_planety + 20) * mat.cos(
                    mat.radians(wyjscie[0] + self.orientacja_planety))   # y wyjścia
            )
            mapa.add_artist(plt.Circle(wspolrzedne_wyjscia,
                                       20, color="red", alpha=0.8))

    def wyznacz_wspolrzedne_sasiadow(self):
        wspolrzedne_sasiadow = []
        for sasiednia_planeta in self.wyjscie:
            wspolrzedne_sasiada = ((
                self.pozycja_planety[0] + sasiednia_planeta[1] * mat.sin(
                    mat.radians(sasiednia_planeta[0] + self.orientacja_planety)),   # x sąsiada
                self.pozycja_planety[1] + sasiednia_planeta[1] * mat.cos(
                    mat.radians(sasiednia_planeta[0] + self.orientacja_planety))    # y sąsiada
            ),
                # orientacja sąsiada
                (sasiednia_planeta[0])
            )
            wspolrzedne_sasiadow.insert(0, wspolrzedne_sasiada)
        return wspolrzedne_sasiadow


class Planeta2A(Planeta):
    def __init__(self, nazwa_planety, pozycja_planety=(0, 0), orientacja_planety=0, promien_planety=50):
        Planeta.__init__(self, nazwa_planety, pozycja_planety,
                         orientacja_planety, promien_planety)
        self.kolor_planety = "orange"
        self.atmosfera = (0.5, "deepskyblue", 0.2)
        self.wejscie = (180,)
        self.wyjscie = ((270, 200), (45, 100))


class Planeta2B(Planeta):
    def __init__(self, nazwa_planety, pozycja_planety=(0, 0), orientacja_planety=0, promien_planety=100):
        Planeta.__init__(self, nazwa_planety, pozycja_planety,
                         orientacja_planety, promien_planety)
        self.kolor_planety = "springgreen"
        self.atmosfera = (0.5, "deepskyblue", 0.2)
        self.wejscie = (180,)
        self.wyjscie = ((225, 300), (0, 100))


class Planeta2C(Planeta):
    def __init__(self, nazwa_planety, pozycja_planety=(0, 0), orientacja_planety=0, promien_planety=200):
        Planeta.__init__(self, nazwa_planety, pozycja_planety,
                         orientacja_planety, promien_planety)
        self.kolor_planety = "mediumvioletred"
        self.atmosfera = (0.5, "deepskyblue", 0.2)
        self.wejscie = (180,)
        self.wyjscie = ((315, 100), (90, 200))


class Planeta2D(Planeta):
    def __init__(self, nazwa_planety, pozycja_planety=(0, 0), orientacja_planety=0, promien_planety=200):
        Planeta.__init__(self, nazwa_planety, pozycja_planety,
                         orientacja_planety, promien_planety)
        self.kolor_planety = "mediumvioletred"
        self.atmosfera = (0.5, "deepskyblue", 0.2)
        self.wejscie = (180,)
        self.wyjscie = ((0, 100), (135, 300))


class Planeta3A(Planeta):
    def __init__(self, nazwa_planety, pozycja_planety=(0, 0), orientacja_planety=0, promien_planety=200):
        Planeta.__init__(self, nazwa_planety, pozycja_planety,
                         orientacja_planety, promien_planety)
        self.kolor_planety = "mediumvioletred"
        self.atmosfera = (0.5, "deepskyblue", 0.2)
        self.wejscie = (180,)
        self.wyjscie = ((225, 200), )


class Planeta3B(Planeta):
    def __init__(self, nazwa_planety, pozycja_planety=(0, 0), orientacja_planety=0, promien_planety=200):
        Planeta.__init__(self, nazwa_planety, pozycja_planety,
                         orientacja_planety, promien_planety)
        self.kolor_planety = "mediumvioletred"
        self.atmosfera = (0.5, "deepskyblue", 0.2)
        self.wejscie = (180,)
        self.wyjscie = ((270, 200), )


class Planeta3C(Planeta):
    def __init__(self, nazwa_planety, pozycja_planety=(0, 0), orientacja_planety=0, promien_planety=200):
        Planeta.__init__(self, nazwa_planety, pozycja_planety,
                         orientacja_planety, promien_planety)
        self.kolor_planety = "mediumvioletred"
        self.atmosfera = (0.5, "deepskyblue", 0.2)
        self.wejscie = (180,)
        self.wyjscie = ((225, 300), )


class Planeta3D(Planeta):
    def __init__(self, nazwa_planety, pozycja_planety=(0, 0), orientacja_planety=0, promien_planety=200):
        Planeta.__init__(self, nazwa_planety, pozycja_planety,
                         orientacja_planety, promien_planety)
        self.kolor_planety = "mediumvioletred"
        self.atmosfera = (0.5, "deepskyblue", 0.2)
        self.wejscie = (180,)
        self.wyjscie = ((270, 300), )


class Planeta3E(Planeta):
    def __init__(self, nazwa_planety, pozycja_planety=(0, 0), orientacja_planety=0, promien_planety=200):
        Planeta.__init__(self, nazwa_planety, pozycja_planety,
                         orientacja_planety, promien_planety)
        self.kolor_planety = "mediumvioletred"
        self.atmosfera = (0.5, "deepskyblue", 0.2)
        self.wejscie = (180,)
        self.wyjscie = ((90, 200), )


class Planeta3F(Planeta):
    def __init__(self, nazwa_planety, pozycja_planety=(0, 0), orientacja_planety=0, promien_planety=200):
        Planeta.__init__(self, nazwa_planety, pozycja_planety,
                         orientacja_planety, promien_planety)
        self.kolor_planety = "mediumvioletred"
        self.atmosfera = (0.5, "deepskyblue", 0.2)
        self.wejscie = (180,)
        self.wyjscie = ((135, 200), )


class Planeta3G(Planeta):
    def __init__(self, nazwa_planety, pozycja_planety=(0, 0), orientacja_planety=0, promien_planety=200):
        Planeta.__init__(self, nazwa_planety, pozycja_planety,
                         orientacja_planety, promien_planety)
        self.kolor_planety = "mediumvioletred"
        self.atmosfera = (0.5, "deepskyblue", 0.2)
        self.wejscie = (180,)
        self.wyjscie = ((90, 300), )


class Planeta3H(Planeta):
    def __init__(self, nazwa_planety, pozycja_planety=(0, 0), orientacja_planety=0, promien_planety=200):
        Planeta.__init__(self, nazwa_planety, pozycja_planety,
                         orientacja_planety, promien_planety)
        self.kolor_planety = "mediumvioletred"
        self.atmosfera = (0.5, "deepskyblue", 0.2)
        self.wejscie = (180,)
        self.wyjscie = ((135, 300), )


class Planeta4(Planeta):
    def __init__(self, nazwa_planety, pozycja_planety=(0, 0), orientacja_planety=0, promien_planety=200):
        Planeta.__init__(self, nazwa_planety, pozycja_planety,
                         orientacja_planety, promien_planety)
        self.kolor_planety = "mediumvioletred"
        self.atmosfera = (0.5, "deepskyblue", 0.2)
        self.wejscie = (180,)
        self.wyjscie = ()
