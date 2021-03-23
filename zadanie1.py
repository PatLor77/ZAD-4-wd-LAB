lista1 = [0+x for x in range(1, 31, 1)]
lista2 = [str(x*2) for x in lista1]
plik = open("policzx2.txt", "w")
plik.writelines(lista2)



