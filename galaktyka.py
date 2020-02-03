from planetalib import *

galaktyka = []


# Planeta centralna (pseudo-gwiazda)
galaktyka.append(Planeta("Planeta x", (10, 10), 0, 300))

# Planety pierwszego rzędu
for i in galaktyka[0].wyznacz_wspolrzedne_sasiadow():
    galaktyka.append(Planeta2B(nazwa_planety="Planeta i",
                               pozycja_planety=i[0], orientacja_planety=i[1]))
    # Planety drugiego rzędu
    for j in galaktyka[-1].wyznacz_wspolrzedne_sasiadow():
        galaktyka.append(Planeta2A(nazwa_planety="Planeta j",
                                   pozycja_planety=j[0], orientacja_planety=i[1] + j[1]))

mapa, uklad = plt.subplots()
uklad.axis('equal')
uklad.axis('off')
uklad.set_xlim((-5000, 5000))
uklad.set_ylim((-5000, 5000))
mapa.tight_layout()

for planeta in galaktyka:
    planeta.dodaj_do_mapy(uklad)

plt.show()
mapa.savefig('galaktyka.png')
