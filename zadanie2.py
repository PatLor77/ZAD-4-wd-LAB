with open("tekst.txt", "w") as plik4:
    for newLine in range(10):
        plik4.write("hehe\n")
with open("tekst.txt", "r") as plik4:
    for line in plik4:
        print(line, end="")


