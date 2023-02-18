class vino:
    def __init__(self,nome,colore,gradoalcolico,zonaproduzione):
        self.nome = nome
        self.colore = colore
        self.gradoalcolico = gradoalcolico
        self.zonaproduzione = zonaproduzione


vini = []
ga = 0
ngpa = ""
cgpa = ""
conta_zf = 0
checkGrado = False
checkColore = False
coloriVino = ["rosso","bianco","rosato"]

for i in range(30):
    checkGrado = False
    checkColore = False
    print (i,")")
    nome = input("Inserisci il nome del vino ")
    while checkColore == False:
        colore = input("Rosso/Bianco/Rosato ")
        if colore.lower() in coloriVino:
            checkColore = True
    
    while checkGrado == False:
        gradoalcolico = int(input("Inserisci il grado alcolico del vino "))
        if (gradoalcolico >= 3) and (gradoalcolico <= 40):
            checkGrado = True
    zonaproduzione = input("Inserisci la zona di produzione del vino ")

    vini.append(vino(nofme, colore, gradoalcolico, zonaproduzione))

for i in range(30):
    if vini[i].gradoalcolico > ga:
        ga = vini[i].gradoalcolico
        ngpa = vini[i].nome 
        cgpa = vini[i].colore
    if vini[i].zonaproduzione == "Zona Friulana":
        conta_zf+=1

print("Il", ngpa, "di colore", cgpa, "è il vino più alcolico")

print("I vini prodotti nella Zona Friulana sono", conta_zf)
