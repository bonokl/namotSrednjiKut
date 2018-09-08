Utori = [["-B","-B","A","A","-C","-C","B","B","-A","-A","C","C"],["C","-B","-B","A","A","-C","-C","B","B","-A","-A","C"]]

utor = 0
kutUtora = 6.
prosjecniKut = []
pocetniKut = kutUtora/2
while(True):
    suma = pocetniKut
    brojac = 0
    flagZona = False
    for i in range(utor, len(Utori[0])):
        if "A" in Utori[0][i] or "A" in Utori[1][i]:
            noKut = int("A" in Utori[0][i]) + int("A" in Utori[1][i])
            brojac += noKut
            suma += noKut*kutUtora*i
            flagZona = True
        if "A" not in Utori[0][i] and "A" not in Utori[1][i] and flagZona:
            prosjecniKut.append(suma/brojac)
            utor = i
            break
    if utor >= len(Utori[0])-1:
        break

print(prosjecniKut)


